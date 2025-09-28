import sys

if(len(sys.argv)<3):
    print("wrong input\nusage: python vigenere_decrypt <key> <cypherfile>")
    exit(1)

key=[ord(i)-65 for i in list(sys.argv[1])]

cipher=''
for arg in sys.argv[2:]:
    with open(arg,"r") as file:
        cipher+="".join(file.read().strip().upper().split(" "))

cipher=[ord(i)-65 for i in list(cipher)]

plain=[]

for i in range(len(cipher)):
    x=(cipher[i]-key[i%len(key)])%26
    plain.append(chr(x+65))

print("".join(plain))