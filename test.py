import requests

u=requests.get('http://192.168.190.1:45678/json')
print(u.text)
print(u.json())
