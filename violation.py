# Violates: File read operation without with
file = open("data.txt", "r")
content = file.read()
file.close()

# Violates: Use of dictionary
data_dict = {"name": "John", "age": 30}

# Violates: Lambda function and lambda assignment
square = lambda x: x * x

# Violates: Implicit return
def check_value(x):
    # Violates: No else for every if condition
    if x > 10:
        return "High"
    # Missing else for the above if
    
    # Violates: use of If True:
    if True:
        return "Always true"

result = square(5)
print(result)
print(check_value(15))
