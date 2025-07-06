# least common multiple
def lcm(a, b):
    # loop through numbers from 1 to a * b
    # a*b is the maximum possible LCM
    for l in range(1, a * b + 1):
        # check if l is divisable by both a and b
        if l % a == 0 and l % b == 0:
        # if so, this is the least common multiple
            return l

# this line should never be reached for positive integers
    assert False

if __name__ == '__main__':
    # read two interger from input
    a, b = map(int, input().split())
    print(lcm(a, b))