import string

keyword = input("Enter keyword: ").upper()

alphabet = string.ascii_uppercase

cipher = ""

for ch in keyword:
    if ch not in cipher:
        cipher += ch

for ch in alphabet:
    if ch not in cipher:
        cipher += ch

print("\nPlain Alphabet :")
print(" ".join(alphabet))

print("\nCipher Alphabet :")
print(" ".join(cipher))
