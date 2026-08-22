# Simple Substitution Frequency Analysis

cipher = input("Enter ciphertext: ")

freq = {}

for ch in cipher:
    if ch not in [' ', '\n']:
        freq[ch] = freq.get(ch, 0) + 1

print("\nCharacter Frequency:")

for i, j in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(i, ":", j)

print("\nHints:")
print("Most frequent symbol may represent E")
print("Look for repeated symbols representing EE")
print("Guess THE using common patterns")
print("Complete substitution manually.")
