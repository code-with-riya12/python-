def power(x, n):
    """Calculate x raised to the power of n."""
    result = 1
    for _ in range(n):
        result *= x
    return result


x = 2
n = 3
print(f"{x} raised to the power of {n} is:", power(x, n))  
