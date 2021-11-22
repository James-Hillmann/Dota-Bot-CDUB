

def create_lobby(dota, name, password):
    dota.abandon_current_game()
    dota.sleep(1)
    dota.leave_practice_lobby()
    dota.sleep(1)
    dota.create_tournament_lobby(password=password, tournament_game_id=None, tournament_id=0, options={
        'allow_cheats': False,
        'visibility': 0,  # 0 -> Public, 1 -> Friends, 2 -> Unlisted
        'server_region': 2,  # 1-> US West, 2 -> US East
        'game_mode': 2,  # 2-> CAPTAINS MODE, 1-> ALL PICK
        'game_name': name,
        'fill_with_bots': False,
        'dota_tv_delay': 3,
        'allow_spectating': True
    })
    dota.sleep(1)
    dota.join_practice_lobby_team()
    dota.sleep(1)
    dota.channels.join_lobby_channel()
    dota.sleep(1)


if __name__ == "__main__":
    print("RUN IT IN MAIN YOU IDIOT")
