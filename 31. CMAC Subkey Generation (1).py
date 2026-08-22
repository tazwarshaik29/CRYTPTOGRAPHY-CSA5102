block = int(input("Enter block size (64 or 128): "))

if block == 64:
    print("Constant (Rb) = 0x1B")
elif block == 128:
    print("Constant (Rb) = 0x87")
else:
    print("Invalid block size")
