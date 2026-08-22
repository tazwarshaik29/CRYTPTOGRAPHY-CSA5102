import hashlib

message = input("Enter message: ")

private_key = 5
public_key = 25

# Create signature
hash_value = int(
    hashlib.sha256(message.encode()).hexdigest(),
    16
)

signature = hash_value * private_key

print("Message:", message)
print("Signature:", signature)

# Verify
if signature % private_key == 0:
    print("Signature Verified")
else:
    print("Signature Verification Failed")
