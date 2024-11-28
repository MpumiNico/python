# Given string
s = 'fullstackslp'

# 1. Print the first character 'f' using indexing
print(s[0])

# 2. Print the last character 'p' using indexing
print(s[-1])

# 3. Print the substring 'stack' using slicing
print(s[4:9])

# 4. Print the substring 'slp' using slicing
print(s[9:])

# 5. Reverse the entire string using slicing and print
print(s[::-1])

# Given dictionaries
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

# 6. Grab 'hello' from the dictionary d1
print(d1['simple_key'])

# 7. Grab 'hello' from the nested dictionary d2
print(d2['k1']['k2'])

# 8. Grab 'hello' from the deeply nested dictionary d3
print(d3['k1'][0]['nest_key'][1][0])

# List with values
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]

# 9. Use a set to find the unique values of the list
unique_values = set(mylist)
print(unique_values)

# Variables
age = 45
name = "Kyle"

# 10. Use print formatting to print the desired string
print(f"Hello my dog's name is {name} and he looks {age} years old.")
