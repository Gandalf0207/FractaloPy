# Importation des modules / librairies nécessaires

from Fractales import MainFractales
from tkinter import *
from turtle import *
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Tool Box
bgHomePage = "#f2f2ff"
bgFramePanelModif = "#fc3fc3"
widthFrameModifPanel = 200
# Initialisation de la fenetre Mère
fenetre = Tk()
fenetre.config(bg = bgHomePage)
fenetre.geometry("900x600")
fenetre.title("Fractales | © Cyanne Théo Loan Quentin")

# Panel des modifications
framePanelModif = Frame(fenetre, bg = bgFramePanelModif, width=widthFrameModifPanel)
framePanelModif.pack(side=LEFT, expand=False, fill='y', padx=10, pady=10)


# Box du canvas et btn img + pause
frameBoxCanvas = Frame(fenetre, bg=bgFramePanelModif)
frameBoxCanvas.pack(expand=True, fill=BOTH)

# Création de la figure dans Tkinter
fig = plt.Figure(dpi=94)
fig.set_facecolor("black")
canvas = FigureCanvasTkAgg(fig, master=frameBoxCanvas)  # Mettre la figure dans Tkinter
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True, padx = 10, pady = 10)

# Box boutton pause et generation d'image
frameBoxButton = Frame(frameBoxCanvas, bg="blue")
frameBoxButton.pack(side=BOTTOM, fill='x')

# Boutton lancer pause (gauche)
buttonLancerPause = Button(frameBoxButton, bg='white', width=15)
buttonLancerPause.pack(side=LEFT, pady=10, padx=10)

# Boutton Générer une image (droite)
buttonMakePlotToImg = Button(frameBoxButton, bg="white", width=15)
buttonMakePlotToImg.pack(side=RIGHT, pady=10, padx=10)




fenetre.mainloop()



# Passer en classe objet le panel de modif pour pouvoir utiliser à chaque modif et créer un object stockable 