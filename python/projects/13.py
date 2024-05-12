# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Slice of tuple:", my_tuple[2:5])

# Tuple unpacking
first, second, *rest = my_tuple
print("Unpacked elements:")
print("First:", first)
print("Second:", second)
print("Rest:", rest)

# Iterating over a tuple
print("Iterating over the tuple:")
for item in my_tuple:
    print(item)

# Length of a tuple
print("Length of tuple:", len(my_tuple))

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Checking membership in a tuple
print("Check if 'a' is in tuple:", 'a' in my_tuple)

# Count occurrences of an element in a tuple
print("Count of 'a' in tuple:", my_tuple.count('a'))

# Finding the index of an element in a tuple
print("Index of 'b' in tuple:", my_tuple.index('b'))