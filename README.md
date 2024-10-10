<!-- MARKDOWN THEME -->
# $\textsf {Fractalo} \textsf{\color{#ba1ce6}{Py}}$

> [!IMPORTANT]
> Pour toutes informations concernant les droits d'utilisation, veillez vous référer à la [Licence](https://github.com/Gandalf0207/FractaloPy?tab=License-1-ov-file)


## Présentation du Projet :
Ce projet a été réalisé dans le cadre de l'enseignement NSI (Numérique et Sciences Informatiques) en Terminale. Il s'agit d'une interface graphique (GUI) en Python utilisant le module Turtle pour générer différentses fractales. L'utilisateur peut interagir avec l'interface pour modifier les paramètres de génération des fractales, comme le nombre de niveaux de récursivité, la taille des éléments et bien d'autres !

> Le projet met en avant plusieurs concepts clés :

- **Programmation récursive** : utilisée pour générer les fractales.
- **Programmation orientée objet** : pour structurer le code en différentes classes et rendre le programme plus modulaire / compréhensible par des développeurs externe.
- **Modularité** : le programme est organisé de manière à pouvoir facilement ajouter d'autres types de fractales, de nouvelles fonctionnalités à l'avenir ou encore pour être utilisé en partie par d'autre developpeurs.

<br></br>

> Le projet met à disposition 5 types de fractales différentes :

- Fractale de **Sierpinski**
- Fractale de **Koch**
- Fractale de **Fibonacci**
- Fractale de **Vicsek**
- Fractale de **Pythagore**

<br></br>

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

De plus, vous avez la possibilité d'enregister, si vous le souhaitez une ou plusieurs image(s) de votre travail !

<br></br>
<br></br>

## Intégration développeurs :

Vous souhaitez modifier le projet ? Vous souhaiter inéger de nouvelles fractales / récupérer les différentes ```class object```, ou bien simplement comprendre le code source de $\textsf {Fractalo} \textsf{\color{#ba1ce6}{Py}}$. Alors ces différentes interfaces sont pour vous !


#### Setup

| Fonctions                                                                                                                           | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
|         |         |
|         |         |
|         |         |
|         |         |
|         |         |
|         |         |

.... Autres class.... 


#### Model pour ajouter des fractales : 

> Ajout de chaque fractale en suivant la compo nécéssaire pour chaque fonctionnalités

```Python3
class <nomFractale>:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []

    def dessiner_<nomFractale>(self, n, l):
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return

        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.CouleurRandom()

        # < Corps fractales récursives >
           
    def reprendre_dessin(self):
        if self.state:
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.dessiner_sierpinski(n, l)
        else:
            self.dessiner_<nomFractale>(self.nombre, self.longueur)

    def dessiner(self):
        if not self.gestionnaire.isPaused:
            self.reprendre_dessin()
```

<br></br>
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
<br></br>


#
$\textsf {Fractalo} \textsf{\color{#ba1ce6}{Py}}$ __© Tous droits réservés 2024__

*Made by Vuadelle Cyanne, Berruezo Loan, Luban Théo, Pladeau Quentin with* :heart:
