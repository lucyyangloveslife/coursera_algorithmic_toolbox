def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    # input() allows users to type a line of input
    # split() split the input string into a list of substring based on spaces
    # map applys int() function to each item in the list
    a, b = map(int, input().split())
    
    print(sum_of_two_digits(a, b))
