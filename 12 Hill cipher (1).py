import numpy as np

key = np.array([[9,4],
                [5,7]])

plaintext = input("Enter plaintext: ").replace(" ","").lower()

if len(plaintext)%2!=0:
    plaintext+='x'

print("Ciphertext:",end=" ")

for i in range(0,len(plaintext),2):
    p=np.array([[ord(plaintext[i])-97],
                [ord(plaintext[i+1])-97]])

    c=np.dot(key,p)%26

    print(chr(c[0][0]+97)+chr(c[1][0]+97),end="")
