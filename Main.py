# Importation des modules / librairies nécessaires

from Fractales import MainFractales
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion
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
    
    colors = askcolor(title="Couleur trait")
    couleurInverse = luminosityColor(str(colors[1]))
    cadreVisuelCouleur.configure(bg = colors[1], text=str(colors[1]), fg=couleurInverse)

def TailleTraitAffichage(value):
    textTailleTrait.config(text=f"Taille trait : {value}")

def ClearMaKe(fig):
    reponseUtilisateur = askquestion("Clear", "Vous êtes sur le point de supprimer la toile. Voulez vous la sauvegarder en image ?")
    if reponseUtilisateur == 'yes':
        a = 1 ### Faire appel au script de génération de l'image (en passant la classe object pour avoir les bonnes infos je pense) ## module à faire

    fig.clear()  
    fig.set_facecolor("#ffffff") # pour check que les modifs se font bien
    canvas.draw()

def ChoixBackground(fig):
    def luminosityColor(hex_color):
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        # Calcule la luminosité perçue
        luminosity = (0.299 * r + 0.587 * g + 0.114 * b)
    
        # Choisit le texte en fonction de la luminosité
        return '#000000' if luminosity > 186 else '#FFFFFF'
    
    colors = askcolor(title="Couleur Arrière Plan")
    couleurInverse = luminosityColor(str(colors[1]))
    cadreVisuelBackground.configure(bg = colors[1], text=str(colors[1]), fg=couleurInverse)
    fig.set_facecolor(f"{colors[1]}")
    canvas.draw()


    
    
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
box1Profondeur.pack(padx = 5, pady = 5, fill='x')
valeurProfondeur = StringVar()
valeurProfondeur.set(5)
textProfondeur = Label(box1Profondeur, text=f"Profondeur : {valeurProfondeur.get()}")
textProfondeur.pack(fill='x')
scrollBarProfondeur = Scale(box1Profondeur, variable=valeurProfondeur,orient='horizontal',from_=1, to=11,showvalue=0, command=ProfondeurAffichage)
scrollBarProfondeur.pack(fill='x')

# Box2 : Couleur
box2Couleur = Frame(framePanelModif, bg=None)
box2Couleur.pack(pady=5, padx=5, fill='x')
bouttonChoixCouleur = Button(box2Couleur, text="Couleur : ▶️", command=ChoixCouleur)
bouttonChoixCouleur.pack(fill='x')
cadreVisuelCouleur = Label(box2Couleur, bg = "#c3c3c3", text="#c3c3c3")
cadreVisuelCouleur.pack(fill='x')

# Box 3 : Taille trait
box3TailleTrait = Frame(framePanelModif, bg = None)
box3TailleTrait.pack(pady=5,padx=5,fill='x')
valeurTailleTrait = StringVar()
valeurTailleTrait.set(5)
textTailleTrait = Label(box3TailleTrait, text=f"Taille trait : {valeurTailleTrait.get()}")
textTailleTrait.pack(fill='x')
scrollBarTailleTrait = Scale(box3TailleTrait, variable=valeurTailleTrait, orient='horizontal', from_=1, to=11, showvalue=0, command=TailleTraitAffichage)
scrollBarTailleTrait.pack(fill='x')

# Box 4 : Clear Canva Matplotlib
box4Clear = Frame(framePanelModif, bg = None)
box4Clear.pack(pady=5, padx=5,fill='x')
textButtonClear = Label(box4Clear, text="Nettoyage Toile")
textButtonClear.pack()
buttonClear = Button(box4Clear, text="Clear !", command=lambda:ClearMaKe(fig))
buttonClear.pack(fill='x')

# Box 5 : ArrièrePlan
box5Background = Frame(framePanelModif, bg= None)
box5Background.pack(fill='x', padx=5, pady=5)
butttonChoixBackground = Button(box5Background,text="Arrière Plan : ▶️", command=lambda:ChoixBackground(fig))
butttonChoixBackground.pack(fill='x')
cadreVisuelBackground = Label(box5Background, bg = "#ffffff", text="#ffffff")
cadreVisuelBackground.pack(fill='x')

# Box du canvas et btn img + pause -------------------------------------------------------
frameBoxCanvas = Frame(fenetre, bg=bgFramePanelModif)
frameBoxCanvas.pack(expand=True, fill=BOTH)

# Création de la figure dans Tkinter
fig = plt.Figure(dpi=94)
fig.set_facecolor("#ffffff")
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