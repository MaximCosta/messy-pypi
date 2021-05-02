import sys
sys.path.append('../')
from functions.main_terminalGetKey import getKey, getBytesKey
from functions.main_terminalFunctions import DrawChar, Clear, TerminalSize, MessageTropPetitPage
from random import randint

def MessageConfigDemineur():
    mines = int(input("mines : "))
    size = int(size("size : "))
    
def demineur():
    GameOpen = True
    size = 10
    Plateau = []
    for i in range(10):
        Ligne = []
        for j in range(10):
            if randint(1,10) >= 3:
                Ligne += [10]
            else:
                Ligne += [9]
        Plateau += [Ligne]
    NouveauPlateau = []
    for i in range(len(Plateau)):
        Ligne = []
        for j in range(len(Plateau[i])):
            if Plateau[i][j] == 9:
                Ligne += [9]
            else:
                somme = 0
                for k in range(-1, 2):
                    for l in range(-1,2):
                        if not ( k == 0 and l == 0):
                            if 0 <= i+k < 10 and 0 <= j+l < 10:
                                if Plateau[i+k][j+l] == 9:
                                    somme +=1
                if somme == 0:
                    Ligne += [10]
                else:
                    Ligne += [-somme]
        NouveauPlateau += [Ligne]
    del Ligne
    Plateau = NouveauPlateau
    # Plateau = [[0 if randint(1,10) >= 2 else -1 for j in range(size)] for i in range(size)]
    # Cache = [[1 for j in range(size)] for i in range(size)]
    x,y = size//2, size//2
    InGame = False # Si le joueur est dans une partie ou si il est sur le menu d'acceuil

    while GameOpen:
        SizeTropPetit = MessageTropPetitPage(size+2, size+2)
        if not SizeTropPetit:
            key = getKey(debug=True)
            Clear()
            if key == "q" or key == "\x1b[D":
                x = max(0, x-1)
            if key == "d" or key == "\x1b[C":
                x = min(size-1, x+1)
            if key == "z" or key == "\x1b[A":
                y = max(0, y-1)
            if key == "s" or key == "\x1b[B":
                y = min(size-1, y+1)
            if key == "a":
                if Plateau[x][y] == 9:
                    GameOpen = False
                    continue
                if Plateau[x][y] < 0:
                    Plateau[x][y] = -Plateau[x][y]
                if Plateau[x][y] == 10:
                    Plateau[x][y] = 0 
            #print(Plateau)
            for i in range(len(Plateau)):
                print("\n ", end="")
                for j in range(len(Plateau[i])):
                    match Plateau[i][j]:
                        case 0:
                            charItem = " "
                        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
                            charItem = Plateau[i][j]
                        case -1 | -2 | -3 | -4 | -5 | -6 | -7 | -8:
                            charItem = "\033[32m\u2588\033[0m"
                        case 10:
                            charItem = "\u2588"
                        case 9:
                            charItem = "\033[31m\u2588\033[0m"
                        case 12:
                            charItem = "\033[31m☭\033[0m"
                        case _:
                            charItem = "X"
                    DrawChar(((TerminalSize("X")-size)//2)+i,((TerminalSize("Y")-size)//2)+j, charItem)
            DrawChar(((TerminalSize("X")-size)//2)+x,((TerminalSize("Y")-size)//2)+y, "X")
            # DrawChar((TerminalSize("Y")//2), 10, "Y")
            # print(x,y, size)
# ⓪①②③④⑤⑥⑦⑧ ⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾

"""

TODO:

"""