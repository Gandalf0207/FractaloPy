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

framePanelModif = Frame(fenetre, bg = bgFramePanelModif, width=widthFrameModifPanel)
framePanelModif.pack(side=LEFT, expand=False, fill='y', padx=10, pady=10)



fenetre.mainloop()