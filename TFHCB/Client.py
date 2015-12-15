import requests

from TFHCB import Room


class Client:
    def __init__(self, key, username):
        self.key = key
        self.username = username

    def get_room(self, id):
        room = requests.get('http://localhost:3000/chat/rooms/' + str(id))
        if room.status_code == 404:
            raise ValueError('No such room!')
        return Room.Room(id, self)
