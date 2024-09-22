# Importation des modules / librairies nécessaires

from Fractales import MainFractales
from tkinter import *
from turtle import *
from numpy import *
from matplotlib import *

# Tool Box
bgHomePage = "#f2f2ff"
bgFramePanelModif = "#fc3fc3"
widthFrameModifPanel = 200
# Initialisation de la fenetre Mère
fenetre = Tk()
fenetre.config(bg = bgHomePage)
fenetre.geometry("900x500")
fenetre.title("Fractales | © Cyanne Théo Loan Quentin")

# Panel des modifications
framePanelModif = Frame(fenetre, bg = bgFramePanelModif, width=widthFrameModifPanel)
framePanelModif.pack(side=LEFT, expand=False, fill='y', padx=10, pady=10)


# Box du canvas et btn img + pause
frameBoxCanvas = Frame(fenetre, bg=bgFramePanelModif)
frameBoxCanvas.pack(expand=True, fill=BOTH)

# Canvas > matplotlib canvas # A faire
frameCanvas = Frame(frameBoxCanvas, bg="black")
frameCanvas.pack(expand=True, fill=BOTH,side=TOP,  padx=10, pady=10)

# Box boutton pause et generation d'image
frameBoxButton = Frame(frameBoxCanvas, bg="blue")
frameBoxButton.pack(side=BOTTOM, fill='x')

# Boutton pause (gauche)
buttonPause = Button(frameBoxButton, bg='white', width=15)
buttonPause.pack(side=LEFT, pady=10, padx=10)

# Boutton Générer une image (droite)
buttonMakePlotToImg = Button(frameBoxButton, bg="white", width=15)
buttonMakePlotToImg.pack(side=RIGHT, pady=10, padx=10)




fenetre.mainloop()