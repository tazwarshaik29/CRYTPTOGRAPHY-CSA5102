# Affine Caesar Cipher Encryption

text = input("Enter plaintext: ").upper()
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Check if 'a' is valid
if a % 2 == 0 or a == 13:
    print("Invalid value of a. Choose a coprime with 26.")
else:
    cipher = ""
    for ch in text:
        if ch.isalpha():
            p = ord(ch) - 65
            c = (a * p + b) % 26
            cipher += chr(c + 65)
        else:
            cipher += ch
    print("Ciphertext:", cipher)
