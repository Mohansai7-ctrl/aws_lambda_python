"""
variables
conditions
loops
functions

DevOps Use case: Cost Optimization
   - CRON job schedule: *   *  *  *  *
AWS Lambda
Modules
"""

# print("Hello World")

# Variables
# 1. Integer
# 2. Float / double
# 3. Strings
# 4. Boolean
# 5. List
# 6. Tuples
# 7. Dictonary
# 8. Sets

# List and tuples both are not same?

# res = 10 + 20
# print("Result: ", res)
# # print(10 + 20)
# print("Memory Address: ",id(res))

# # There are methods specific to that data type 
# print("Data type: ", type(res))

"""
this is a block comment
"""

# This is a line comment

# a = 10.23
# b = 20.34
# res = a + b
# print("Result:", res, "Type:", type(res))

# sample_str = "this is a string"
# print(sample_str, type(sample_str))
# print(dir(sample_str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""
# print(sample_str.capitalize())
# print(sample_str.casefold())
# # print(sample_str.center())

# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)

# print(txt.swapcase())
# print(txt.split(' '))
# print(txt.find('M'))

# Python uses zero indexing
# sample_str = "Hello"
# print(sample_str.index('H'))
# print(sample_str.index('o'))

# sample_char = sample_str[-1]
# print(sample_char)
# print(len(sample_str))


# a = True
# b = False

# print(a and b) # False
# print(a or b)  # True

# a = 2
# b = 4

# print(a + b) # addition
# print(a - b) # substraction
# print(a * b) # multiplication
# print(a / b) # division
# print(b % a) # modulo division: returns remainder
# print(a // b) # Integer division
# print(a ** b) # exponentiation

# 1234 = 10

sample_str = "this is a string"
sample_str[0] = 'T'
# TypeError: 'str' object does not support item assignment

print(sample_str)