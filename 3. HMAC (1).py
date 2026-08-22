import hmac
import hashlib

message = input("Enter message: ")
key = b"secret"

h = hmac.new(key, message.encode(), hashlib.sha256)

print("HMAC:", h.hexdigest())

# Verification
h2 = hmac.new(key, message.encode(), hashlib.sha256)

if hmac.compare_digest(h.hexdigest(), h2.hexdigest()):
    print("Message Verified")
else:
    print("Message Not Verified")
