Skip to content
 Enterprise
Search or jump to…
Pull requests
Issues
Explore
 
@akshaysamalbito 
akshaysamalbito
/
agent_rules
Public
Code
Issues
Pull requests
38
Actions
Projects
Wiki
Security
Insights
Settings
agent_rules
/
code_quality_violations.py
in
Rules-and-Guidelines-Citation-with-Custom-Guidelines_27
 

Spaces

4

No wrap
1
​
2
​
3
def x(a, b):  
4
    return a + b
5
​
6
def process_data():
7
    data = get_data()
8
    result = []
9
    for i in data:
10
        if i > 10:
11
            result.append(i * 2)
12
        else:
13
            result.append(i)
14
    return result
15
​
16
def handle_user_registration_and_validation_and_email_sending_and_profile_creation(user_data, email_service, profile_service, validation_service):
17
​
18
    if validate_user_data(user_data):
19
        user = create_user(user_data)
20
        send_welcome_email(user, email_service)
21
        create_user_profile(user, profile_service)
22
        log_registration(user)
23
        return user
24
    else:
25
        return None
26
​
27
​
28
def calculate_total(items, tax_rate, discount):
29
​
30
    subtotal = sum(item['price'] for item in items)
31
    tax = subtotal * tax_rate
32
    total = subtotal + tax - discount
33
    return total
34
​
35
def read_config_file(file_path):
36
    config = open(file_path).read()  
37
    return parse_config(config)
38
​
@akshaysamalbito
Commit changes
Commit summary
Create code_quality_violations.py
Optional extended description
Add an optional extended description…
 Commit directly to the Rules-and-Guidelines-Citation-with-Custom-Guidelines_27 branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
FooterBito Inc
Bito Inc
Bito Inc
© 2026 GitHub, Inc.
Footer navigation
Help
Support
API
Training
Blog
About
GitHub Enterprise Server 3.11.19
Editing agent_rules/code_quality_violations.py at Rules-and-Guidelines-Citation-with-Custom-Guidelines_27 · akshaysamalbito/agent_rules
