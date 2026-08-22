matrix = [
['M','F','H','I','K'],
['U','N','O','P','Q'],
['Z','V','W','X','Y'],
['E','L','A','R','G'],
['D','S','T','B','C']
]

print("Playfair Matrix:\n")

for row in matrix:
    print(row)

message = input("\nEnter message: ")

print("\nMessage:")
print(message)

print("\nEncryption requires Playfair rules:")
print("1. Same row -> take next letter")
print("2. Same column -> take below letter")
print("3. Rectangle -> swap columns")
