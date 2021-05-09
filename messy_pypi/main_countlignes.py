import os
import re


def countNumberOfLinesInFile(file: str) -> int:
    """
    Entrée: file: str
    Sortie: int
    
    Compte le nombre de lignes dans un fichier
    """
    with open(file, "r", encoding="latin-1") as f:
        text = f.readlines()
        text = [e for e in text if e.strip() not in {""}]
        return len(text)


def countNumberOfLinesInFolderWithMatch(folder: str, match: str = "(.py$|.md$)") -> int:
    """
    Info: You can set "../../Here"
    Info: C'est le fichier a partir du dossier de ce fichier
    """
    nombres_lignes = 0
    for root, directories, files in os.walk(folder, topdown=False):
        for name in files:
            if re.search(match, name):
                nombres_lignes += countNumberOfLinesInFile(os.path.join(root, name))
    return nombres_lignes
