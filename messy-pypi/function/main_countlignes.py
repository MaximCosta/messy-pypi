import sys
import os

def countNumberOfLinesInFolder(file: str) -> int:
    """
    Entrée: file: str
    Sortie: int
    
    Compte le nombre de lignes dans un fichier
    """
    with open(file, "r") as f:
        return len(f.readlines())

def listeInsideFolder(dirname: str) -> List[str]:
    """
    Info: You can set "../../Here"
    Info: C'est le fichier a partir du dossier de ce fichier
    """
    return os.listdir(folder)