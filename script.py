import requests

r = requests.get("http://kollathat.com")
print(r.status_code)
print(r.ok)
