# Time complexity of version 1: O(n2)
def max_pairwise_product_v1(numbers):

    n = len(numbers) #lenth of the list
    max_product = 0 #keep track of the maximum product found so far

    # double loop to find maximum product
    for first in range(n): # goes through each number using index first
        for second in range(first + 1, n): # goes through all the numbers after first (pairs are not repeated and no number is multiplied by itself)
    
    # max updates max_product to be the highest product so far
            max_product = max(max_product,
                numbers[first] * numbers[second])  # computes the product of 2 different numbers

    return max_product

# Time complexity of version 1: O(n)
def max_pairwise_product_v2(numbers):
    n =  len(numbers)

    # Find the index of the largest nubmer
    first = 0
    for i in range(1, n):
        if numbers[i] > numbers[first]:
            first= i
    
    # Find the index of the second largest number
    # use sentinel value -1, to label second largest number hasn't been marked
    second = -1
    for i in range(n):
        if i != first:
            if second == -1 or numbers[i] > numbers[second]:
                second = i
    return numbers[first] * numbers[second]


if __name__ == '__main__':
    # read the first line of the input, i.e. the counting number of the next line.

    # If we comment out this line, then only one line of input is needed
    _ = int(input()) # read an integer (but it's not used)

    # get real number from the second line, use map(int, ...) to transfer from string into integer
    input_numbers = list(map(int, input().split())) # read numbers and convert to a list of integers
    print(max_pairwise_product_v2(input_numbers)) # print the result