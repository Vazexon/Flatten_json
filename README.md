# Flatten_json
Here we have a list of improvements that can be done in an existent program.
The resulting program is in test.py

**1.	Optional Folder Path Parameter in init Method**  
•	What: Changed the folder_path parameter in the __init__ method to have a default value of None.  
•	Why: This change allows the user to create an instance of FlattenJson without specifying a folder path, providing more flexibility in object instantiation.  
•	Benefits: Users can set the folder path later using a separate method, offering a more versatile class design.

**2.	Added Type Hints for Improved Readability**  
•	What: Added type hints to function signatures and class attributes.  
•	Why: Type hints enhance code readability and offer better IDE support, aiding developers in understanding the expected data types.  
•	Benefits: Clearer type annotations help prevent type-related errors and make the codebase more maintainable.  

**3.	Improved File Handling with pathlib.Path**  
•	What: Replaced the use of glob with pathlib.Path.rglob for file handling.  
•	Why: pathlib.Path provides a more Pythonic and cross-platform approach to working with file paths.  
•	Benefits: The code is now more readable and portable, making file-related operations easier to comprehend and maintain.  

**4.	Method Returns Result Dictionary Instead of Updating Class Attribute**  
•	What: Modified the flatten_dict method to return a result dictionary instead of updating a class attribute.  
•	Why: Returning the result instead of updating an attribute improves the method's encapsulation and reduces reliance on external state.  
•	Benefits: The flatten_dict method becomes more self-contained, facilitating reusability and testability.  

**5.	Simplified Data Collection with dict.get() Method**  
•	What: Utilized dict.get() method with a default value in the get_keys method.  
•	Why: The get() method simplifies the code by eliminating explicit if/else statements for dictionary updates.  
•	Benefits: The code becomes more concise, easier to read, and less prone to errors, improving code maintainability.  

**6.	Eliminated Unnecessary Class Attributes**  
•	What: Removed unused class attributes (examples and flatten_json).  
•	Why: These attributes were only used locally in the flatten_json_to_excel method and not required as class-level properties.  
•	Benefits: Eliminating unnecessary class attributes reduces memory overhead and enhances code clarity.  

**7.	Optimized DataFrame Operations with Set Index**  
•	What: Set the 'key' column as the index in the examples_df DataFrame.  
•	Why: Setting the index column improves performance for DataFrame lookups and operations based on 'key' values.  
•	Benefits: Faster and more efficient access to specific examples based on their 'key' values.  

**8.	Comprehensive Type Hints for Improved Code Documentation**  
•	What: Added type hints to function arguments, class attributes, and intermediate variables.  
•	Why: Type hints enhance code documentation and provide better IDE support for understanding data types.  
•	Benefits: The code becomes more self-explanatory, reducing ambiguity and promoting safer coding practices.  

**9.	Removing del Statements**  
•	What: The del statements were used to remove specific class attributes that were not needed later in the code.  
•	Why: Removing these attributes is unnecessary and doesn't significantly impact memory usage or performance in this context.  
•	Benefits: Eliminating the del statements simplifies the code and makes it more straightforward, as Python's garbage collection handles the cleanup of unused objects.  

**10.	Removing Looping by Dict Items**  
•	What: The original code used a for loop with dict.items() to iterate through the flatten dictionary in the get_keys() method.  
•	Why: Looping through dict.keys() directly is more efficient when we don't need the corresponding values in the loop.  
•	Benefits: By using dict.keys(), we avoid unnecessary memory overhead and improve performance.  

**11.	Garbage Collection Part**  
•	What: The code used gc.enable() to enable garbage collection.  
•	Why: Enabling garbage collection can be useful in specific scenarios where memory management is critical.  
•	Benefits: In this case, it is not clear whether garbage collection is necessary since Python's garbage collection usually works efficiently on its own. For many use cases, manually enabling garbage collection is not required.  

**12.	Use of List Comprehension in the get_flatten_json Method**  
•	What: The code used list comprehension to create the temp_dict in the get_flatten_json method.  
•	Why: List comprehensions are a concise and efficient way to create lists from iterables.  
•	Benefits: List comprehensions improve code readability and can be more efficient than traditional loops when creating new lists.  

**13.	Exception Handling**  
•	What: The code used a try-except block to catch exceptions when reading JSON files in the read_files method.  
•	Why: Exception handling allows the code to gracefully handle errors during file reading without crashing the entire process.  
•	Benefits: With proper exception handling, the program can continue processing other files even if there are issues with one or more JSON files.  

**14.	Optimizing get_keys Method**  
•	What: The original code had nested loops in the get_keys method, which could be inefficient for large JSON files.  
•	Why: Optimizing the method to update the counters directly in self.collected_data_from_file for each JSON file avoids redundant iterations and improves efficiency.  
•	Benefits: The optimized method reduces the overall time complexity and improves performance, especially when dealing with large JSON files.  

**15.	Redundant Dictionary Update**  
•	What: The original code collected data in both self.collected_data_from_file and self.temp_examples.  
•	Why: Storing data in both dictionaries is unnecessary duplication of information and can increase memory usage.  
•	Benefits: By eliminating self.temp_examples and directly updating the self.collected_data_from_file dictionary, we reduce memory overhead and simplify the code.  

**16.	Use of OrderedDict**  
•	What: The code uses collections.OrderedDict in the flatten_dict method.  
•	Why: OrderedDict preserves the order of insertion, which ensures that the order of keys in the flattened dictionary is consistent with the order of appearance in the JSON.  
•	Benefits: When dealing with JSON data where the order of keys matters, using OrderedDict ensures that the output maintains the original order, making it useful in specific scenarios.  
