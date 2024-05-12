# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements of a dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Modifying elements of a dictionary
my_dict['age'] = 31
print("Updated age:", my_dict['age'])

# Adding new key-value pairs
my_dict['job'] = 'Engineer'
print("Job:", my_dict['job'])

# Removing key-value pairs
del my_dict['city']
print("Dictionary after removing 'city':", my_dict)

# Iterating over a dictionary
print("Iterating over the dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)

# Length of a dictionary
print("Length of dictionary:", len(my_dict))

# Checking if a key exists in a dictionary
print("Check if 'name' exists in dictionary:", 'name' in my_dict)

# Getting a list of keys and values
keys = my_dict.keys()
values = my_dict.values()
print("Keys:", keys)
print("Values:", values)

# Creating a dictionary using dict() constructor
another_dict = dict(name='Alice', age=25, city='London')
print("Another dictionary:", another_dict)

# Copying a dictionary
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)

# Clearing a dictionary
my_dict.clear()
print("Cleared dictionary:", my_dict)
