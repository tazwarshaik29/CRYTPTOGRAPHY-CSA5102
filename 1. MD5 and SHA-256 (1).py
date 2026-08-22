import hashlib

msg = input("Enter message: ")

md5 = hashlib.md5(msg.encode()).hexdigest()
sha = hashlib.sha256(msg.encode()).hexdigest()

print("MD5    :", md5)
print("SHA-256:", sha)
