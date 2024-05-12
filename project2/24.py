def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers less than 10:")
for num in range(2, 10):
    if is_prime(num):
        print(num)
