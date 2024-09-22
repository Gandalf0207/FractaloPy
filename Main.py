# Importation des modules / librairies nécessaires

from Fractales import MainFractales
from tkinter import *
from tkinter.colorchooser import askcolor
from turtle import *
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def ProfondeurAffichage(value):
    textProfondeur.config(text=f"Profondeur : {value}")

def ChoixCouleur():
    def luminosityColor(hex_color):
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        # Calcule la luminosité perçue
        luminosity = (0.299 * r + 0.587 * g + 0.114 * b)
    
        # Choisit le texte en fonction de la luminosité
        return '#000000' if luminosity > 186 else '#FFFFFF'
    
    colors = askcolor(title="Tkinter Color Chooser")
    couleurInverse = luminosityColor(str(colors[1]))
    cadreVisuelCouleur.configure(bg = colors[1], text=str(colors[1]), fg=couleurInverse)
    
    
# Tool Box
bgHomePage = "#f2f2ff"
bgFramePanelModif = "#fc3fc3"
widthFrameModifPanel = 200
# Initialisation de la fenetre Mère
fenetre = Tk()
fenetre.config(bg = bgHomePage)
fenetre.geometry("900x600")
fenetre.title("Fractales | © Cyanne Théo Loan Quentin")


# Panel des modifications ---------------------------------------------------------------
framePanelModif = Frame(fenetre, bg = bgFramePanelModif, width=widthFrameModifPanel)
framePanelModif.pack(side=LEFT, expand=False, fill='y', padx=10, pady=10)


# Box1 : Profondeur
box1Profondeur = Frame(framePanelModif, bg = None)
box1Profondeur.pack(padx = 5, pady = 5)
valeurProfondeur = StringVar()
valeurProfondeur.set(5)
textProfondeur = Label(box1Profondeur, text=f"Profondeur : {valeurProfondeur.get()}")
textProfondeur.pack()
scrollBarProfondeur = Scale(box1Profondeur, variable=valeurProfondeur,orient='horizontal',from_=1, to=11,showvalue=0, command=ProfondeurAffichage)
scrollBarProfondeur.pack()

# Box2 : Couleur
box2Coueur = Frame(framePanelModif, bg=None)
box2Coueur.pack(pady=5, padx=5, fill='x')
bouttonChoixCouleur = Button(box2Coueur, text="Couleur : ▶️", command=ChoixCouleur)
bouttonChoixCouleur.pack()
cadreVisuelCouleur = Label(box2Coueur, bg = "#c3c3c3", text="#c3c3c3")
cadreVisuelCouleur.pack(fill='x')

# Box du canvas et btn img + pause -------------------------------------------------------
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