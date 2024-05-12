# File: my_module.py
def calculate_rectangle_area(length, width):
    return length * width
# File: main.py
import my_module
import math

# Length and width of the rectangle
length = 5
width = 3

# Calculate area of rectangle using user-defined module
rectangle_area = my_module.calculate_rectangle_area(length, width)
print("Area of rectangle:", rectangle_area)

# Calculate square root of area using built-in module
square_root_area = math.sqrt(rectangle_area)
print("Square root of area:", square_root_area)
