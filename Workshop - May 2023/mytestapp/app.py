import requests


resp = requests.get('http://localhost:8000/').json()
print(resp)
print(resp['all_shows'])
print(resp['all_shows'][1])
print(resp['all_shows'][1]['name'])