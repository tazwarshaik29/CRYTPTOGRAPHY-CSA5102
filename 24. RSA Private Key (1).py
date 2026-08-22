from math import gcd

p = 59
q = 61

n = p * q

phi = (p - 1) * (q - 1)

e = 31

for d in range(1, phi):
    if (e * d) % phi == 1:
        break

print("Public Key = ", (e, n))
print("Private Key =", d)
