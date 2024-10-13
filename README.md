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

Vous souhaitez modifier le projet ? Vous souhaiter intéger de nouvelles fractales / récupérer les différentes ```class object```, ou bien simplement comprendre le code source de $\textsf {Fractalo} \textsf{\color{#ba1ce6}{Py}}$. Alors ces différentes interfaces sont pour vous !


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

> Pour ajouter une nouvelle fractale, veuillez respecter la mise en page suivante. Dans le fichier `ModuleFractales.py`, ajouter une nouvelle class comme l'exemple ci-dessous.

> [!WARNING]
> Chaque élément turtle pour le corps de votre fractale récursive, doit obligatoirement être précédé de `self.gestionnaire.turtle`

```Python3
class <nomFractale>:
    """ class permettant de dessiner et de gérer globalement la fractale en cours de dessin / en pause"""

    def __init__(self, nombre, longueur, gestionnaire):
        """Méthode d'initialisation de la class, grâce à l'intanciation de la class. 
    
        Input : nombre (int), 
                longueur (int), 
                gestionnaire (class parent), 
        Output : None """
    
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []  # Pile pour sauvegarder l'état de la récursion
    
    def __Dessiner< nom >__(self, n, l):
        """ Méthode privé permettant le dessin de la fractale appelé, 
        ainsi que la sauvegarde de son état d'avancement si pause il y a. 
        
        Input : n (int),
                l (int)
        Ouput : None """
    
        # Sauvegarde de l'état actuel si on met en pause
        if self.gestionnaire.isPaused: # Si boolean True
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading())) # On prend les infos et on les stock
            return  # Arrêt temporaire
        
        # Paramétrage de la tortue
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()
    
        if self.gestionnaire.couleurTrait == "Random": # Si la couleur est aléatoire
            self.gestionnaire.__CouleurRandom__() # On fait appel à la méthode compétente pour changer la couleur
    
        # Partie modulable, pour dessiner en récursif la fractale
        < script récursif de votre fractale >
    
           
    def __ReprendreDessin__(self):
        """Méthode qui reprend le dessin depuis l'état sauvegardé"""
    
        if self.state: # Si boolean True
            # Récupération de l'état sauvegardé
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__Dessiner< nom >__(n, l) # On transmet les valeurs sauvegardés
        else: #Si booelan False
            self.__Dessiner< nom >__(self.nombre, self.longueur) # On lance le dessins simplement
    
    def dessiner(self):
        """Méthode qui permet de reprendre ou non le dessin"""
    
        if not self.gestionnaire.isPaused: # Check simple avant de dessiner si on peut
            self.__ReprendreDessin__()
```

> Après avoir ajouté votre `classFractale`, vous devez configurer l'option d'appel de votre nouvelle class. Pour ce faire, dans le fichier `ModuleFractales.py`, dans la class `MainFractaleGestion`, dans la méthode `Lancer` respecter la disposition suivante et ajouter votre nouvelle `classFractale`

> [!NOTE]
> Le `nomFractaleSimple`, sera le nom qui sera affiché dans le menu déroulant de l'interface utilisateur. Ce sera également le même texte pour l'étape suivante.

```Python3
class MainFractaleGestion(object):
    """ class de MainGestion Fractale qui permet lors de l'appel de la méthode lancer,
    d'éxécuter et de lancer les script adéquats aux demandes de l'utilisateurs  """
    def __init__(self,**args):
        pass

    def Lancer(self, fractaleType):
        match fractaleType:
            case "Sierpinski": 
                self.fractale = FractaleSierpinski(self.profondeur, self.longueurTrait, self)
            case "Koch":
                self.fractale = FractaleKoch(self.profondeur, self.longueurTrait, self)
            case "<nomFractaleSimple>":
                self.fractale = <nomFractale>(self.profondeur, self.longueurTrait, self)
            ...
        self.fractale.dessiner()
```

> Enfin, il faut ajouter le `nomFractaleSimple`, de l'étape précédente dans la variable `fractaleListe` du fichier `settings.py`.

```Python3
fractaleListe = ("Sierpinski", "Koch","<nomFractaleSimple>")
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
