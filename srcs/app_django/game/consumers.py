import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

# Now we can safely import and use Django models and other components
import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .game_manager import game_manager

# Wrap the synchronous Django ORM calls with database_sync_to_async

@database_sync_to_async
def get_session(session_key):
    return Session.objects.get(session_key=session_key)

@database_sync_to_async
def get_user(uid):
    return get_user_model().objects.get(pk=uid)

# Function to get the user object from the session key
async def get_user_from_session_key(session_key):
    try:
        session = await get_session(session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = await get_user(uid)
        return user
    except ObjectDoesNotExist:
        return None

class PongConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = None  # Initialize self.game to None
        self.game_id = None  # Initialize self.game_id to None
        self.user = None  # Initialize self.player to None
        self.is_added_to_group = False  # Initialize self.player to None

    async def connect(self):
        
        # Authenticate the user
        cookies_header = next((value for (key, value) in self.scope['headers'] if key == b'cookie'), None)
        user = None  # Initialize user as None
        if cookies_header:
            cookies = dict(cookie.split(b"=") for cookie in cookies_header.split(b"; "))
            session_key = cookies.get(b'sessionid')
            if session_key:
                session_key = session_key.decode('utf-8')  # Ensure session_key is a string
                user = await get_user_from_session_key(session_key)
                print(user)
            else:
                print("Session key not found in cookies")
        else:
            print("No cookies found")

        # If user is not found, reject the connection
        if not user:
            print("Authentication failed. Closing connection.")
            await self.close()
            return  # Stop further execution
        
        # Extract the game_id 
        game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_id = game_id
        print(f"Connecting to game {self.game_id}")
        self.game = game_manager.get_game(game_id)
        self.user = user

        if not self.game:
            self.game = game_manager.create_game(game_id)
        self.game.add_player(self, user)
        await self.channel_layer.group_add(self.game_id, self.channel_name)
        self.is_added_to_group = True
        await self.accept()


    async def disconnect(self, close_code):
        if self.game:
            self.game.remove_player(self)
        # if not self.game.players:
        #     game_manager.remove_game(self.game_id)
        if self.is_added_to_group:
            await self.channel_layer.group_discard(self.game_id, self.channel_name);

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data_json)
        # print(text_data)
        action = text_data_json['action']
        if action == 'move_paddle' :
            player = text_data_json['player']
            direction = text_data_json['direction']
            game_manager.handle_paddle_move(self.game_id, player, direction)
        else :
            self.send(text_data=json.dumps({
                'error': 'Key "message" not found in WebSocket'
            }))

    async def game_update(self, event):
        message = event['message']
        # Assuming event['timestamp'] is a UNIX timestamp
        
        print(f"Received message: {message} at time : {datetime.datetime.now().time()}")
        await self.send(text_data=json.dumps({'game_state': message}))

    async def send_game_state_directly(self, state):
        # print ("state : ", state)
        # print(f"Sending state {state} at time : {datetime.datetime.now().time()}")
        try :
            await self.send(text_data=json.dumps({'game_state': state}))
        except Exception as e :
            print(f"Error while sending game state : {e}")

    async def game_over(self, event):
        message = event['message']
        print("Game n° %s is over" % self.game_id)
        print("Winner : % s" % message)
        await self.send(text_data=json.dumps({'game_over': message}))
