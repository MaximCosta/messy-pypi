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
Touche different de Windows à Linux/MacOs \
Ne pas print directement la sortie car pour les touches spéciales la chaine est du type `\r` ou `\x1b`. Pour savoir la sortie à obtenir transformez encoder la sortie. Utilisez `functions.main_terminalGetKey.getBytesKey`.
Si `debug` est à True le terminal fera exit quand l’on appuiera sur `Ctrl+C` 

Compatible: Windows Linux macOS

### functions.main_terminalGetKey.**getBytesKey**

Entrée : debug:bool=False \
Sortie : Bytes String 

Retourne getKey mais en encoder pour pouvoir le print()
Si `debug` est à True le terminal fera exit quand l’on appuiera sur `Ctrl+C` 

### functions.main_terminalFunction.**print_char**
Entrée: x, y: int; char: String \
Sotie: None

Doit être des int !
Affiche `char` a la position (x, y) du terminal
le point Origine se trouve en haut à gauche et commence par 1 

Compatible : terminaux ayant l'option ANSI `\033[...`

### functions.main_terminalFunction.**count_number_of_lines_in_file**
Entrée: folder: str, match="(.py$|.md$)" : str \
Sotie: int

Renvoie le nombre de lignes dans le fichier qui match avec le regex `match` dans le fichier `folder` de les le dossier enfant et petit-enfants et encore plus petits
Et supprime les lignes vides

### functions.main_terminalFunction.**count_number_of_lines_in_folder**
Entrée : file: str \
Sortie : int

Renvoie le nombre de lignes dans le fichier `file`
Info : You can set "../../Here"
Info : C'est le fichier a partir du dossier de ce fichier


### functions.main_demineur.**demineur**
Entrée: None \
Sortie: None \
PythonVersion: 3.10 (Match Case) 

Lance un demineur sur le terminal

### functions.main_terminalFunction.**clear**
Entrée: None \
Sortie: None 

clear le terminal avec l'ASSCI `\033[2J\033[1;1H`



### functions.main_terminalFunction.**terminal_size**
Entrée : item : str=None \
Sortie : tuple[int, int] or int \
X: > \
Y: \/ \

Retourne la taille de l'écran sous forme de tuple.
Ou retorune la taille X ou Y si item vaux "X" ou "Y"

### functions.main_terminalFunction.**message_page_trop_petite**
Entrée: sizex, sizey: int
Sortie: bool

Si le terminal est plus petit que la taille indiquée il Affiche Trop petit et rénvoie True sinon False

### functions.main_duplicateFile.**check_for_duplicates**
`check_for_duplicates(paths='./',remove=False)`
paths est le chemin racine pour le scan, si remove = True, les fichiers dupliquer trouver seront supprimé.

### functions.main_messe.**human_delta_time**
`human_delta_time(time:int, curValue:str='seconde', minValue='seconde', minValue='jour', remove: list[str] = []) -> (dict or None)`
permet a partir d'un nombre de le transformé en Année,Mois,Jour,Heure,Minute,Seconde.
`human_delta_time(86461) -> {'jour': 1, 'minute': 1, 'seconde': 1}`

`human_delta_time(30,curValue='jour',remove=['jour']) -> {'heure':720}`

## classes

### classes.main_customElement.List
list custom pour python, avec \
	`- prepend(elt)` : permet d'inserer l'element a l'index zero \
	`- rmAllBeside(elt, index)` : permet de supprimer tout les element après la premiere itération de l'element ou après l'index \
	`- rmAllBehind(elt, index)` : permet de supprimer tout les element avant la premiere itération de l'element ou avant l'index \
	`- rm(elt)` : permet de supprimer le premier element dans la liste correspondant, s'il n'existe pas ne renvoie pas d'erreur \
	`- rmAll(elt)` : permet de supprimer tout les element dans la liste correspondant, s'il n'existe pas ne renvoie pas d'erreur \
	`- rmMAll([elt,...])` : permet de supprimer tout les element dans la liste contenue dans le tableau, s'ils n'existe pas ne renvoie pas d'erreur \
	`- indexExist(index)` : renvoie True si l'index existe sinon False \
	`- replace(start,end)` : remplace la valeur de depart part la nouvelle, sur le premiere element trouvé \
	`- replaceAll(start,end,maxreplace)` : remplace la valeur de depart part le nouveau, opération sur tout le tableau \
	`- find(elt)` : trouve l'index d'un element par sa valeur, retourne l'index \
	`- findAll(elt)` : retourne tout l'index de tout les element correspondent \
	`- clearNotValue()` : supprime toutes les valeurs null : [0,'',None,False, ...] \
	`- clearDuplicate()` : supprimer toutes les doublont \
	`- showDuplicate()` : renvoie les valeurs dupliquer \
	`- countAll()` : renvoie une list de tuple avec le count de chaque element \
	`- toType()` : transforme tout les float et int sous forme de string ex: '1.0' -> 1.0, '1'-> 1  \
	`- include(elt)`: retourne True ou False dépendant si l'element est present ou non \
	`- includes(elts)`: retourne True ou False dépendant si les elements sont present ou non \
	`- copy()`: return copy of list with init new class List \
	`- help`: affiche la doc suivant \
	`- enumerate` : un iterator enumerate -> list(liste.enumerate) => [(index,value),...] \
	`- renumerate` : un iterator enumerate reverse -> list(liste.renumerate) => [(index-1,value-1),...] \
	`- maxv` : retourne la valeur max du tableau \
	`- maxi` : retourne l'index de la valeur max \
	`- maxl` : retourne la valeur avec le len max du tableau \
	`- minv` : retourne la valeur min du tableau \
	`- mini` : retourne l'index de la valeur min \
	`- minl` : retourne la valeur avec le len min du tableau \
	`- length` : renvoie le poid du tableau \


### classes.main_minesweeper
Permet de jouer au démineur avec pygame \
	`Main.start()` : permet de lancer le jeu \

### classes.main_tetris
Permet de jouer a tetris avec pygame \
	`tetris().main_menu()` : permet de lancer le jeu \

## init
// Pour importer `main_projet.py` il faut mettre `from functions.main_projet import *` dans le `__init__.py` (* peux être remplacé par le nom de la fonction à importer) 

## collaboration
Maxio && ArkanYota

## infos
!(Lien tuto)[https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56]

## TODO

### ArkanYota
- Demineur
- Snake
- printColor
- Insert https://github.com/ARKANYOTA/ImageEnPoints
- GameMakerTerminal
- Tri par insertion avec recherche dichotomique
- Recherche dichotomique dans JSON
- Tri un base de donnée de façon dichotomique (potentiellement avec sort()) 
- App launcher for use app functions `app_lanuch.py` ->  Add interface graphique 

### Maxio
- Minesweeper (pygame)
- Tetris (pygame)
- duplicateFile	
- CustomElement
- messy

### Nous 2

- Translate for all. Francais anglais
- Documentation
