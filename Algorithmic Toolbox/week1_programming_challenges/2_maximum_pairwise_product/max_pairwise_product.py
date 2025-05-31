def max_pairwise_product(numbers):

    n = len(numbers) #lenth of the list
    max_product = 0 #keep track of the maximum product found so far

    # double loop to find maximum product
    for first in range(n): # goes through each number using index first
        for second in range(first + 1, n): # goes through all the numbers after first (pairs are not repeated and no number is multiplied by itself)
    
    # max updates max_product to be the highest product so far
            max_product = max(max_product,
                numbers[first] * numbers[second])  # computes the product of 2 different numbers

    return max_product


if __name__ == '__main__':
    # read the first line of the input, i.e. the counting number of the next line.

    # If we comment out this line, then only one line of input is needed
    _ = int(input()) # read an integer (but it's not used)

    # get real number from the second line, use map(int, ...) to transfer from string into integer
    input_numbers = list(map(int, input().split())) # read numbers and convert to a list of integers
    print(max_pairwise_product(input_numbers)) # print the result
