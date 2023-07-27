#!/usr/bin/env python
from typing import Optional, List
import json
from glob import glob
import pandas as pd
from pandas import json_normalize
from tqdm import tqdm


class FlattenJson:
    def __init__(self, folder_path: Optional[str] = None, encoding: Optional[str] = None, amount_of_examples: int = 1000):
        self.folder_paths: List[str] = self.get_files_from_folder(folder_path)
        self.encoding: Optional[str] = encoding
        self.collected_data_from_file: = {}
        self.amount_of_examples: int = amount_of_examples

    def get_files_from_folder(self, folder_path: Optional[str]) -> List[str]:
        if not folder_path.endswith('*.json'):
            folder_path = folder_path + '*.json'
        files: = [str(file) for file in glob(folder_path, recursive=True)]
        if len(files) == 0:
            raise ValueError("0 files in folder.")
        return files

    @staticmethod
    def flatten_dict(nested_dict: dict, schema_name: str = "") -> dict:
        result: = {}

        if schema_name:
            schema_name = schema_name + ' =>'

        def flatten(data, name = '') -> None:
            if isinstance(data, dict):
                for elem in data:
                    if elem.startswith(('http://', 'https://')):
                        flatten(data[elem], name + '[url]' + ' => ')
                    else:
                        flatten(data[elem], name + elem + ' => ')
            elif isinstance(data, list):
                [flatten(elem, name + '[]' + ' => ') for elem in data]
            else:
                data = str(data)
                if name[:-4] not in result:
                    result[name[:-4]] = data
                else:
                    if isinstance(result[name[:-4]], str):
                        result[name[:-4]] = [result[name[:-4]], data]
                    else:
                        result[name[:-4]].append(data)

        flatten(nested_dict, schema_name)
        for key, value in result.items():
            if isinstance(value, list):
                result[key] = '; '.join(value[:10])
        return result

    def get_keys(self, json_input) -> None:
        flatten: dict = self.flatten_dict(json_input)
        for key in flatten:
            self.collected_data_from_file[key] = self.collected_data_from_file.get(key, {"counter": 0})
            self.collected_data_from_file[key]["counter"] += 1

    def read_files(self) -> None:
        print(f'Getting keys from {len(self.folder_paths)} files.')
        for file_path in tqdm(self.folder_paths):
            try:
                with open(file_path, 'r', encoding=self.encoding) as f:
                    content = json.loads(f.read())
                    self.get_keys(content)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    def get_flatten_json(self) -> None:
        print(f'Fixing {len(self.collected_data_from_file)} keys.')
        temp_dict: List[dict] = [{"key": key, "counter": value["counter"]} for key, value in self.collected_data_from_file.items()]
        self.collected_data_from_file = temp_dict

    def flatten_json_to_excel(self, output_file_name: str) -> None:
        print('Preparing flatten data.')
        flatten_df: pd.DataFrame = pd.DataFrame(self.collected_data_from_file)['key']

        print('Preparing counter data.')
        flatten_counter_df: pd.DataFrame = pd.DataFrame(self.collected_data_from_file).sort_values(
            by='counter', ascending=False
        )

        print('Preparing examples data.')
        examples_df: pd.DataFrame = pd.DataFrame(self.collected_data_from_file).head(self.amount_of_examples)
        examples_df.set_index('key', inplace=True)

        print('Writing data to excel.')
        writer: pd.ExcelWriter = pd.ExcelWriter(f"{output_file_name}.xlsx", engine='xlsxwriter')
        flatten_df.to_excel(writer, sheet_name='unique keys', index=False, encoding=self.encoding)
        flatten_counter_df.to_excel(writer, sheet_name='count of keys', index=False, encoding=self.encoding)
        examples_df.to_excel(writer, sheet_name='examples', index=True, encoding=self.encoding)

        writer.save()

        print(f'Excel file saved:\n{output_file_name}')
