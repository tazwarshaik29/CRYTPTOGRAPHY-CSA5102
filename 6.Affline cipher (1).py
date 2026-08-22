# Affine Cipher Frequency Analysis

cipher = input("Enter the ciphertext: ")

freq = {}

for ch in cipher:
    if ch.isalpha():
        ch = ch.upper()
        freq[ch] = freq.get(ch, 0) + 1

print("\nLetter Frequencies:")
for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(k, ":", v)

print("\nMost frequent letter is assumed to be 'E'")
print("Second most frequent letter is assumed to be 'T'")
print("Given:")
print("B -> E")
print("U -> T")
print("Further affine key calculations are done manually.")
