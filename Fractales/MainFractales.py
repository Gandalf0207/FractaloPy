import time

class MainFractaleGestion(object):
    def __init__(self, profondeur, couleurTrait, tailleTrait, turtle, screen):
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.tailleTrait = 200
        self.isPaused = False
        self.turtle = turtle
        self.screen = screen
        self.fractale = None  # La fractale courante

    def ChangerCouleur(self, newCouleurTrait):
        self.couleurTrait = newCouleurTrait
        self.turtle.pencolor(self.couleurTrait)

    def ChangerTailleTrait(self, newTailleTrait):
        self.tailleTrait = newTailleTrait
        self.turtle.pensize(self.tailleTrait)

    def Lancer(self, fractaleType):
        # Sélectionne et dessine la fractale en fonction du type
        if fractaleType == "Sierpinski":
            self.fractale_sierpinski = Fractale_Sierpinski(self.profondeur, self.tailleTrait, self) # NE PAS OUBLIER le self de fin pour lier les deux elements
            self.fractale_sierpinski.dessiner()
        # D'autres fractales peuvent être ajoutées ici
        if self.fractale:
            self.fractale.dessiner()

    def Pause(self):
        self.isPaused = True



class Fractale_Sierpinski:
    def __init__(self, nombre, longueur, gestionnaire):
        self.nombre = nombre
        self.longueur = longueur
        self.gestionnaire = gestionnaire  # Initialisation du gestionnaire

    def dessiner_sierpinski(self, n, l):
        self.gestionnaire.turtle.speed(10)
        if n == 0:
            for i in range(3):
                self.gestionnaire.turtle.forward(l)
                self.gestionnaire.turtle.left(120)
        else:
            self._verifier_pause()
            self.dessiner_sierpinski(n - 1, l / 2)
            self.gestionnaire.turtle.forward(l / 2)
            self._verifier_pause()
            self.dessiner_sierpinski(n - 1, l / 2)
            self.gestionnaire.turtle.backward(l / 2)
            self.gestionnaire.turtle.left(60)
            self.gestionnaire.turtle.forward(l / 2)
            self.gestionnaire.turtle.right(60)
            self._verifier_pause()
            self.dessiner_sierpinski(n - 1, l / 2)
            self.gestionnaire.turtle.left(60)
            self.gestionnaire.turtle.backward(l / 2)
            self.gestionnaire.turtle.right(60)

    def _verifier_pause(self):
        while self.gestionnaire.isPaused:
            time.sleep(0.1)
        self.gestionnaire.screen.update()

    def dessiner(self):
        self.dessiner_sierpinski(self.nombre, self.longueur)
