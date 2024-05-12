import math

# Function to find GCD
def find_gcd(x, y):
    return math.gcd(x, y)

# Example usage
num1 = 36
num2 = 48
gcd = find_gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", gcd)