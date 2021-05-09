class GameMakerTerminal:
    def __init__(self, mapconfig, fileconfig):
        self.fileconfig = fileconfig
        self.mapconfig = mapconfig
        self.chunksize = (10, 10)
        self.mapsize = (10, 10)

    def TailleMinimaleAtteinte(self):
        print("TailleMinimaleAtteinte")
