plain=input("Enter plaintext: ").replace(" ","").lower()

key=[9,0,1,7,23,15,21,14,11,11,2,8,9]

cipher=""

for i in range(len(plain)):
    p=ord(plain[i])-97
    c=(p+key[i])%26
    cipher+=chr(c+97)

print("Ciphertext =",cipher)
