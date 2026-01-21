# VIOLATES: No type annotations, no docstrings
def process_data(data, config, options):  # No types, no docstring
    result = ""
    for item in data:
        result += str(item)  # No type safety
    return result  # Unknown return type

class DataProcessor:  # No docstring
    def __init__(self):
        self.cache = []  # No type annotation
        
    def add_item(self, item):  # No types, no docstring
        self.cache.append(item)
        return len(self.cache)  # Inconsistent return type
# VIOLATES: Too many params, too long, multiple responsibilities
def do_everything(data, config, user, context, flags, options, settings):  # 7 params
    # Function does data processing, validation, and formatting
    if not data:
        return None
    
    # Process data
    processed = []
    for item in data:
        if item > 0:
            processed.append(item * 2)
    
    # Validate results
    if len(processed) == 0:
        raise Exception("No data")
    
    # Format output
    output = {"count": len(processed), "data": processed}
    
    # Log results
    print(f"Processed {len(processed)} items")
    
    return output  # Function too long, multiple responsibilities
# VIOLATES: No type annotations, no docstrings
def process_data(data, config, options):  # No types, no docstring
    result = ""
    for item in data:
        result += str(item)  # No type safety
    return result  # Unknown return type

class DataProcessor:  # No docstring
    def __init__(self):
        self.cache = []  # No type annotation
        
    def add_item(self, item):  # No types, no docstring
        self.cache.append(item)
        return len(self.cache)  # Inconsistent return type
# VIOLATES: Wrong naming conventions throughout
class badClass:  # Should be PascalCase
    def BadMethod(self, x, y):  # Should be snake_case
        A = 5  # Should be lowercase
        Bad_Var = "value"  # Should be snake_case without caps
        return A + Bad_Var

CONSTANT = 10  # Should be UPPER_SNAKE_CASE
mixedCaseVar = "wrong"  # Should be snake_case
