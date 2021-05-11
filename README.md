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
Entrée: file: str \
Sortie: int

Renvoie le nombre de lignes dans le fichier `file`
Info: You can set "../../Here"
Info: C'est le fichier a partir du dossier de ce fichier


### functions.main_demineur.**demineur**
Entrée: None \
Sortie: None \
PythonVersion: 3.10 (Match Case) 

Lance un demineur sur le terminal

### functions.main_terminalFunction.**Clear**
Entrée: None \
Sortie: None 

Clear le terminal avec l'assci `\033[2J\033[1;1H`



### functions.main_terminalFunction.**TerminalSize**
Entrée: item: str=None \
Sortie: tuple[int, int] or int \
X: > \
Y: \/ \

Retourne la taille de l'écran sous forme de tuple.
Ou retorune la taille X ou Y si item vaux "X" ou "Y"

### functions.main_terminalFunction.**MessageTropPetitPage**
Entrée: sizex, sizey: int
Sortie: bool

Si le terminal est plus petit que la taille indiquée il Affiche Trop petit et rénvoie True sinon False

### functions.main_duplicateFile.**check_for_duplicates**
`check_for_duplicates(paths='./',remove=False)`
paths est le chemin racine pour le scan, si remove = True, les fichiers dupliquer trouver seront supprimer.

## classes

### classes.main_customElement.List
list custom pour python, avec \
	`- rm(elt)` : permet de supprimer le premier element dans la liste correspondant, s'il n'existe pas ne renvoie pas d'erreur \
	`- rmAll(elt)` : permet de supprimer tout les element dans la liste correspondant, s'il n'existe pas ne renvoie pas d'erreur \
	`- rmMAll([elt,...])` : permet de supprimer tout les element dans la liste contenu dans le tableau, s'ils n'existe pas ne renvoie pas d'erreur \
	`- indexExist(index)` : renvoie True si l'index existe sinon False \
	`- replace(start,end)` : remplace la valeur de depart part la nouvelle, sur le premiere element trouvé \
	`- replaceAll(start,end,maxreplace)` : remplace la valeur de depart part le nouvelle, opération sur tout le tableau \
	`- find(elt)` : trouve l'index d'un element par sa valeur, retourne l'index \
	`- findAll(elt)` : retourne tout l'index de tout les element corespondant \
	`- clearNotValue()` : supprime toutes les valeurs null : [0,'',None,False, ...] \
	`- clearDuplicate()` : supprimer toutes les doublont \
	`- showDuplicate()` : renvoie les valeurs dupliquer \
	`- countAll()` : renvoie une list de tuple avec avec  \
	`- toType()` : transforme tout les float et int sous forme de string ex: '1.0' -> 1.0, '1'-> 1  \
	`- maxv` : retourne la valeur max du tableau \
	`- maxi` : retourne l'index de la valeur max \
	`- maxl` : retourne la valeur avec le len max du tableau \
	`- minv` : retourne la valeur min du tableau \
	`- mini` : retourne l'index de la valeur min \
	`- minl` : retourne la valeur avec le len min du tableau \
	`- length` : renvoie le poid du tableau \


### classes.main_minesweeper
permet de jouer au démineur avec pygame \
	`Main.start()` : permet de lancer le jeux \

### classes.main_tetris
permet de jouer a tetris avec pygame \
	`tetris().main_menu()` : permet de lancer le jeux \

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
- GameMakerTerminal
- Tri par insertion avec recherche dicotomique
- Recherche dicotomique dans JSON
- Tri un base de donnée de façon dicotomique (potentielelmene avec sort()) 

### Maxio
- Minesweeper (pygame)
- Tetris (pygame)
- duplicateFile	
- CustomElement

### Nous 2:
- Translate for all. Francais anglais
