# Importation des modules / librairies nécessaires
from settings import *
from Fractales import ModuleFractales


class SetupFractale(object):

    def __init__(self, profondeur, couleurTrait, longueurTrait, couleurBackground, turtle, screen) -> None:
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.longueurTrait = longueurTrait
        self.couleurBackground = couleurBackground
        self.turtle = turtle
        self.screen = screen

        # Nouveaux attributs
        self.isPaused = True # Indique si le processus est en pause

        self.ModuleFractalesGestionObject = ModuleFractales.MainFractaleGestion(self.profondeur, self.couleurTrait, self.longueurTrait,self.turtle, self.screen)

    def QuestionTkinter(self, titreFenetre, textFenetre):
        return askquestion(titreFenetre, textFenetre)

    def PanelCouleurTkinter(self, titreFenetre):
        return askcolor(title=f"Couleur {titreFenetre}")
    
    def luminosityColor(self, hexColor):    
        hexColor = hexColor.lstrip('#')
        r = int(hexColor[0:2], 16)
        g = int(hexColor[2:4], 16)
        b = int(hexColor[4:6], 16)
        # Calcule la luminosité perçue
        luminosity = (0.299 * r + 0.587 * g + 0.114 * b)
    
        # Choisit le texte en fonction de la luminosité
        return '#000000' if luminosity > 186 else '#FFFFFF'

    def SaveAsPng(self):
        # Attendre un peu pour que l'écran ait le temps de se rafraîchir
        time.sleep(1)
        

        # Obtenir le chemin du fichier à enregistrer (dialogue de sauvegarde)
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                                                 title="Enregistrer sous")
        
        if file_path:
            # Obtenir les dimensions de la fenêtre turtle
            canvas = self.screen.getcanvas()
            canvas.postscript(file="turtle_drawing.ps")  # Sauvegarder d'abord en PostScript

            # Utiliser Pillow pour convertir en PNG directement à partir de PostScript
            img = ImageGrab.grab(bbox=(canvas.winfo_rootx(), canvas.winfo_rooty(),
                                    canvas.winfo_rootx() + canvas.winfo_width(),
                                    canvas.winfo_rooty() + canvas.winfo_height()))
            img.save(file_path)



    def ProfondeurAffichage(self, value, textProfondeur):
        self.profondeur = int(value)
        textProfondeur.config(text=f"Profondeur : {value}")
        self.ModuleFractalesGestionObject.ChangerProfondeur(self.profondeur)


    def ChoixCouleur(self, cadreVisuelCouleur, bouttonChoixCouleur):
        reponseUtilisateur = self.QuestionTkinter("Choix Couleur Type", "Voulez vous une génération aléatoire de couleurs ?")
        if reponseUtilisateur == 'no':
            colors = self.PanelCouleurTkinter(titreFenetre='trait')
            luminosity = self.luminosityColor(hexColor=str(colors[1]))
            cadreVisuelCouleur.configure(bg = colors[1], text=str(colors[1]), fg=luminosity)
            bouttonChoixCouleur.configure(text="Couleur : Définie")   
            self.couleurTrait = str(colors[1])  
            self.ModuleFractalesGestionObject.ChangerCouleur(self.couleurTrait)  
        else:
            cadreVisuelCouleur.configure(bg = "#000000", text="#Random", fg="#ffffff")
            bouttonChoixCouleur.configure(text="Couleurs : Aléatoires")
            self.couleurTrait = "Random"

    def longueurTraitAffichage(self, value, textlongueurTrait):
        self.longueurTrait = int(value)
        textlongueurTrait.config(text=f"Longueur trait : {value}")
        self.ModuleFractalesGestionObject.ChangerlongueurTrait(self.longueurTrait)

    def ClearMake(self, cadreVisuelBackground):
        reponseUtilisateur = self.QuestionTkinter("Clear", "Vous êtes sur le point de supprimer la toile. Voulez vous la sauvegarder en image ?")
        if reponseUtilisateur == "yes":
            self.SaveAsPng()
        self.turtle.clear()
        self.screen.bgcolor("#ffffff") # pour check que les modifs se font bien
        self.screen.update()
        cadreVisuelBackground.configure(bg = "#ffffff", text="#ffffff")

    
    def ChoixBackground(self, cadreVisuelBackground):
        colors = self.PanelCouleurTkinter(titreFenetre='Arrière Plan')
        luminosity = self.luminosityColor(hexColor=str(colors[1]))
        cadreVisuelBackground.configure(bg = colors[1], text=str(colors[1]), fg=luminosity)
        self.screen.bgcolor(f"{colors[1]}")
        self.screen.update()
        self.couleurBackground = str(colors[1])
        
    def OrientationAffichage(self, value, textOrientation):
        self.Orientation = int(value)
        textOrientation.config(text=f"Orientation : {value}")
        self.turtle.setheading(self.Orientation)
        self.screen.update()

    def EpaisseurAffichage(self, value, textEpaisseur):
        self.Epaisseur = int(value)
        textEpaisseur.config(text=f"Epaisseur trait : {value}")
        self.turtle.pensize(self.Epaisseur)

    def ActiveCurseurPosition(self):
        canvasturtle.bind("<Button-1>", self.ClickButtonMoveTurtle)
    
    def ClickButtonMoveTurtle(self, event):
        canvas_width = canvasturtle.winfo_width()
        canvas_height = canvasturtle.winfo_height()

        # Transformation des coordonnées pour que (0,0) soit au centre du canvas
        turtle_x = event.x - canvas_width / 2
        turtle_y = canvas_height / 2 - event.y

        self.turtle.penup()
        self.turtle.goto((turtle_x , turtle_y))
        self.turtle.pendown()
        self.screen.update()
        cadreInfosPositions.config(text=f"({turtle_x},{turtle_y})")

        canvasturtle.unbind("<Button-1>")

    # Méthode pour gérer le bouton pause/lancer
    def LancerPauseAppel(self, typeFractale = None):
        if not self.isPaused:
            self.isPaused = True
            self.ModuleFractalesGestionObject.Pause()
        else:
            self.isPaused = False
            self.ModuleFractalesGestionObject.Lancer(typeFractale)
            self.screen.update()  # Assurer que l'écran est mis à jour après chaque appel

    
    
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




# Box du canvas et btn img + pause -------------------------------------------------------
frameBoxCanvas = Frame(fenetre, bg = None)
frameBoxCanvas.pack(expand=True, fill=BOTH)

canvasturtle = ScrolledCanvas(frameBoxCanvas)
canvasturtle.pack(expand=True, fill=BOTH)

# Set up the turtle screen using the canvas
screen = TurtleScreen(canvasturtle)

# Create a turtle instance attached to the screen
turtle = RawTurtle(screen)
screen.tracer(0)

# Box boutton pause et generation d'image
frameBoxButton = Frame(frameBoxCanvas, bg="blue")
frameBoxButton.pack(side=BOTTOM, fill='x')

# Bouton lancer/pause (gauche)
buttonLancerPause = Button(frameBoxButton, bg='white', width=15, text="Lancer", command=lambda: toggle_pause())
buttonLancerPause.pack(side=LEFT, pady=10, padx=10)

# Fonction pour mettre à jour le bouton et l'état
def toggle_pause(typeFractale = None):
    if object1.isPaused:
        buttonLancerPause.config(text="Pause")
    else:
        buttonLancerPause.config(text="Lancer")
    object1.LancerPauseAppel(typeFractale)

# Boutton Générer une image (droite)
buttonMakePlotToImg = Button(frameBoxButton,text="Enregistrer", bg="white", width=15, command=lambda: object1.SaveAsPng())
buttonMakePlotToImg.pack(side=RIGHT, pady=10, padx=10)


# Ajout d'un menu pour le choix des fractales
box6ChoixFractale = Frame(framePanelModif, bg=None)
box6ChoixFractale.pack(pady=5, padx=5, fill='x')
textChoixFractale = Label(box6ChoixFractale, text="Choix de la fractale :")
textChoixFractale.pack(fill='x')

fractaleType = StringVar(value=fractaleListe[0])  # Valeur par défaut
choixFractaleMenu = OptionMenu(box6ChoixFractale, fractaleType, *fractaleListe)  # Ajouter d'autres types ici
choixFractaleMenu.pack(fill='x')

# Appel pour choisir et lancer la fractale
buttonLancerPause.config(command=lambda: toggle_pause(fractaleType.get()))










# Box1 : Profondeur
box1Profondeur = Frame(framePanelModif, bg = None)
box1Profondeur.pack(padx = 5, pady = 5, fill='x')
valeurProfondeur =  IntVar()
valeurProfondeur.set(5)
textProfondeur = Label(box1Profondeur, text=f"Profondeur : {valeurProfondeur.get()}")
textProfondeur.pack(fill='x')
scrollBarProfondeur = Scale(box1Profondeur, variable=valeurProfondeur,orient='horizontal',from_=1, to=11,showvalue=0, command=lambda value:object1.ProfondeurAffichage(value=value, textProfondeur=textProfondeur))
scrollBarProfondeur.pack(fill='x')

# Box2 : Couleur
box2Couleur = Frame(framePanelModif, bg=None)
box2Couleur.pack(pady=5, padx=5, fill='x')
bouttonChoixCouleur = Button(box2Couleur, text="Couleur : ▶️", command=lambda:object1.ChoixCouleur(cadreVisuelCouleur=cadreVisuelCouleur, bouttonChoixCouleur=bouttonChoixCouleur))
bouttonChoixCouleur.pack(fill='x')
cadreVisuelCouleur = Label(box2Couleur, bg = "#c3c3c3", text="#c3c3c3")
cadreVisuelCouleur.pack(fill='x')

# Box 3 : Longueur trait
box3longueurTrait = Frame(framePanelModif, bg = None)
box3longueurTrait.pack(pady=5,padx=5,fill='x')
valeurlongueurTrait = IntVar()
valeurlongueurTrait.set(200)
textlongueurTrait = Label(box3longueurTrait, text=f"Longueur trait : {valeurlongueurTrait.get()}")
textlongueurTrait.pack(fill='x')
scrollBarlongueurTrait = Scale(box3longueurTrait, variable=valeurlongueurTrait, orient='horizontal', from_=100, to=400, showvalue=0, command=lambda value:object1.longueurTraitAffichage(value = value, textlongueurTrait=textlongueurTrait))
scrollBarlongueurTrait.pack(fill='x')

# Box 4 : Clear Canva Matplotlib
box4Clear = Frame(framePanelModif, bg = None)
box4Clear.pack(pady=5, padx=5,fill='x')
textButtonClear = Label(box4Clear, text="Nettoyage Toile")
textButtonClear.pack()
buttonClear = Button(box4Clear, text="Clear !", command=lambda:object1.ClearMake(cadreVisuelBackground=cadreVisuelBackground))
buttonClear.pack(fill='x')

# Box 5 : ArrièrePlan
box5Background = Frame(framePanelModif, bg= None)
box5Background.pack(fill='x', padx=5, pady=5)
butttonChoixBackground = Button(box5Background,text="Arrière Plan : ▶️", command=lambda:object1.ChoixBackground(cadreVisuelBackground=cadreVisuelBackground))
butttonChoixBackground.pack(fill='x')
cadreVisuelBackground = Label(box5Background, bg = "#ffffff", text="#ffffff")
cadreVisuelBackground.pack(fill='x')

# box 6 : orientation mouse 
box6Orientation = Frame(framePanelModif, bg = None)
box6Orientation.pack(fill='x', pady=5, padx=5)
valeurOrientation = IntVar()
valeurOrientation.set(180)
textOrientation = Label(box6Orientation, text=f"Orientation : {valeurOrientation.get()}")
textOrientation.pack(fill='x')
scrollBarOrientation = Scale(box6Orientation, variable=valeurOrientation, orient='horizontal', from_=0, to=360, showvalue=0, command=lambda value:object1.OrientationAffichage(value = value, textOrientation = textOrientation))
scrollBarOrientation.pack(fill='x')


#box 7 : épaisseur trait
box7Epaisseur = Frame(framePanelModif, bg = None)
box7Epaisseur.pack(fill='x', pady = 5, padx = 5)
valeurEpaisseur = IntVar()
valeurEpaisseur.set(1)
textEpaisseur = Label(box7Epaisseur, text=f"Epaisseur trait : {valeurEpaisseur.get()}")
textEpaisseur.pack(fill='x')
scrollBarEpaisseur = Scale(box7Epaisseur, variable=valeurEpaisseur, orient='horizontal', from_=1, to=5, showvalue=0, command=lambda value:object1.EpaisseurAffichage(value = value, textEpaisseur = textEpaisseur))
scrollBarEpaisseur.pack(fill='x')

# box 8 : position curseur
box8CurseurPosition = Frame(framePanelModif, bg = None)
box8CurseurPosition.pack(fill='x', pady = 5, padx=5)
textButtonCurseurPosition = Button(box8CurseurPosition, text = "Position Curseur", command=lambda:object1.ActiveCurseurPosition())
textButtonCurseurPosition.pack(fill='x')
cadreInfosPositions = Label(box8CurseurPosition, bg = None, text=f"{turtle.pos()}")
cadreInfosPositions.pack(fill='x')







# Initialisation de l'objet
object1 = SetupFractale(profondeur=5,couleurTrait='#c3c3c3',longueurTrait=200,couleurBackground="#ffffff", turtle=turtle, screen= screen)




fenetre.mainloop()



# Passer en classe objet le panel de modif pour pouvoir utiliser à chaque modif et créer un object stockable 