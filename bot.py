from steam.client import SteamClient
from dota2.client import Dota2Client

client = SteamClient()
dota = Dota2Client(client)

@client.on('logged_on')
def start_dota():
    dota.launch()

@dota.on('ready')

def create_practice_lobby():
    dota.leave_practice_lobby()
    dota.create_practice_lobby(password="h", options=None)
    print("practice Lobby Made")
    dota.join_practice_lobby_broadcast_channel(channel=1)
    dota.invite_to_lobby(76561198050409028)
    dota.invite_to_lobby(76561198048107269)

client.cli_login()
client.run_forever()