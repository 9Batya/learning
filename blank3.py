import requests

url = 'https://api.telegram.org/bot6858510351:AAGOhAl0zFaAvFE270kV4tJR9MYNz4JpvQw/getMe'
req = requests.request('GET',url)
print(req.json())
