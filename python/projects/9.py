def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Example usage
side1 = 5
side2 = 6
side3 = 7
area = calculate_area(side1, side2, side3)
print("The area of the triangle with sides", side1, ",", side2, ", and", side3, "is:", area)
