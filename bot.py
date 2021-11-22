from secret import BOTPASSWORD
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
    print("practice Lobby Made")
    dota.invite_to_lobby(76561198050409028)
    # dota.invite_to_lobby(76561198048107269)
    dota.join_practice_lobby_broadcast_channel(channel=1)


@dota.channels.on(dota2.features.chat.ChannelManager.EVENT_MESSAGE)
def chat_message(channel, msg_obj):
    print("got message")
    text = msg_obj.text
    if channel.type != DOTAChatChannelType_t.DOTAChannelType_Lobby:
        return  # ignore postgame and other chats
    print(text)


print("Logging in.....")
client.login("TheSmallNut", BOTPASSWORD)
print("Logged in")
client.run_forever()
