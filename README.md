# Messy_Pypi

## Structure
```
packaging_tutorial/
	├── LICENSE
	├── pyproject.toml
	├── README.md
	├── setup.cfg
	├── setup.py
	├── messy-pypi/
	│   ├── __init__.py
	│	├── functions
	│	│	├── main_projet.py
	│	│	└── main_messy.py
	│	└── classes
	│		├── main_projet.py
	│		└── main_messy.py
	└── tests/
```

## lib

## functions

### functions.main_terminalGetKey.**getKey**

Entrée: debug:bool=False \
Sortie: String of key

Met en pause le terminal et attend l'appui d'une touche et retourne un string. \
Touche differantes de Windows à Linux/MacOs \
Ne pas print dirrectement la sortie car pour les touches spéciales la chaine est du type `\r` ou `\x1b`. Pour savoir la sortie à obtenir transformez encodez la sortie. Utilisez `functions.main_terminalGetKey.getBytesKey`.
Si `debug` est à True le termial fera exit quand la on appuira sur `Ctrl+C` 

Compatible: Windows Linux MacOs

### functions.main_terminalGetKey.**getBytesKey**

Entrée : debug:bool=False \
Sortie : Bytes String 

Retourne getKey mais en encoder pour pouvoir le print()
Si `debug` est à True le termial fera exit quand la on appuira sur `Ctrl+C` 

### functions.main_terminalFunction.**DrawChar**
Entrée: x, y: int; char: String \
Sotie: None

Doit être des int!
Affiche `char` au potition (x,y) du terminal
le point Origine se trouve en haut à gauche et commance par 1 

Compatible: terminaux ayant l'option Ansii `\033[...`

### functions.main_terminalFunction.**countNumberOfLinesInFile**
Entrée: folder: str, match="(.py$|.md$)" : str \
Sotie: int

Renvoie le nombre de lignes dans les fichier qui match avec le regex `match` dans le fichier `folder` de les les dossier enfants et petit-enfants et encore plus petits
Et supprime les lignes vides

### functions.main_terminalFunction.**countNumberOfLinesInFolderWithMatch**
Entrée: file: str
Sortie: int

Renvoie le nombre de lignes dans le fichier `file`
Info: You can set "../../Here"
Info: C'est le fichier a partir du dossier de ce fichier


### functions.main_terminalFunction.**Clear**
TODO


### functions.main_terminalFunction.**TerminalSize**
TODO

### functions.main_terminalFunction.**MessageTropPetitPage**
TODO

## classes

### classes.main_customElement.List
list custom pour python, avec 
	-rm : permet de supprimer le premier element dans la liste correspondant, s'il n'existe pas ne renvoie pas d'erreur
	-rmA : permet de supprimer tout les element dans la liste correspondant, s'il n'existe pas ne renvoie pas d'erreur

## init
// Pour importer `main_projet.py` il faut mettre `from functions.main_projet import *` dans le `__init__.py` (* peux être remplacer par le nom de la fonction à importer) 

## colab
Maxio && ArkanYota

## infos
!(Lien tuto)[https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56]

## TODO

### ArkanYota
- Demineur
- Snake
- printColor
- insert https://github.com/ARKANYOTA/ImageEnPoints
