import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

uname = input("Enter your DNA username: ")
password = getpass("Enter your DNA password: ")

BASEURL = "https://sandboxdnac.cisco.com"
authAPI = "/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

dnaAuth = BASEURL + authAPI

response = requests.post(dnaAuth, auth=HTTPBasicAuth(uname, password), headers=headers, data=payload)

tokenJSON = response.json()

while True: 
       try:
        TOKEN = tokenJSON['Token']
        break
       except KeyError:
             print("Login incorrect, please try again")
             quit()
    
             
print("Token generated, the requested token is the following:\n'"+ TOKEN)
