import requests

url = 'https://bbc.com/news/world/'

response = requests.get(url)
print(response.text)
