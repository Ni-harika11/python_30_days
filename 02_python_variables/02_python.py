# # //Varibale
# # //1.Start with letters or underscore
# # //2.cannot start with number
# # //3.only contains alpha numeric characters and underscores
# # //4.variable name is case sensitive(Firtsname and firstname are different variables)

# # Variables in Python
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Asabeneh',
#    'lastname':'Yetayeh',
#    'country':'Finland',
#    'city':'Helsinki'
#    }
# print('Hello, World!') # The text Hello, World! is an argument
# print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
# print(len('Hello, World!')) # it takes only one argument
# # Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)
# # Declaring Multiple Variable in a Line
# # Multiple variables can also be declared in one line:

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

# location = input("What is your 20 ?")
# age = input("Do you want 86 me?.")
# print(first_name)
# print(age)
# # Checking Data types and Casting
# # Different python data types
# # Let's declare variables with various data types

# first_name = 'Asabeneh'     # str
# last_name = 'Yetayeh'       # str
# country = 'Finland'         # str
# city= 'Helsinki'            # str
# age = 250                   # int, it is not my real age, don't worry about it

# # Printing out types
# print(type('Asabeneh'))          # str
# print(type(first_name))          # str
# print(type(10))                  # int
# print(type(3.14))                # float
# print(type(1 + 1j))              # complex
# print(type(True))                # bool
# print(type([1, 2, 3, 4]))        # list
# print(type({'name':'Asabeneh'})) # dict
# print(type((1,2)))               # tuple
# print(type(zip([1,2],[3,4])))    # zip
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
# Directly converting a decimal string to int is not possible.
# First, convert the string to float, then convert the float to int.
# print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

# Numbers data types
# 1) Integers: Whole numbers without a decimal point. Example: -2, 0, 5, 100
# 2) Float: Numbers with a decimal point. Example: -2.5, 0.0, 3.14, 100.0
# 3) Complex: Numbers with a real and imaginary part. Example: 1 + 2j, 3 - 4j
