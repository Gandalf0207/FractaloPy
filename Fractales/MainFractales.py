import numpy as np

class MainFractaleGestion(object):
    def __init__(self, profondeur, couleurTrait, tailleTrait, fig, canvas) -> None:
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.tailleTrait = tailleTrait
        self.fig = fig
        self.canvas = canvas
        self.fractaleType = None

    def Lancer(self, fractaleType):
        # Appeler la fonction pour dessiner la fractale
        pass

   
    def ChangerCouleur(self, newCouleurTrait):
        self.couleurTrait = newCouleurTrait

    def ChangerTailleTrait(self, newTailleTrait):
        self.tailleTrait = newTailleTrait

