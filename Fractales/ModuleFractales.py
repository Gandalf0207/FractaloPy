from settings import *
#Gestion ---
class MainFractaleGestion(object):
    def __init__(self, profondeur, couleurTrait, longueurTrait, turtle, screen):
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.longueurTrait = longueurTrait
        self.isPaused = False
        self.turtle = turtle
        self.screen = screen
        self.isFinished = True
        self.fractale = None
        self.fractaleType = None

    def ChangerProfondeur(self, profondeur):
        self.profondeur = profondeur

    def ChangerCouleur(self, newCouleurTrait):
        self.couleurTrait = newCouleurTrait
        if newCouleurTrait != "Random":
            self.turtle.pencolor(self.couleurTrait)

    def CouleurRandom(self):
        self.turtle.pencolor('#{:06x}'.format(randint(0, 0xFFFFFF)))

    def ChangerlongueurTrait(self, newlongueurTrait):
        self.longueurTrait = newlongueurTrait

    def Lancer(self, fractaleType):
        self.isPaused = False

        # Sélectionne et dessine la fractale en fonction du type
        if self.isFinished == True or fractaleType != self.fractaleType:
            self.fractaleType = fractaleType
            self.isFinished = False
            match fractaleType:
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
            self.fractale.dessiner()
            
        elif self.isFinished == False:
            self.fractale.dessiner()
            self.isFinished = True

    def Pause(self):
        self.isPaused = True


# Ajout de chaque fractale en suivant la compo nécéssaire pour chaque fonctionnalités
class FractaleSierpinski:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []  # Pile pour sauvegarder l'état de la récursion

    def __DessinerSierpinski__(self, n, l):

        # Sauvegarde de l'état actuel si on met en pause
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return  # Arrêt temporaire
        
        # Paramétrage de la tortue
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.CouleurRandom()

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
        """Reprend le dessin depuis l'état sauvegardé"""
        if self.state:
            # Récupération de l'état sauvegardé
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerSierpinski__(n, l)
        else:
            self.__DessinerSierpinski__(self.nombre, self.longueur)

    def dessiner(self):
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()


class FractaleKoch:
    def __init__(self, nombre, longueur, gestionnaire):
        """Initialise la fractale de Koch avec une profondeur et une longueur de segment."""
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []  # Pile pour sauvegarder l'état de la récursion

    def __DessinerKoch__(self, n, l):
        """Méthode récursive pour dessiner le flocon de Koch de profondeur n et longueur l."""
                # Sauvegarde de l'état actuel si on met en pause
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return  # Arrêt temporaire

        # Paramétrage de la tortue
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()
        
        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.CouleurRandom()

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
        """Reprend le dessin depuis l'état sauvegardé"""
        if self.state:
            # Récupération de l'état sauvegardé
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerKoch__(n, l)
        else:
            self.__DessinerKoch__(self.nombre, self.longueur)

    
    def dessiner(self):
        """Méthode pour dessiner le flocon de Koch en utilisant la profondeur et la longueur initiales."""
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()


class FractaleVicsek:
    def __init__(self, nombre, longueur, gestionnaire):
        """Initialisation de la fractale de Vicsek"""
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []  # Pile pour sauvegarder l'état de la récursion
        
    def __Carre__(self, l):
        self.gestionnaire.turtle.pendown()
        for i in range(4):
            self.gestionnaire.turtle.forward(l)
            self.gestionnaire.turtle.left(90)

    def __DessinerVicsek__(self, n, l):
        # Sauvegarde de l'état actuel si on met en pause
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return  # Arrêt temporaire

        # Paramétrage de la tortue
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.CouleurRandom()

        # Sauvegarder la position actuelle
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
        """Reprend le dessin depuis l'état sauvegardé"""
        if self.state:
            # Récupération de l'état sauvegardé
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerVicsek__(n, l)
        else:
            self.__DessinerVicsek__(self.nombre, self.longueur)

    def dessiner(self):
        """Commence ou reprend le dessin"""
        if not self.gestionnaire.isPaused:
            self.__ReprendreDessin__()


class FractaleFibonacci:
    def __init__(self, nombre, longueur, gestionnaire):
        """Initialisation de la fractale du mot de Fibonacci"""
        self.nombre = nombre *5
        self.longueur = longueur // 100
        self.gestionnaire = gestionnaire
        self.state = []  # Pile pour sauvegarder l'état de la récursion

    def liste(self, n):
        if n == 1:
            return "B"
        elif n == 2:
            return self.liste(n - 1) + "A"
        elif n > 2:
            return self.liste(n - 1) + self.liste(n - 2)

    def __DessinerFibonacci__(self, n, l):

        # Paramétrage de la tortue
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if not self.gestionnaire.isPaused:
            # Dessiner selon la séquence de Fibonacci
            self.mot = self.liste(n)
            self.mot = list(self.mot)
            
            for i in range(len(self.mot)):

                if self.gestionnaire.couleurTrait == "Random":
                    self.gestionnaire.CouleurRandom()
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
        """Reprend le dessin depuis l'état sauvegardé"""
        if self.state:
            # Récupération de l'état sauvegardé
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.__DessinerFibonacci__(n, l)  # Reprend le dessin
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
        self.state = []  # Pile pour sauvegarder l'état de la récursion

    def __Carre__(self,l) :
        for i in range(4) :
            self.gestionnaire.turtle.forward(l)
            self.gestionnaire.turtle.right(90)


    def __DessinerPythagore__(self,n,l) :

        # Sauvegarde de l'état actuel si on met en pause
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return  # Arrêt temporaire
        
        # Paramétrage de la tortue
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if self.gestionnaire.couleurTrait == "Random":
            self.gestionnaire.CouleurRandom()


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
        """Reprend le dessin depuis l'état sauvegardé"""
        if self.state:
            # Récupération de l'état sauvegardé
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
