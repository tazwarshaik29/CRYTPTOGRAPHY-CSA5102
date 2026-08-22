from math import gcd

n = int(input("Enter n: "))
m = int(input("Enter plaintext block: "))

g = gcd(n, m)

if g > 1:
    print("Common factor found:", g)
else:
    print("No common factor.")
