import requests

url = 'https://todo.aburifat.com/sa/new/'
url2 = 'http://127.0.0.1:8000/sa/new/'
myobj = {
    'uid': '105',
    'sentance': 'Because I\'m Happy!'
}


x = requests.post(url, json = myobj)

print(x.text)