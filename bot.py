import secret
import dota2
import bot_functions
from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.enums import DOTAChatChannelType_t

client = SteamClient()
dota = Dota2Client(client)


@client.on('logged_on')
def start_dota():
    dota.launch()


@dota.on('ready')
def create_practice_lobby():
    bot_functions.create_lobby(dota, "Testing123", "Password")
    dota.invite_to_lobby(76561198050409028)
    #muffin
    #dota.invite_to_lobby(76561198104057566)
    # dota.invite_to_lobby(76561198048107269)
    #dota.join_practice_lobby_broadcast_channel(channel=1)

@dota.on('message')
def on_message(message):
    print(message)

@dota.on('lobby_new')
def on_lobby_join(lobby):
    # Leave player slot
    print(f"Joined lobby: {lobby.lobby_id}")
    dota.join_practice_lobby_team(slot=1)


@dota.on('lobby_changed')
def lobby_change(lobby):
    print("lobby Changed")

print("Logging in.....")
client.login("TheSmallNut", secret.BOTPASSWORD)
print("Logged in")
client.run_forever()
