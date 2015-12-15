import requests
import websocket
import threading
import json


class WSThread(threading.Thread):
    def __init__(self, room):
        super().__init__()
        self.room = room

    def run(self):
        while True:
            rec = self.room.ws.recv()
            event = json.loads(rec)
            if event['eventType'] == 1:
                for listener in self.room.on_message_cbs:
                    listener(event['content'], event['senderName'], self.room, self.room.client)
                pass


class Room:
    def __init__(self, id, client):
        self.id = id
        self.client = client
        self.ws = websocket.create_connection('ws://localhost:4000/rooms/' + str(id) + '?key=' + client.key)
        self.ws_thread = WSThread(self)
        self.ws_thread.start()
        self.on_message_cbs = []

    def send_message(self, content):
        requests.post('http://localhost:3000/chat/rooms/' + str(self.id) + '/messages/add', data={
            'key': self.client.key,
            'text': content
        })

    def on_message(self, callback):
        self.on_message_cbs.append(callback)
