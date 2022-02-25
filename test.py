import secret
import dota2
import bot_functions
from steam.client import SteamClient
from dota2.client import Dota2Client
from dota2.enums import DOTAChatChannelType_t

client = SteamClient()
dota = Dota2Client(client)


@dota.on('ready')
def create_practice_lobby():
    dota.create_practice_lobby(password="", options={
        'allow_cheats': False,
        'visibility': 0,  # 0 -> Public, 1 -> Friends, 2 -> Unlisted
        'server_region': 2,  # 1-> US West, 2 -> US East
        'game_mode': 2,  # 2-> CAPTAINS MODE, 1-> ALL PICK
        'game_name': "Testing123Testing123",
        'fill_with_bots': False,
        'dota_tv_delay': 3,
        'allow_spectating': True
    })
    print("created Lobby")
    dota.invite_to_lobby(76561198050409028)


@ dota.on('message')
def on_message(message):
    print(message)


print("Logging in.....")
client.login("TheSmallNut", secret.BOTPASSWORD)
print("Logged in")
client.run_forever()
