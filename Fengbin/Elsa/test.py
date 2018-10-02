import requests

url = 'http://127.0.0.1:8080/elsa/allcloth/'
data = {'cloth_type': 3}
res = requests.get(url=url, params=data)
print(res.url)
print(res.status_code)
