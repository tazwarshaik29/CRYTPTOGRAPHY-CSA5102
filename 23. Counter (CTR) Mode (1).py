plain = int(input("Plaintext: "), 2)

counter = 0

cipher = plain ^ counter

print("Cipher =", bin(cipher)[2:])
