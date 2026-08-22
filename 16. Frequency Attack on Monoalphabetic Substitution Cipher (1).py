from collections import Counter

cipher = input("Enter Ciphertext: ").upper()
top = int(input("Enter number of guesses: "))

freq = Counter(cipher.replace(" ", ""))

print("\nLetter Frequency:")
for letter, count in freq.most_common():
    print(letter, ":", count)

print("\nPossible Plaintexts (Top", top, "):")
for i in range(1, top + 1):
    print(i, ": Possible plaintext guess", i)
