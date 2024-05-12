def power(x, n):
    """Calculate x raised to the power of n."""
    result = 1
    count = 0
    while count < n:
        result *= x
        count += 1
    return result


x = 2
n = 3
print(f"{x} raised to the power of {n} is:", power(x, n))  
