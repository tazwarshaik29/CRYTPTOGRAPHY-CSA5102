import random

text = input("Enter plaintext: ").upper()

cipher = ""

for ch in text:
    if ch.isalpha():
        key = random.randint(0, 25)
        c = (ord(ch) - 65 + key) % 26
        cipher += chr(c + 65)

print("Ciphertext:", cipher)
