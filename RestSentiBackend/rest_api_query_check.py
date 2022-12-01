import requests

url = 'http://127.0.0.1:8000/sa/new/'
myobj = {
    'uid': '105',
    'sentance': 'While I\'m not happy, I\'m not happy!'
}

x = requests.post(url, json = myobj)

print(x.text)