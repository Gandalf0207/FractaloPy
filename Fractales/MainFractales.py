import time
from turtle import pos, goto

class MainFractaleGestion(object):
    def __init__(self, profondeur, couleurTrait, tailleTrait, turtle, screen):
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.tailleTrait = tailleTrait
        self.isPaused = False
        self.turtle = turtle
        self.screen = screen
        self.fractale = None  # La fractale courante
        self.isFinished = True
        self.coords= (0,0)

    def ChangerProfondeur(self, profondeur):
        self.profondeur = profondeur

    def ChangerCouleur(self, newCouleurTrait):
        self.couleurTrait = newCouleurTrait
        self.turtle.pencolor(self.couleurTrait)

    def ChangerTailleTrait(self, newTailleTrait):
        self.tailleTrait = newTailleTrait

    def Lancer(self, fractaleType):
        self.isPaused = False
        self.turtle.penup()
        self.turtle.goto(self.coords)
        self.turtle.pendown()
        # Sélectionne et dessine la fractale en fonction du type
        if fractaleType == "Sierpinski" and self.isFinished == True:
            self.isFinished = False
            self.fractale_sierpinski = Fractale_Sierpinski(self.profondeur, self.tailleTrait, self) # NE PAS OUBLIER le self de fin pour lier les deux elements
            self.fractale_sierpinski.dessiner()
            
        elif fractaleType == "Sierpinski" and self.isFinished == False:
            self.fractale_sierpinski.dessiner()
            self.isFinished = True


        # D'autres fractales peuvent être ajoutées ici
        if self.fractale:
            self.fractale.dessiner()

        

    def Pause(self):
        self.isPaused = True
        self.coords = self.turtle.pos()



class Fractale_Sierpinski:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire  # Initialisation du gestionnaire

    def dessiner_sierpinski(self, n, l):
        self.gestionnaire.turtle.speed(1000)
        self.gestionnaire.screen.update()
        if n == 0 and not self.gestionnaire.isPaused:
            for i in range(3):
                self.gestionnaire.turtle.forward(l)
                self.gestionnaire.turtle.left(120)

        elif not self.gestionnaire.isPaused:
            self.dessiner_sierpinski(n - 1, l / 2)
            self.gestionnaire.turtle.forward(l / 2)
            self.dessiner_sierpinski(n - 1, l / 2)
            self.gestionnaire.turtle.backward(l / 2)
            self.gestionnaire.turtle.left(60)
            self.gestionnaire.turtle.forward(l / 2)
            self.gestionnaire.turtle.right(60)
            self.dessiner_sierpinski(n - 1, l / 2)
            self.gestionnaire.turtle.left(60)
            self.gestionnaire.turtle.backward(l / 2)
            self.gestionnaire.turtle.right(60)

        # else:
        #     self.nombre = n
        #     self.longeur = l


    def dessiner(self):
        self.dessiner_sierpinski(self.nombre, self.longueur)
