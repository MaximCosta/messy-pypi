"""
Recuperer la liste de toutes les class et fonction
recuperer namfunction.__doc__

"""
import os
import re


def list_files(folder: str) -> int:
    """
    Info: You can set "../../Here"
    Info: C'est le fichier a partir du dossier de ce fichier
    """
    l=[]
    for root, directories, files in os.walk(folder, topdown=False):
        for name in files:
            if re.search("[A-Za-z_]\.py", name):
                l.append(os.path.join(root, name))
    return l

