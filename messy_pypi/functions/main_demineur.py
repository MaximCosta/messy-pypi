import sys
sys.path.append('../')
from functions.main_terminalGetKey import getKey, getBytesKey
from functions.main_terminalFunctions import DrawChar, Clear, TerminalSize, MessageTropPetitPage

def demineur():
    GameOpen = True
    Plateau = []
    size = 10
    x,y = size//2, size//2
    
    while GameOpen:
        SizeTropPetit = MessageTropPetitPage(10)
        if not SizeTropPetit:
            key = getKey(debug=True)
            Clear()
            DrawChar(140,30, "X")
            DrawChar((TerminalSize("Y")//2), 10, "Y")




"""

TODO:

"""