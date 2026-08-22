cipher = input("Enter ciphertext: ").upper()

print("\nPossible Plaintexts:\n")

for key in range(26):
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            p = (ord(ch) - 65 - key) % 26
            plain += chr(p + 65)
        else:
            plain += ch
    print("Key", key, ":", plain)
