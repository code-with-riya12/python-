def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = 17
result = check_even_odd(number)
print(number, "is", result)