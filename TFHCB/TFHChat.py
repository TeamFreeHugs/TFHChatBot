import requests
from bs4 import BeautifulSoup

from TFHCB import Client


def login(username, password):
    loginreq = requests.post('http://localhost:3000/users/login', data={
        'username': username,
        'password': password,
        'referrer': '/chat/'
    })

    if loginreq.url != 'http://localhost:3000/chat/':
        raise ValueError('Incorrect login!')

    soup = BeautifulSoup(loginreq.text, 'html.parser')
    key = soup.find(id='key')['value']
    return Client.Client(key, username)
