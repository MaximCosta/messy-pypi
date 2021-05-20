"""
J'ai un peux la flemme de le faire maintenant et pour un octet c'est un peu nul
Si on veux gagner un octet quand c'est un nombre impair on peux faire


Si snb impaire
get dernier char
ajouter 101+chr(dernier char)

pour read:
supprimer reachend
si ord(i) est entre 101 et 110 (Je sais pas si c'est exactement ça)
alors enlever 101 a ord(i) et le chr()iser puis l'ajouter a l
"""
import random


def randomnombre(lennb):
    """
    Entree: lennb: int
    Sortie: str

    Renvoi un nombre de longeur `lennb` 
    """
    snb = ""
    for i in range(lennb):
        snb += str(random.randint(0, 9))
    return snb


def owrite(snb, outfile):
    """
    Entree: snb: str, outfile: str(file name)
    Sortie: None
    """
    l = ""
    for i in range(len(snb) // 2):
        a = snb[i * 2:((i * 2) + 2)]
        if a == "13":
            l += chr(100)
        else:
            l += chr(int(a))
    if len(snb) % 2 == 1:
        l += "e" + chr(int(snb[-1]))
    with open(outfile, "w") as f:  # Write other thing
        f.write(l)

    # Permet d'ecrire le nombre d'entrée
    # with open("b", "w") as f: # write inital int
    #    f.write(snb)


def oread(file, outfile):
    """
    Entree: file, outfile:str(file)
    Sortie: none
    """
    l = ""
    reachend = False
    with open(file, "r") as f:
        a = f.read()
    for i in a:
        if reachend:
            l += str(ord(i))
        elif ord(i) == 100:
            l += "13"
        elif ord(i) == 101:  # e
            reachend = True
        else:
            l += str(ord(i)).zfill(2)
    with open(outfile, "w") as f:
        f.write(l)


snb = randomnombre(1000001)
owrite(snb, "a")
oread("a", "c")
