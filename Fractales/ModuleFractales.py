# -------------------------------------------------------------------------------------- #
# ----------------------- FractaloPy © Tous droits réservés 2024 ----------------------- #
# -------------------------------------------------------------------------------------- #

# https://github.com/Gandalf0207/FractaloPy


# Importation du fichier settings
from settings import *


class MainFractaleGestion(object):
    """ class de MainGestion Fractale qui permet lors de l'appel de la méthode lancer,
    d'éxécuter et de lancer les script adéquats aux demandes de l'utilisateurs  """

    def __init__(self, profondeur, couleurTrait, longueurTrait, turtle, screen) -> None:
        """ Méthode permettant d'initialiser les valeurs de la class MainFractaleGestion 
        
        Input : profondeur (int),
                couleurTrait (str),
                longueurTrait (int),
                turtle (turtle element),
                screen (turtle element)
        Output : None"""

        self.profondeur = profondeur # nombre de récursivité
        self.couleurTrait = couleurTrait # couleur du trait
        self.longueurTrait = longueurTrait # longueur du trait
        self.isPaused = False # boolean 
        self.turtle = turtle # element turtle
        self.screen = screen # element turtle 
        self.isFinished = True # check element boolean pour reprendre
        self.fractale = None # type de fractale 
        self.fractaleType = None # check pour relancer ou non une nouvelle fractale



    def __CouleurRandom__(self):
        """ Méthode privé permettant de changer la couleur du trait aléatoirement
        
        Input : None
        Output : None """

        # Set de la nouvelle couleur aléatoire sur le stylo de la tortue
        self.turtle.pencolor('#{:06x}'.format(randint(0, 0xFFFFFF)))



    def ChangerProfondeur(self, profondeur):
        """ Méthode pour mettre à jour la profondeur de génération

        Input : profondeur (int)
        Output : None """

        self.profondeur = profondeur # Mise à jour au sein de la class



    def ChangerCouleur(self, newCouleurTrait):
        """ Méthode permettant de metrre à jour la couleur du trait de dessin
         
        Intput : newCouleurTrait (str)
        Output : None """

        self.couleurTrait = newCouleurTrait # Mise à jour au sein de la class
        if newCouleurTrait != "Random": # Si c'est pas en random, alors on met directement la couleur sur le stylo
            self.turtle.pencolor(self.couleurTrait) # Mise à jour au sein de la class



    def ChangerlongueurTrait(self, newlongueurTrait):
        """ Méthode pour changer la longueur du trait de dessin 
        
        Input : newlongueurTrait (int)
        Output : None """

        self.longueurTrait = newlongueurTrait # Mise à jour au sein de la class



    def Lancer(self, fractaleType):
        """ Méthode pour lancer la génération de la bonne fractale et de reprendre si pas terminé
          
        Input : fractaleType (str)
        Output : None  """


        self.isPaused = False # On enlève la pause

        # Sélectionne et dessine la fractale en fonction du type
        if self.isFinished == True or fractaleType != self.fractaleType: # Si erminé et nouvelle fractale
            self.fractaleType = fractaleType #  On actualise la nouvelle fractale
            self.isFinished = False # On indique de ce n'est pas terminé
            match fractaleType: # on check et on initialise le bon object de fractale
                case "Sierpinski": 
                    self.fractale = FractaleSierpinski(self.profondeur, self.longueurTrait, self) # NE PAS OUBLIER le self de fin pour lier les deux elements
                case "Koch":
                    self.fractale = FractaleKoch(self.profondeur, self.longueurTrait, self)
                case "Vicsek":
                    self.fractale = FractaleVicsek(self.profondeur, self.longueurTrait, self)
                case "Fibonacci":
                    self.fractale = FractaleFibonacci(self.profondeur, self.longueurTrait, self)
                case "Pythagore":
                    self.fractale = FractalesPythagore(self.profondeur, self.longueurTrait, self)
            self.fractale.dessiner() # On appel la méthode pour dessiner le tout
            
        elif self.isFinished == False: # Si ce n'est pas terminé
            self.fractale.dessiner() # On termone de dessiner
            self.isFinished = True # On indique que le dessin est terminé



    def Pause(self):
        """ Méthode de mise en pause
        
        Input : None
        Output : None  """


        self.isPaused = True # Mise en pause (True du boolean)


# ------------------------------------------------------------------------------------#
# ------------------------------ class Fractales -------------------------------------#
# ------------------------------------------------------------------------------------#

# NOTE : Seule la class de la Fractale de Sierpinski sera commentée, car chaque class reprend la meme structure et fonctionne pareillement. 

class FractaleSierpinski:
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

    def __DessinerSierpinski__(self, n, l):
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
        if n == 0:
            for i in range(3):
                self.gestionnaire.turtle.forward(l)
                self.gestionnaire.turtle.left(120)
        else:
            self.__DessinerSierpinski__(n - 1, l / 2)
            self.gestionnaire.turtle.forward(l / 2)
            self.__DessinerSierpinski__(n - 1, l / 2)
            self.gestionnaire.turtle.backward(l / 2)
            self.gestionnaire.turtle.left(60)
            self.gestionnaire.turtle.forward(l / 2)
            self.gestionnaire.turtle.right(60)
            self.__DessinerSierpinski__(n - 1, l / 2)
            self.gestionnaire.turtle.left(60)
            self.gestionnaire.turtle.backward(l / 2)
            self.gestionnaire.turtle.right(60)

           
    def __ReprendreDessin__(self):
        """Méthode qui reprend le dessin depuis l'état sauvegardé"""

        if self.state: # Si boolean True
            # Récupération de l'état sauvegardé
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerSierpinski__(n, l) # On transmet les valeurs sauvegardés
        else: #Si booelan False
            self.__DessinerSierpinski__(self.nombre, self.longueur) # On lance le dessins simplement

    def dessiner(self):
        """Méthode qui permet de reprendre ou non le dessin"""

        if not self.gestionnaire.isPaused: # Check simple avant de dessiner si on peut
            self.__ReprendreDessin__()


class FractaleKoch:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []

    def __DessinerKoch__(self, n, l):        
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return

        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()
        
        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.__CouleurRandom__()

        if n == 0:
            self.gestionnaire.turtle.forward(l)
        else:
            self.__DessinerKoch__(n-1, l/3)
            self.gestionnaire.turtle.left(60)
            self.__DessinerKoch__(n-1, l/3)
            self.gestionnaire.turtle.left(-120)
            self.__DessinerKoch__(n-1, l/3)
            self.gestionnaire.turtle.left(60)
            self.__DessinerKoch__(n-1, l/3)

    def __ReprendreDessin__(self):
        if self.state:
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerKoch__(n, l)
        else:
            self.__DessinerKoch__(self.nombre, self.longueur)
    
    def dessiner(self):
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()


class FractaleVicsek:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = [] 
        
    def __Carre__(self, l):
        self.gestionnaire.turtle.pendown()
        for i in range(4):
            self.gestionnaire.turtle.forward(l)
            self.gestionnaire.turtle.left(90)

    def __DessinerVicsek__(self, n, l):
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return 

        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.__CouleurRandom__()

        x = self.gestionnaire.turtle.xcor()
        y = self.gestionnaire.turtle.ycor()
        if n == 0:
            self.__Carre__(l)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x+l*2,y)
            self.__Carre__(l)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x+l,y+l)
            self.__Carre__(l)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x,y+l*2)
            self.__Carre__(l)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x+l*2,y+l*2)
            self.__Carre__(l)
            self.gestionnaire.turtle.penup()
        elif n > 0:
            self.__DessinerVicsek__(n-1,l/3)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x+l*2,y)
            self.__DessinerVicsek__(n-1,l/3)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x+l,y+l)
            self.__DessinerVicsek__(n-1,l/3)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x,y+l*2)
            self.__DessinerVicsek__(n-1,l/3)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.goto(x+l*2,y+l*2)
            self.__DessinerVicsek__(n-1,l/3)
            self.gestionnaire.turtle.penup()

    def __ReprendreDessin__(self):
        if self.state:
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerVicsek__(n, l)
        else:
            self.__DessinerVicsek__(self.nombre, self.longueur)

    def dessiner(self):
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()


class FractaleFibonacci:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre *5
        self.longueur = longueur // 100
        self.gestionnaire = gestionnaire
        self.state = []  

    def __liste__(self, n):
        if n == 1:
            return "B"
        elif n == 2:
            return self.__liste__(n - 1) + "A"
        elif n > 2:
            return self.__liste__(n - 1) + self.__liste__(n - 2)

    def __DessinerFibonacci__(self, n, l):

        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if not self.gestionnaire.isPaused:
            self.mot = self.__liste__(n)
            self.mot = list(self.mot)
            
            for i in range(len(self.mot)):

                if self.gestionnaire.couleurTrait == "Random":
                    self.gestionnaire.__CouleurRandom__()
                self.gestionnaire.screen.update()

                if not self.gestionnaire.isPaused:
                    if self.mot[i] == "A":
                        self.gestionnaire.turtle.pendown()
                        self.gestionnaire.turtle.forward(l)
                    elif self.mot[i] == "B":
                        self.gestionnaire.turtle.pendown()
                        if (i + 1) % 2 == 0:
                            self.gestionnaire.turtle.right(90)
                        elif (i + 1) % 2 != 0:
                            self.gestionnaire.turtle.left(90)
                        self.gestionnaire.turtle.forward(l)
                else:
                    self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))


    def __ReprendreDessin__(self):
        if self.state:
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerFibonacci__(n, l) 
        else:
            self.__DessinerFibonacci__(self.nombre, self.longueur)

    def dessiner(self):
        """Méthode pour démarrer ou reprendre le dessin"""
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()


class FractalesPythagore:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre 
        self.longueur = longueur // 5
        self.gestionnaire = gestionnaire
        self.state = []  

    def __Carre__(self,l) :
        for i in range(4) :
            self.gestionnaire.turtle.forward(l)
            self.gestionnaire.turtle.right(90)


    def __DessinerPythagore__(self,n,l) :
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return 
        
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.__CouleurRandom__()

        if n == 1:
            return self.__Carre__(l)
        if n > 1 :
            self.__Carre__(l)
            self.gestionnaire.turtle.forward(l)
            racine_cote = l/(2**(1/2))
            self.gestionnaire.turtle.left(45)
            self.__DessinerPythagore__(n-1, racine_cote)
            self.gestionnaire.turtle.right(90)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.forward(racine_cote)
            self.gestionnaire.turtle.pendown()
            self.__DessinerPythagore__(n-1, racine_cote)
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.backward(racine_cote)
            self.gestionnaire.turtle.pendown()
            self.gestionnaire.turtle.left(45)
            self.gestionnaire.turtle.backward(l)

    def __ReprendreDessin__(self):
        if self.state:
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerPythagore__(n, l)
        else:
            self.__DessinerPythagore__(self.nombre, self.longueur)

    def dessiner(self):
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()


# -------------------------------------------------------------------------------------- #
# ----------------------- FractaloPy © Tous droits réservés 2024 ----------------------- #
# -------------------------------------------------------------------------------------- #

# https://github.com/Gandalf0207/FractaloPy