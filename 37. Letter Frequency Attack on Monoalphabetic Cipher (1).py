from collections import Counter

cipher = input("Enter ciphertext: ").upper()

count = Counter(cipher)

print("Letter Frequencies:")
for letter, freq in count.items():
    if letter.isalpha():
        print(letter, ":", freq)
