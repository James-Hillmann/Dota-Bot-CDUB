import classTest
from steam.client import SteamClient
from dota2.client import Dota2Client
import secret

client = SteamClient()
dota = Dota2Client(client)


@client.on('logged_on')
def start_dota():
    dota.launch()


bot = classTest.Bot(client, "TheSmallNut", secret.BOTPASSWORD)
bot.create1v1Lobby()
