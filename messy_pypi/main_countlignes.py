import os
import re


def count_number_of_lines_in_file(file: str) -> int:
    """
    Entrée: file: str
    Sortie: int
    
    Compte le nombre de lignes dans un fichier
    """
    with open(file, "r", encoding="latin-1") as f:
        text = f.readlines()
        text = [e for e in text if e.strip() not in {""}]
        return len(text)


def count_number_of_lines_in_folder(folder: str, match: str = "(.py$|.md$)") -> int:
    """
    Info: You can set "../../Here"
    Info: C'est le fichier a partir du dossier de ce fichier
    """
    nombres_lignes = 0
    for root, directories, files in os.walk(folder, topdown=False):
        for name in files:
            if re.search(match, name):
                nombres_lignes += count_number_of_lines_in_file(os.path.join(root, name))
    return nombres_lignes

def count_number_of_lines_in_folder_verbose(folder: str, match: str = "(.py$|.md$)") -> int:
    """
    Info: You can set "../../Here"
    Info: C'est le fichier a partir du dossier de ce fichier
    """
    nombres_lignes = 0
    for root, directories, files in os.walk(folder, topdown=False):
        print("\033[31mroot:\033[0m "+root)
        print("\033[32mdirectories:\033[0m "+ str(directories))
        print("\033[33mfiles:\033[0m "+ str(files))
        for name in files:
            if re.search(match, name):
                print("\033[31m---\033[0m")
                print("\033[34mpath:\033[0m "+str(os.path.join(root, name)))
                print("\033[35mlignes:\033[0m "+str(count_number_of_lines_in_file(os.path.join(root, name))))
                nombres_lignes += count_number_of_lines_in_file(os.path.join(root, name))
        print("\n"+"="*(os.get_terminal_size()[0])+"\n")
    return nombres_lignes

if __name__ == "__main__":
    match = "\.py$|\.md$|\.html$|\.css$|\.txt$|LICENCE$|\.cfg$"
    print("nombre de lignes: "+str(count_number_of_lines_in_folder_verbose(".", match)))
    print("match: "+match)
    print("fichier courant: "+str(os.getcwd()))
