import requests
url = "https://v6.exchangerate-api.com/v6/285dfe149039c038fec336df/latest/USD"
response = requests.get(url)    
response.json()
#----------------------------------------------------------------------------------