from main_terminalGetKey import getKey, get_key_bytes 
from sys import stdout
from resources.keyboard.keyboard_dico import key, latin, keyboard, keyboard_empty, placement, keyboard_keypos
from main_customElement import List
#VARIABLES

default_keyboard_config = "/home/ay/dotfiles/keyboard/ay"

# FUNCTION 
## MAIN
def keygen():
    #VARIBALES
    ShowHelp = True
    EmptyKeyboard = True
    print("\033[2J")

    #keychoosed = input("Choose Default keyoard: ")

    while True:
        print("\033[2J")
        print("\033[1;1H"+ (lambda EmptyKeyboard: keyboard_empty if EmptyKeyboard else keyboard)(EmptyKeyboard))

        if ShowHelp: printposkey()

        key = getKey(debug=True)
        if key=="h":
            ShowHelp = not ShowHelp
        elif key=="k":
            EmptyKeyboard = not EmptyKeyboard


def config_to_dicoallkey(path_to_config):
    dicoallkey = {}
    with open(path_to_config, "r") as f:
        config = List(f.readlines())
        config.rmAll("\n")
    for i in config:
        j = i.split("{")
        j_keys = j[0].strip().replace("key ", "")
        j_valeur = j[1].split("}")[0].strip()[1:-1].split(",")
        j_valeur = [i.strip() for i in j_valeur]
        dicoallkey[j_keys] = j_valeur
    
    # Affiche Dico
    for i, j in dicoallkey.items():
        print(i, ": ", j)
    # print(dicoallkey)
    

def printposkey():
    # prend keyboard_keypos et le place sur le clavier.
    for key, pos in keyboard_keypos.items():
        ##
        print(f"\033[{str((abs(pos[0]-5))*3+5)};{str(pos[1])}H{key[1:-1]}")

## OTHER
def inputbar(before = ""):
    chaine = ""
    InputOpen = True
    while InputOpen:
        key = getKey(debug = True)
        if key=='\x7f':
            chaine = chaine[:-1]
        elif key=='\x1b\x1b' or key=="\r":
            return chaine
        elif key in "azertyuiopqsdfghjklmwxcvbn AZERTYUIOPQSDFGHJKLMWXCVBN_1234567890":
            chaine+=key
        print(before + chaine)
    

# AVANT PROGRAME / GENERATION DES CONFIGS

def tri_du_dico():
    nDico = {}
    for k, v in key.items():
        nDico[v] = [int(k[2:], 16), k]
    for k, v in sorted(nDico.items(), key=lambda x: x[1][0]):
        print("%s: %s" % (k, v))
    return nDico

def updateconfig():
    with open("resources/keyboard/keyboard_config.txt", "r") as f:
        l = f.readline().split("\t")[:-1] 
    dico = {}
    for i in l:
        k = i.split(" ")
        dico[k[0]] = k[1][1:-1]
        
    with open("resources/keyboard/keyboard_dico.txt", "w") as f:
        f.write("key = "+str(dico))

def showconfig():
    print(key)
    for i, j in key.items():
        print(i, j)


"""
DEFINITION DES VARIABLES:

fichier config:
fichier avec plusiers lignes:
"key <AD01>	{ [         q,          Q,           at,  Greek_OMEGA ]	};"


vaiable dicoallkey:
dicionaire avec elements:
'{"<AE01>" :  "['1', 'exclam', 'onesuperior', 'exclamdown']"}'

placement:


config : 
 Doit être exacement du même type que la default
"""
