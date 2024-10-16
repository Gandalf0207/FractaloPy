<!-- MARKDOWN THEME -->
# $\textsf {Fractalo} \textsf{\color{#ba1ce6}{Py}}$

> [!IMPORTANT]
> Pour toutes informations concernant les droits d'utilisation, veillez vous référer à la [Licence](https://github.com/Gandalf0207/FractaloPy?tab=License-1-ov-file)

> [!WARNING]
> Ce projet a été développé sur la version 3.12.6 de python sur l'OS Windows 11. Veuillez vérifier les compatibilités de versions des logiciels que vous utilisez. De plus, ce projet n'est, en aucun cas, certifié infaillible, il peut donc contenir des bugs... Merci de votre compréhension.

## Présentation du Projet :
Ce projet a été réalisé dans le cadre de l'enseignement NSI (Numérique et Sciences Informatiques) en Terminale. Il s'agit d'une interface graphique (GUI) en Python utilisant le module Turtle pour générer différentses fractales. L'utilisateur peut interagir avec l'interface pour modifier les paramètres de génération des fractales, comme le nombre de niveaux de récursivité, la taille des éléments et bien d'autres !

> Le projet met en avant plusieurs concepts clés :

- **Programmation récursive** : utilisée pour générer les fractales.
- **Programmation orientée objet** : pour structurer le code en différentes classes et rendre le programme plus modulaire / compréhensible par des développeurs externe.
- **Modularité** : le programme est organisé de manière à pouvoir facilement ajouter d'autres types de fractales, de nouvelles fonctionnalités à l'avenir ou encore pour être utilisé en partie par d'autre developpeurs.

<br>

> Le projet met à disposition 5 types de fractales différentes :

- Fractale de **Sierpinski**
- Fractale de **Koch**
- Fractale de **Fibonacci**
- Fractale de **Vicsek**
- Fractale de **Pythagore**

<br>

> Le panel de modification des valeurs :

Ce panel, vous permet de modifier selon vos envis, un grand nombre de paramettres afin de modéliser et d'exprimer vos talents artistique avec la représentation de fractales customisé ;) 
Pour ce faire, nous vous mettons à disposition la possibiliser de modifier : 

- La profondeur de récursivité
- La couleur du dessins (couleur fixe / aléatoire pendant la génération)
- La longueur du trait de dessin
- La couleur de l'arrière plan
- L'orientation du curseur de dessin (360°)
- L'épaisseur du trait de dessin
- Le placement du curseur sur la toile

De plus, vous avez la possibilité d'enregister, si vous le souhaitez une ou plusieurs image(s) de votre travail et de changer le curseur de dessins !


<br></br>

## Intégration développeurs :

Vous souhaitez modifier le projet ? Vous souhaiter intéger de nouvelles fractales / récupérer les différentes ```class object```, ajouter de nouveaux curseurs ou bien simplement comprendre le code source de $\textsf {Fractalo} \textsf{\color{#ba1ce6}{Py}}$. Alors ces différentes interfaces sont pour vous !

### Main.py 
#### class SetupFractale

| Fonctions                                                                                                                           | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| def __init__(self, profondeur, couleurTrait, longueurTrait, couleurBackground, turtle, screen) -> None  :                           | Méthode d'initialisation de la class, grâce à l'intanciation de la class par l'objet1. Cette méthode, permet donc la création de cette meme class et l'instanciation de la class MainFractaleFestion <br></br> Input :<br> - prodondeur (int),  <br>  - couleurTrait (str),  <br> - longeurTrait (int),  <br> - couleurBackgound (str),  <br> - turtle (TurteModule),  <br> - screen (TurtleModule)  <br> Output : None                                                                                                                                                                                                                                                   |
| def ProfondeurAffichage(self, value, textProfondeur):                                                                               | Méthode modifiant l'affichage de la valeur de prodondeur sur l'interface utilisteur et sur les attributs de MainFractaleGestion. <br></br> Input : <br> - value (str), <br> - textPrfondeur (variable tkinter)  <br> Output : None                                                                                                                                                                   |
| def ChoixCouleur(self, cadreVisuelCouleur, bouttonChoixCouleur):                                                                    | Méthode modifiant l'affiche de la valeur couleur sur l'interface utilisteur (code + bg visualisation) et sur les attributs de MainFractaleGestion. (soit unique / soit aléatoire). Ouverture d'une fenetre question (unique / aléatoire). Ouverture d'une fenetre que choix de couleur. <br></br> Input : <br> - cadreVisuelCouleur (element tkinter),  <br> - buttonChoixCouleur (element tkinter) <br> Output : None                                                                                                                                                                                                                                                   |
| def LongueurTraitAffichage(self, value, textlongueurTrait):                                                                         | Méthode modifiant l'affiche de la valeur de longeur du trait sur l'interface utilisteur et sur les attributs de MainFractaleGestion <br></br> Input : <br> - value (str), <br> - textLongueurTrait (variable tkinter) <br> Output : None                                                                                                                                                            |
| def ClearMake(self, cadreVisuelBackground):                                                                                         | Méthode permettant de supprimer tout ce qui se trouve sur le canvas. Avant cela le script demande une confirmation sous forme d'une fenetre avec une question. Et une possibilité de sauvegarder ou non une image du dessin. Après cela, l'interface utilisateur est mise à jour <br></br> Input : <br> - cadreVisuelBackground (element tkinter) <br> Output : None                                |
| def ChoixBackground(self, cadreVisuelBackground):                                                                                   | Méthode permettant de choisir l'arrière plan du canvas. Ouverture d'une fenetr de choix de couleur, Mise à jour de l'interface utilisateur en fonction. <br></br> Input : <br> - cadreVisuelBackground (element tkinter) <br> Output : None                                                                                                                                                    |
| def OrientationAffichage(self, value, textOrientation):                                                                             | Méthode permettant de choisir l'orientation du curseur. <br></br> Input : <br> - textOrientation (element tkinter) <br> Output : None                                                                                                                                                                                                                                                                 |
| def EpaisseurAffichage(self, value, textEpaisseur):                                                                                 | Méthode permettant de modifier l'épaisseur du trait de dessin <br></br> Input : <br> - value (str), <br> - textEpaisseur (element tkinter) <br> Output : None                                                                                                                                                                                                                                     |
| def ActiveCurseurPosition(self):                                                                                                    | Méthode qui active simplement le get du click gauche et qui appel la méthode privé compétente <br></br> Input : None <br> Output : None                                                                                                                                                                                                                                                            |
| def LancerPauseAppel(self, typeFractale = None):                                                                                    | Méthode permettant de lancer ou de mettre en pause en fonction de l'état de la pause et d'agir sur la class MainFractaleGestion <br></br> Input : <br> - typeFractale : (str) None si aucune valeur envoyé <br> Output : None                                                                                                                                                                       |
| def SaveAsPng(self):                                                                                                                | Méthode permettant l'enregistrement du canvas déssiné par l'utilisateur au formet png. Le script prend un screen de la fenetre canvas, le sauvgarde en PostScript et puis le convertit au format png. Il ouvre une fenetre permettant à l"utilisteur de choisir le chemin d'enregistrement de l'image. <br></br> Input : None <br> Output : image.png                                          |

#### class Cursor

| Fonctions                                                                                                                           | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| def __init__(self, turtle, screen) -> None:                                                                                         | Méthode d'initialisation de la class cursor, permettant de changer de curseur. Prend la forme d'une fenetre avec une sélection multiple <br></br>  Input : <br> - turtle (element turtle), <br> - screen (element turtle) <br>  Output : None                                                                                                                                                  |
| OpenWindow(self)                                                                                                                    | Méthode qui permet d'ouvrir la fenetre qui contient tout les boutons de sélection. Cette méthode contient également une vérification pour éviter d'ouvrir plusieur fois la même fenetre. <br></br>  Input : None <br>   Output : None                                                                                                                                                                |
        

#### Fonctions autre 
| Fonctions                                                                                                                           | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| def toggle_pause(typeFractale = None):                                                                                              | Fonction qui permet de mettre à jour l'affichage du bouton pause et d'appeler la méthode compétente <br></br> Input : <br> - typeFractale (str ou None si aucune valeur) <br> Output : None                                                                                                                                                                                                  |
| def LienOuvrir(lien):                                                                                                               | Fonction pour ouvrir un lien dans un navigateur <br></br> Input : <br> None Ouput : None                                |
| def SeparatorAdd():                                                                                                                 | Fonction qui ajoute un séparateur pour épurer l'affichage <br></br> Input : <br> None Ouput : None                      |

<br>

### ModuleFractales.py
#### class MainFractaleGestion
| Fonctions                                                                                                                           | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| def __init__(self, profondeur, couleurTrait, longueurTrait, turtle, screen) -> None:                                                | Méthode permettant d'initialiser les valeurs de la class MainFractaleGestion  <br></br>   Input : <br> - profondeur (int), <br> - couleurTrait (str), <br> - longueurTrait (int), <br> - turtle (turtle element), <br> - screen (turtle element) <br> Output : None                                                                                                                               |
| def ChangerProfondeur(self, profondeur):                                                                                            | Méthode pour mettre à jour la profondeur de génération <br></br>   Input : <br> - profondeur (int) <br> Output : None   |
| def ChangerCouleur(self, newCouleurTrait):                                                                                          | Méthode permettant de metrre à jour la couleur du trait de dessin <br></br>    Intput : <br> - newCouleurTrait (str) <br> Output : None                                                                                                                                                                                                                                                            |
| def ChangerlongueurTrait(self, newlongueurTrait):                                                                                   | Méthode pour changer la longueur du trait de dessin <br></br>   Input : <br> - newlongueurTrait (int) <br>  Output : None                                                                                                                                                                                                                                                                             |
| def Lancer(self, fractaleType):                                                                                                     |  Méthode pour lancer la génération de la bonne fractale et de reprendre si pas terminé <br></br>   Input : <br> -  fractaleType (str) <br>  Output : None                                                                                                                                                                                                                                             |
| def Pause(self):                                                                                                                    | Méthode de mise en pause <br></br>    Input : None <br> Output : None                                                   |

#### class FractaleSierpinskie : Même interface pour les autres class de meme type.
| Fonctions                                                                                                                           | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| def __init__(self, nombre, longueur, gestionnaire):                                                                                 | Méthode d'initialisation de la class, grâce à l'intanciation de la class. <br></br>   Input : <br>  - nombre (int), <br> - longueur (int), <br>  - gestionnaire (class parent), <br>  Output : None                                                                                                                                                                                                 |
| def dessiner(self):                                                                                                                 | Méthode qui permet de reprendre ou non le dessin                                                                        |

<br>

#### Model pour ajouter des fractales : 

> Pour ajouter une nouvelle fractale, veuillez respecter la mise en page suivante. Dans le fichier `ModuleFractales.py`, ajouter une nouvelle class comme l'exemple ci-dessous.

> [!WARNING]
> Chaque élément turtle pour le corps de votre fractale récursive, doit obligatoirement être précédé de `self.gestionnaire.turtle`

```Python3
class <nomFractale>:

    # Méthode obligatoire (non modifiable)
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []

    # Méthode obligatoire (modifiable)
    def __Dessiner< nom >__(self, n, l):

        # Élément non modifiable
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return
        
        # Élément non modifiable
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        # Élément non modifiable
        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.__CouleurRandom__()
    
        # Partie modulable, pour dessiner en récursif la fractale
        # Élément modifiable
        < script récursif de votre fractale >
    
    # Méthode obligatoire (modifiable)  
    def __ReprendreDessin__(self):    
        if self.state:
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__Dessiner< nom >__(n, l) # Modification ici
        else:
            self.__Dessiner< nom >__(self.nombre, self.longueur)

    # Méthode obligatoire (non modifiable)
    def dessiner(self):
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()
```

<br>

> Après avoir ajouté votre `classFractale`, vous devez configurer l'option d'appel de votre nouvelle class. Pour ce faire, dans le fichier `ModuleFractales.py`, dans la class `MainFractaleGestion`, dans la méthode `Lancer` respecter la disposition suivante et ajouter votre nouvelle `classFractale`

> [!NOTE]
> Le `nomFractaleSimple`, sera le nom qui sera affiché dans le menu déroulant de l'interface utilisateur. Ce sera également le même texte pour l'étape suivante.

```Python3
class MainFractaleGestion(object):
    def __init__(self,**args):
        pass

    def Lancer(self, fractaleType):
        match fractaleType:
            case "Sierpinski": 
                self.fractale = FractaleSierpinski(self.profondeur, self.longueurTrait, self)
            case "Koch":
                self.fractale = FractaleKoch(self.profondeur, self.longueurTrait, self)
            case "<nomFractaleSimple>":
                self.fractale = < nomFractale >(self.profondeur, self.longueurTrait, self)
            ...
        self.fractale.dessiner()
```

<br>

> Enfin, il faut ajouter le `nomFractaleSimple`, de l'étape précédente dans la variable `fractaleListe` du fichier `settings.py`.

```Python3
fractaleListe = ("Sierpinski", "Koch","<nomFractaleSimple>")
```

<br>

#### Méthode pour ajouter des curseurs custom : 

> Pour ajouter des curseurs custom, vous devez suivres les étapes suivants.

Placer dans le dossier `Cursor` du projet, votre curseur custom sous ce format : `< nom >.gif`

<br>

> Dans le fichier `settings.py` ajouter le < nom > de votre curseur **à la suite** de la liste :

```Python3
cursorListe = ["sun", "leaf", "unicorn", "< nom >"]
```

> [!TIP]
> Vérifiez la résolution de votre image avant de l'intégrer. De plus, si vous ne voyez pas le bouton de votre curseur apparaître, vérifiez la taille de la fenêtre de sélection (mettre en grand écran).


<br></br>

## Installation : 

Pour récupérer le projet : 

> Dans un terminal, rentrer la commande :
```cmd
git clone https://github.com/Gandalf0207/FractaloPy.git
```

> Dans le dossier du projet, dans un terminal, rentrer la commande :
```cmd
python -m pip install Requirements.txt
```

Après cela, exécuter le fichier `Main.py`

<br>

> [!TIP]
> Assurez-vous d'avoir les droits nécessaires et que Python soit correctement installé au préalable sur votre machine.


<br></br>


#
$\textsf {Fractalo} \textsf{\color{#ba1ce6}{Py}}$ __© Tous droits réservés 2024__

*Made by Vuadelle Cyanne, Berruezo Loan, Luban Théo, Pladeau Quentin with* :heart:
