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

def guilaunch():
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk

    def on_activate(app):
        win = Gtk.ApplicationWindow(application=app)
        btn = Gtk.Button(label="Hello, World!")
        btn.connect('clicked', lambda x: win.close())
        win.add(btn)
        win.show_all()

    app = Gtk.Application(application_id='org.gtk.Example')
    app.connect('activate', on_activate)
    app.run(None)
"""
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
"""
if __name__ == "__main__":
    import sys
    args = sys.argv
    if "--help" in args:
        print("--help: Affiche ceci\n--gui: Affiche une interface graphique avec GTK3")
    elif "--gui" in args:
        guilaunch()
    else:
        launch()

