import turtle
import time
from turtle import *

class MainFractaleGestion(object):
    def __init__(self, profondeur, couleurTrait, tailleTrait, turtle, screen) -> None:
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.tailleTrait = tailleTrait
        self.isPaused = False
        self.segment_stack = []
        self.turtle = turtle
        self.screen = screen
        self.screen.tracer(0)  # Désactiver le traçage automatique pour un contrôle manuel du rendu

        # Paramètres Turtle
        self.turtle.speed(0)  # Vitesse maximale pour un dessin rapide
        self.turtle.hideturtle()
        self.turtle.pensize(self.tailleTrait)
        self.turtle.pencolor(self.couleurTrait)

    def Lancer(self, fractaleType):
        # Réinitialiser les variables à chaque lancement
        self.isPaused = False
        
    def ChangerCouleur(self, newCouleurTrait):
        self.couleurTrait = newCouleurTrait
        self.turtle.pencolor(self.couleurTrait)

    def ChangerTailleTrait(self, newTailleTrait):
        self.tailleTrait = newTailleTrait
        self.turtle.pensize(self.tailleTrait)

class Fractale_Fibonacci:
    def __init__(self, nombre, longueur):
        """Initialisation de la fractale du mot de fibonacci"""
        self.nombre = nombre
        self.longueur = longueur
    def liste(self,n):
        if n == 1:
            return "B"
        elif n == 2:
            return self.liste(n-1) + "A"
        elif n > 2:
            return self.liste(n-1) + self.liste(n-2)
    def dessiner_Fibonacci(self, nombre, l):
        pendown()
        mot = self.liste(nombre)
        mot = list(mot)
        for i in range(len(mot)):
            if mot[i] == "B":
                forward(l)
            elif mot[i] == "A":
                if (i+1)%2 == 0:
                    right(90)
                elif (i+1)%2 != 0:
                    left(90)
                forward(l)
    def dessiner(self):
        self.dessiner_Fibonacci(self.nombre, self.longueur)
if __name__ == "__main__":
    fractale = Fractale_Fibonacci(30, 2)  # CrÃ©er une instance de FractaleKoch avec profondeur 3 et longueur 200
    penup()
    goto(-100,0)
    pendown()
    fractale.dessiner()  # Dessiner la fractale
    mainloop()

    # Méthode pour gérer la pause
    def Pause(self):
        self.isPaused = True

    def Resume(self):
        self.isPaused = False
        self.screen.update()
