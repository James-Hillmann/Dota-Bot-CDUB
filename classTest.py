class Bot():
    def __init__(self, client, username, password):
        self.client = client
        self.login(username, password)

    def login(self, username, password):
        print("Logging in.....")
        self.client.login(username, password)
        print("Logged in")
        self.client.run_forever()

    def printSomething(self, something):
        print(something)

    def create1v1Lobby(self):
        print("1v1 Lobby Created")
