# Messy-Pypi

## Structure
	packaging_tutorial/
		├── LICENSE
		├── pyproject.toml
		├── README.md
		├── setup.cfg
		├── setup.py
		├── messy-pypi/
		│   ├── __init__.py
		│	├── function
		│	│	├── main_projet.py
		│	│	└── main_messy.py
		│	└── class
		│		├── main_projet.py
		│		└── main_messy.py
		└── tests/

## lib

## function

### function.main_terminalGetKey.**getKey**

Entrée: None \
Sortie: String of key

Met en pause le terminal et attend l'appui d'une touche et retourne un string. \
Touche differantes de Windows à Linux/MacOs \
Ne pas print dirrectement la sortie car pour les touches spéciales la chaine est du type `\r` ou `\x1b`. Pour savoir la sortie à obtenir transformez encodez la sortie. Utilisez `function.main_terminalGetKey.getBytesKey`.

Compatible: Windows Linux MacOs

### function.main_terminalGetKey.**getBytesKey**

Entrée : None \
Sortie : Bytes String 

Retourne getKey mais en encoder pour pouvoir le print()

### function.main_terminalFunction.**DrawChar**
Entrée: x, y: int; char: String \
Sotie: None

Affiche `char` au potition (x,y) du terminal

Compatible: terminaux ayant l'option Ansii `\033[...`

## class

## init
// Pour importer `main_projet.py` il faut mettre `from function.main_projet import *` dans le `__init__.py` (* peux être remplacer par le nom de la fonction à importer) 

## colab
Maxio && ArkanYota

## infos
!(Lien tuto)[https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56]
