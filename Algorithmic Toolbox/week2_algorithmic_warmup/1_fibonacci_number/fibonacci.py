'''
initial method-----time complexity O(2^n) exponential time
'''

# def fibonacci_number(n):
#     if n <= 1:
#         return n
#     return fibonacci_number(n - 1) + fibonacci_number(n - 2)

'''
optimized method-----time complexity O(n)
'''

def fibonacci_number(n):
    # If n is 0 or 1, return n directly
    if n <= 1:
        return n
    
    # Create a list F with n+1 elements, initialized to 0
    F = [0] * (n + 1)

    # Set the first two Fibonacci numbers
    F[0] = 0
    F[1] = 1

    # Use a loop to fill in the Fibonacci values from F[2] to F[n]
    for i in range(2, n + 1):
        # Each Fibonacci number is the sum of the two preceding ones
        F[i] = F[i-1] + F[i-2]

    return F[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))