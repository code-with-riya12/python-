def calculate_distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

# Example usage
x1, y1 = 1, 2
x2, y2 = 4, 6
distance = calculate_distance(x1, y1, x2, y2)
print("The distance between the points ({}, {}) and ({}, {}) is: {:.2f}".format(x1, y1, x2, y2, distance))
