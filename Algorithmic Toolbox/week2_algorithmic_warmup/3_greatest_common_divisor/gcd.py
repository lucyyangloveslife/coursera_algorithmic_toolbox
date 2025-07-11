def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# Euclidean Algorithm: gcd(a, b) == gcd(b, a % b)
def gcd(a, b):
    # while b != 0
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))