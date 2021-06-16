if __name__ == "__main__":
    import sys

    sys.path.append('../')
    from main_gamemakerterminal import GameMakerTerminal

    GameMakerTerminal("map.txt","config.txt")