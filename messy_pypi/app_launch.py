from main_demineur import demineur
from main_terminalFunctions import clear
from main_countlignes import count_number_of_lines_in_file, count_number_of_lines_in_folder
import os

def launch():
    print("---")
    print("1: demineur terminal")
    print("2: conter le nombre de lignes")
    print("---")
    menu = input("Menu: ")
    # TODO match
    if menu == "1":
        clear()
        demineur()
    if menu == "2":
        print("---")
        print("1: file")
        print("2: folder")
        print("---")
        menu = input("Menu : ")
        if menu == "1":
            print(count_number_of_lines_in_file(input("Nom de fichier: ")))
        if menu == "2":
            print("---")
            print("1: match")
            print("2: all match at racine")
            print("---")
            menu = input("Menu : ")
            if menu == "1":
                count_number_of_lines_in_folder(input("folder"), input("match"))
            elif menu == "2":
                print("DOSSIER "+ str(os.getcwd())+"/../")
                print("All Ext\t", count_number_of_lines_in_folder("../", "(.py$|.md$|.png$|.txt$|LICENCE|.json$)"),
                      "\t Pour être plus précis: (.py$|.md$|.png$|.txt$|LICENCE|.json$)")
                print("py$ md$\t", count_number_of_lines_in_folder("../", "(.py$|.md$)"))
                print("py$\t", count_number_of_lines_in_folder("../", ".py$"))


launch()
