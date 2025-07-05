def fibonacci_last_digit(n):
    if n <= 1:
        return n

    # Initialize the first two Fibonacci numbers
    previous = 0 #F(0)
    current  = 1 #F(1)

    # Compute Fibonacci numbers from F(2) to F(n)
    for _ in range(n - 1):
        # Update previous and current values for the next step
        previous, current = current, previous + current

    # Return the last digit
    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))