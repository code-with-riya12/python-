def fibonacci(n):
    """Generate the Fibonacci sequence up to the nth term."""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def nth_fibonacci(n):
    """Return the nth Fibonacci number."""
    fib_sequence = fibonacci(n)
    return fib_sequence[-1]

