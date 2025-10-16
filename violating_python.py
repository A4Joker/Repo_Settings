import os
from my_local_module import *
import sys
from third_party import something

# VIOLATION: Hardcoded API key
API_KEY = "sk-1234567890abcdef"
global_data = []

class badly_named_class:
    
    def BadlyNamedMethod(self, param1, param2, param3, param4, param5):
        global global_data
        global_data.append("data")
        
        # VIOLATION: Potential XSS if output to web
        user_input = input("Enter your name: ")
        print(f"<div>Hello {user_input}</div>")
        
        very_long_variable_name = "This is a very long string that definitely exceeds the maximum line length of 88 characters"
        message = "Hello %s, you have %d messages" % ("user", 5)
        
        # VIOLATION: Empty except block
        try:
            result = 10 / 0
        except:
            pass
            
        # VIOLATION: Inefficient data structure for large datasets
        numbers = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x**2, numbers))
        
        # VIOLATION: No input validation
        def inner_function(data):
            return data.upper()
            
        # VIOLATION: SQL injection vulnerability
        query = f"SELECT * FROM users WHERE name = '{user_input}'"
        
        return inner_function("test")

def do_everything():
    # VIOLATION: Function too long and violates single responsibility
    data = []
    for i in range(100):
        if len(data) > 50:
            data.clear()
        data.append(i * 2)
        
        # VIOLATION: Deep nesting
        if i % 10 == 0:
            if i % 20 == 0:
                if i % 30 == 0:
                    print("deeply nested")
                    
    # VIOLATION: Resource not properly managed
    file = open("data.txt", "w")
    file.write("some data")
    # File not closed - potential resource leak
    
    # VIOLATION: Code duplication
    save_user_data("John", "john@example.com", "123 Main St")
    save_user_data("Jane", "jane@example.com", "456 Oak Ave")
    save_user_data("Bob", "bob@example.com", "789 Pine St")
    
    global global_data
    global_data.extend(data)
    
    # VIOLATION: No error handling for file operations
    config = load_config("config.json")
    
    return data

# VIOLATION: Duplicated code pattern
def save_user_data(name, email, address):
    print(f"Saving user: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("-" * 30)

# VIOLATION: No input validation, no error handling
def process_data(input_data, config, options, flags, more_params):
    result = ""
    for item in input_data:
        result += str(item)  # VIOLATION: Inefficient string concatenation
        
    return result

def format_message(name, count):
    return "User %s has %d items" % (name, count)

# VIOLATION: No error handling, potential file not found
def read_file_badly(filename):
    with open(filename, 'r') as f:
        return f.read()

# VIOLATION: No input validation, potential security issue
def load_config(config_path):
    # VIOLATION: Using eval on untrusted data
    config_data = read_file_badly(config_path)
    return eval(config_data)

# VIOLATION: Repeated expensive API call
def get_user_profile(user_id):
    # Simulate expensive API call
    import time
    time.sleep(0.5)
    return {"name": "User", "id": user_id}

def process_users(user_ids):
    profiles = []
    for user_id in user_ids:
        # VIOLATION: Expensive operation in loop
        profile = get_user_profile(user_id)
        profiles.append(profile)
    return profiles
