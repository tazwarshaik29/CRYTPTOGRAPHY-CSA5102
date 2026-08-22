text = input("Enter text: ")

cipher = text[::-1]

print("Encrypted:", cipher)

plain = cipher[::-1]

print("Decrypted:", plain)
