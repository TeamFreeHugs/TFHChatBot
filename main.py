import os
import getpass

from TFHCB import TFHChat
import chatcommunicate

global username
global password


if 'TFHCBU' not in os.environ:
    username = input('Username: ')
else:
    username = os.environ['TFHCBU']

if 'TFHCBP' not in os.environ:
    password = getpass.getpass()
else:
    password = os.environ['TFHCBP']

client = TFHChat.login(username, password)
print('Logged in')
room = client.get_room(4)
room.on_message(chatcommunicate.callback)
print('Chatbot started.')
while True:
    send = input('>> ')
    room.send_message(send)
