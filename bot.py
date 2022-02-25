import secret
#import dota2
import bot_functions
from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.enums import DOTAChatChannelType_t

client = SteamClient()
dota = Dota2Client(client)


@client.on('logged_on')
def start_dota():
    dota.launch()


# https://github.com/ziadoma/dota_hoster/blob/c35b553ec8232b374a0493f199caec3613fa30fd/main.py
# https://github.com/ValvePython/dota2/blob/6cb1008f3070e008e9bed9521fad8d1438123aa1/protobufs/dota_gcmessages_client_chat.proto#L86-L122


def inviteToLobby(listOfPlayers):
    for player in listOfPlayers:
        dota.invite_to_lobby(player)


@dota.on('ready')
def create_practice_lobby():
    bot_functions.create_lobby(dota, "Testing123", "Password")
    dota.invite_to_lobby(76561198050409028)
    # muffin
    # dota.invite_to_lobby(76561198104057566)
    # dota.invite_to_lobby(76561198048107269)
    # dota.join_practice_lobby_broadcast_channel(channel=1)


@dota.on('message')
def on_message(message):
    print(message)


@dota.on('lobby_new')
def on_lobby_join(lobby):
    print(f"Joined lobby: {lobby.lobby_id}")
    dota.join_practice_lobby_team(slot=1)


@dota.on('lobby_changed')
def lobby_change(lobby):
    print("lobby Changed")


print("Logging in.....")
client.login("TheSmallNut", secret.BOTPASSWORD)
print("Logged in")
client.run_forever()
