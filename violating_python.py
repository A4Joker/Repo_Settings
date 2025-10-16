# Violates: Mixed imports, wrong order
import os
from my_local_module import *
import sys
from third_party import something

# Violates: Global variable
global_data = []

# Violates: Class name should be PascalCase
class badly_named_class:
    
    # Violates: Should be snake_case
    def BadlyNamedMethod(self, param1, param2, param3, param4, param5):
        # Violates: Too many parameters
        
        # Violates: Using global variable
        global global_data
        global_data.append("data")
        
        # Violates: Line too long (over 88 chars)
        very_long_variable_name = "This is a very long string that definitely exceeds the maximum line length of 88 characters"
        
        # Violates: Using % formatting instead of f-strings
        message = "Hello %s, you have %d messages" % ("user", 5)
        
        # Violates: Bare except clause
        try:
            result = 10 / 0
        except:
            pass
            
        # Violates: Using map instead of list comprehension
        numbers = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x**2, numbers))
        
        # Violates: No type hints
        def inner_function(data):
            return data.upper()
            
        return inner_function("test")

# Violates: Function too long and does multiple things
def do_everything():
    # This function is way too long and violates single responsibility
    data = []
    for i in range(100):
        # Violates: Repeated function call in loop
        if len(data) > 50:
            data.clear()
        data.append(i * 2)
        
        # Violates: Deep nesting
        if i % 10 == 0:
            if i % 20 == 0:
                if i % 30 == 0:
                    print("deeply nested")
                    
    # Violates: Not using context manager for file
    file = open("data.txt", "w")
    file.write("some data")
    # Violates: File not closed properly
    
    # Violates: Using global statement
    global global_data
    global_data.extend(data)
    
    # Many more lines making this function too long...
    # ... imagine 40+ more lines here ...
    
    return data

# Violates: No docstring, no type hints
def process_data(input_data, config, options, flags, more_params):
    # Violates: Too many parameters
    result = ""
    for item in input_data:
        result += str(item)  # Violates: String concatenation in loop
        
    return result

# Violates: Using old-style string formatting
def format_message(name, count):
    return "User %s has %d items" % (name, count)

# Violates: No error handling for file operations
def read_file_badly(filename):
    with open(filename, 'r') as f:
        return f.read()
