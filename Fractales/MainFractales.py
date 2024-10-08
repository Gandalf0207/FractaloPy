from settings import *

class MainFractaleGestion(object):
    def __init__(self, profondeur, couleurTrait, longueurTrait, turtle, screen):
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.longueurTrait = longueurTrait
        self.isPaused = False
        self.turtle = turtle
        self.screen = screen
        self.fractale = None  # La fractale courante
        self.isFinished = True

    def ChangerProfondeur(self, profondeur):
        self.profondeur = profondeur

    def ChangerCouleur(self, newCouleurTrait):
        self.couleurTrait = newCouleurTrait
        self.turtle.pencolor(self.couleurTrait)

    def ChangerlongueurTrait(self, newlongueurTrait):
        self.longueurTrait = newlongueurTrait

    def Lancer(self, fractaleType):
        self.isPaused = False

        # Sélectionne et dessine la fractale en fonction du type
        if fractaleType == "Sierpinski" and self.isFinished == True:
            self.isFinished = False
            self.fractale_sierpinski = Fractale_Sierpinski(self.profondeur, self.longueurTrait, self) # NE PAS OUBLIER le self de fin pour lier les deux elements
            self.fractale_sierpinski.dessiner()
            
        elif fractaleType == "Sierpinski" and self.isFinished == False:
            self.fractale_sierpinski.dessiner()
            self.isFinished = True


        # D'autres fractales peuvent être ajoutées ici
        if self.fractale:
            self.fractale.dessiner()

        

    def Pause(self):
        self.isPaused = True



class Fractale_Sierpinski:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire
        self.state = []  # Pile pour sauvegarder l'état de la récursion

    def dessiner_sierpinski(self, n, l):
        # Sauvegarde de l'état actuel si on met en pause
        if self.gestionnaire.isPaused:
            self.state.append((n, l, self.gestionnaire.turtle.position(), self.gestionnaire.turtle.heading()))
            return  # Arrêt temporaire

        # Paramétrage de la tortue
        self.gestionnaire.turtle.speed(10)
        self.gestionnaire.screen.update()

        if n == 0:
            for i in range(3):
                self.gestionnaire.turtle.forward(l)
                self.gestionnaire.turtle.left(120)
        else:
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

    def reprendre_dessin(self):
        """Reprend le dessin depuis l'état sauvegardé"""
        if self.state:
            # Récupération de l'état sauvegardé
            n, l, pos, heading = self.state.pop()
            self.gestionnaire.turtle.penup()
            self.gestionnaire.turtle.setposition(pos)
            self.gestionnaire.turtle.setheading(heading)
            self.gestionnaire.turtle.pendown()
            self.dessiner_sierpinski(n, l)
        else:
            self.dessiner_sierpinski(self.nombre, self.longueur)

    def dessiner(self):
        """Commence ou reprend le dessin"""
        if not self.gestionnaire.isPaused:
            self.reprendre_dessin()

