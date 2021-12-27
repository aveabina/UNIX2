import requests
print('>User creation')
response = requests.put(
    'httplocalhost7070userbina',
    {'password' 'bn2809'})
print(response.json())

print('>Adding user with same password')
response = requests.put(
    'httplocalhost7070userlili',
    {'password' 'bn2809'})
print(response.json())

print('>Adding user with existing name')
response = requests.put(
    'httplocalhost7070userbina',
    {'password' 'bn2usr'})
print(response.json())

print('>Get user info')
response = requests.get('httplocalhost7070userbina')
print(response.json())

print('>Delete user')
response = requests.delete('httplocalhost7070userlili')
print(response.text)

print('>Get user info of non-existent')
response = requests.get('httplocalhost7070userlili')
print(response.json())
