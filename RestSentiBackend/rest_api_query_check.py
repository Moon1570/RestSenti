import requests

url = 'http://127.0.0.1:8000/sa/new/'
url2 = 'http://127.0.0.1:8000/sa/records/105'
myobj = {
    'uid': '105',
    'sentance': 'Why you are?'
}

myobj2 = {
    'uid': [
        '101'
    ],
    'sentance': [
        'I\'m happy.'
    ]
}

x = requests.post(url, json = myobj)
#y = requests.get(url2)

print(x.text)