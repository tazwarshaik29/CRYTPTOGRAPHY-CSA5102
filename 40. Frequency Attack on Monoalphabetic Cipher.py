cipher = input("Enter ciphertext: ").upper()

print("Top 10 Possible Plaintexts:\n")

for i in range(10):
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            p = (ord(ch) - 65 - i) % 26
            plain += chr(p + 65)
        else:
            plain += ch
    print("Guess", i + 1, ":", plain)
