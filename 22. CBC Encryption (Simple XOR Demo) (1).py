plain = int(input("Plaintext (binary): "), 2)
iv = int(input("IV (binary): "), 2)

cipher = plain ^ iv

print("Cipher =", bin(cipher)[2:])
