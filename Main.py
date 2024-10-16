# -------------------------------------------------------------------------------------- #
# ----------------------- FractaloPy © Tous droits réservés 2024 ----------------------- #
# -------------------------------------------------------------------------------------- #

# https://github.com/Gandalf0207/FractaloPy


# Importation Fichier Settings
from settings import *
# Importation second script
from Fractales import ModuleFractales


class SetupFractale(object):
    """ Class contenant toutes les méthodes permettant de modifier les parametres de génération de la fractale;
        Instanciation de la class MainFractaleGestion. """
    
    def __init__(self, profondeur, couleurTrait, longueurTrait, couleurBackground, turtle, screen) -> None:
        """ Méthode d'initialisation de la class, grâce à l'instanciation de la class par l'objet1. 
        Cette méthode permet donc la création de cette meme class et l'instanciation de la class MainFractaleFestion

        Input : prodondeur (int), 
                couleurTrait (str), 
                longeurTrait (int), 
                couleurBackgound (str), 
                turtle (TurteModule), 
                screen (TurtleModule)
        Output : None """

        self.profondeur = profondeur # Valeur de récursion
        self.couleurTrait = couleurTrait # Couleur du dessin
        self.longueurTrait = longueurTrait # Longueur du trait
        self.couleurBackground = couleurBackground # Couleur de l'arrière plan
        self.turtle = turtle # Turtle element
        self.screen = screen # Turtle element
        self.isPaused = True # Boolean de pause

        # Instanciation de la class MainFractaleGestion
        self.ModuleFractalesGestionObject = ModuleFractales.MainFractaleGestion(self.profondeur, self.couleurTrait, self.longueurTrait,self.turtle, self.screen)



    def __QuestionTkinter__(self, titreFenetre, textFenetre):
        """ Méthode privée pour ouvrir une fenetre qui pose une question à l'utilisateur
        
        Input : titreFenetre (str),
                textFenetre (str)      
        Output : askquestion window (element tkinter) """

        # Ouverture de la fenetre avec les éléments envoyés
        return askquestion(titreFenetre, textFenetre)



    def __PanelCouleurTkinter__(self, titreFenetre):
        """ Méthode privée pour ouvrir une fenetre de choix de couleur
        
        Input : titreFenetre (str),       
        Output : askcolor window (element tkinter) """

        # Ouverture de la fenetre avec l'éléments envoyés
        return askcolor(title=f"Couleur {titreFenetre}")
    


    def __LuminosityColor__(self, hexColor):  
        """ Méthode privée pour calculer le niveau de luminosité d'une couleur depuis son code héxadécimal.
        Dans le but de retourner une couleur contrasté avec ce niveau de luminosité, pour favoriser le confort 
        et l'accessibilité de lecture de l'utilisteur.
        
        Input : hexColor (str),                
        Output : code héxadécimal en fonction du niveau de luminosité """

        # Récupération et calcul ave les valeurs données
        hexColor = hexColor.lstrip('#')
        r = int(hexColor[0:2], 16)
        g = int(hexColor[2:4], 16)
        b = int(hexColor[4:6], 16)
        luminosity = (0.299 * r + 0.587 * g + 0.114 * b) # Calcule la luminosité perçue
        return '#000000' if luminosity > 186 else '#FFFFFF' # Choisit la couleur du texte en fonction de la luminosité
    
    
    def __ClickButtonMoveTurtle__(self, event):
        """ Méthode privée qui place le curseur aux coordonnées choisies par l'utilisateur.
        Mise à jour de l'interface de l'utilisateur en général après cela.

        Input : event (element tkinter)
        Output : None
        """

        # Récupération de la largeur et longueur du canvas de dessin
        canvas_width = canvasturtle.winfo_width()
        canvas_height = canvasturtle.winfo_height()

        # Transformation des coordonnées pour que (0,0) soit au centre du canvas
        turtle_x = event.x - canvas_width / 2
        turtle_y = canvas_height / 2 - event.y

        # Position et mise en place de la tortue et mise à jour de l'interface utilisateur
        self.turtle.penup()
        self.turtle.goto((turtle_x , turtle_y))
        self.turtle.pendown()
        self.screen.update()
        cadreInfosPositions.config(text=f"({turtle_x},{turtle_y})")

        canvasturtle.unbind("<Button-1>") # Arret de la sélection du click Gauche



    def ProfondeurAffichage(self, value, textProfondeur):
        """ Méthode modifiant l'affichage de la valeur de prodondeur sur l'interface utilisateur
        et sur les attributs de MainFractaleGestion.
        
        Input : value (str),
                textPrfondeur (variable tkinter) 
        Output : None """
        
        self.profondeur = int(value) # Modification de la valeur de profondeur au sein de la class
        textProfondeur.config(text=f"Profondeur : {value}") # Modification du text interface utilisateur
        self.ModuleFractalesGestionObject.ChangerProfondeur(self.profondeur) # Actualisation de la valeur dans MainFractaleGestion



    def ChoixCouleur(self, cadreVisuelCouleur, bouttonChoixCouleur):
        """ Méthode modifiant l'affichage de la valeur couleur sur l'interface utilisteur (code + bg visualisation)
        et sur les attributs de MainFractaleGestion. (soit unique / soit aléatoire). Ouverture d'une fenetre
        question (unique / aléatoire). Ouverture d'une fenetre choix de couleur.
        
        Input : cadreVisuelCouleur (element tkinter), 
                buttonChoixCouleur (element tkinter)
        Output : None """

        # Appel de la méthode privé e
        reponseUtilisateur = self.__QuestionTkinter__("Choix Couleur Type", "Voulez-vous une génération aléatoire de couleurs ?")
        # Action différente en fonction de la réponse utilisateur
        if reponseUtilisateur == 'no': # Gestion de la couleur unique
            colors = self.__PanelCouleurTkinter__(titreFenetre='trait') # Appel ouverture fenetre choix couleur
            luminosity = self.__LuminosityColor__(hexColor=str(colors[1])) # Appel choix luminosité texte
            cadreVisuelCouleur.configure(bg = colors[1], text=str(colors[1]), fg=luminosity) # Mise à jour bg visualisation utilisteur + code héxa affiché
            bouttonChoixCouleur.configure(text="Couleur : Définie")  # Information complémentaire mise à jour interface utilisateur  
            self.couleurTrait = str(colors[1]) # Actualisation de la couleur du trait pour la class
        else: # Gestion de la couleur aléatoire
            cadreVisuelCouleur.configure(bg = "#000000", text="#Random", fg="#ffffff") # Mise à jour bg visualisation utilisateur + code héxa affiché
            bouttonChoixCouleur.configure(text="Couleurs : Aléatoires") # Information complémentaire mise à jour interface utilisateur  
            self.couleurTrait = "Random" # Actualisation de la couleur du trait pour la class
            
        self.ModuleFractalesGestionObject.ChangerCouleur(self.couleurTrait) # Actualisation de la couleur du trait pour la class MainFractaleGestion



    def LongueurTraitAffichage(self, value, textlongueurTrait):
        """ Méthode modifiant l'affichage de la valeur de longeur du trait sur l'interface utilisteur
        et sur les attributs de MainFractaleGestion.
        
        Input : value (str),
                textLongueurTrait (variable tkinter) 
        Output : None """

        self.longueurTrait = int(value) # Modification de la valeur de longueurTrait au sein de la class
        textlongueurTrait.config(text=f"Longueur trait : {value}") # Modification du text interface utilisateur
        self.ModuleFractalesGestionObject.ChangerlongueurTrait(self.longueurTrait) # Actualisation de la valeur dans MainFractaleGestion



    def ClearMake(self, cadreVisuelBackground):
        """ Méthode permettant de supprimer tout ce qui se trouve sur le canvas. Avant le script 
        demande une confirmation sous forme d'une fenetre avec une question et une possibilité de sauvegarder 
        ou non une image du dessin. Après, l'interface utilisateur est mise à jour 
        
        Input : cadreVisuelBackground (element tkinter)
        Output : None """

        # Appel de la méthode privé 
        reponseUtilisateur = self.__QuestionTkinter__("Clear", "Vous êtes sur le point de supprimer la toile. Voulez vous la sauvegarder en image ?")
        if reponseUtilisateur == "yes": # Gestion pour une réponse 
            self.SaveAsPng() # Appel de la mathode pour sauvegarder une image en png
        self.turtle.clear() # Suppression des dessins
        self.screen.bgcolor("#ffffff") # Mise en place d'un nouvel arrière plan
        self.screen.update() # Mise à jour du canvas pour l'utilisateur
        cadreVisuelBackground.configure(bg = "#ffffff", text="#ffffff") # Mise à jour dans les paramètres de l'utilisateur



    def ChoixBackground(self, cadreVisuelBackground):
        """ Méthode permettant de choisir l'arrière plan du canvas. Ouverture d'une fenetre de choix de 
        couleur, Mise à jour de l'interface utilisateur en fonction.  
        
        Input : cadreVisuelBackground (element tkinter)
        Output : None"""

        colors = self.__PanelCouleurTkinter__(titreFenetre='Arrière Plan') # Appel de la méthode privé 
        luminosity = self.__LuminosityColor__(hexColor=str(colors[1])) # Appel de la méthode privé 
        cadreVisuelBackground.configure(bg = colors[1], text=str(colors[1]), fg=luminosity) # Mise à jour interface utilisateur
        self.screen.bgcolor(f"{colors[1]}") # Mise à jour de l'arrière plan du canvas
        self.screen.update() # Mise à jour de l'arrière plan du canvas de l'interface utilisateur
        self.couleurBackground = str(colors[1]) # Actualisation de la couleur de l'arrière plan au sein de la class
        


    def OrientationAffichage(self, value, textOrientation):
        """ Méthode permettant de choisir l'orientation du curseur.
        
        Input : textOrientation (element tkinter)
        Output : None"""

        self.Orientation = int(value) # Actualisation de l'orientation du curseur au sein de la class
        textOrientation.config(text=f"Orientation : {value}") # Mise à jour de cette même valeur au l'interface utilisateur
        self.turtle.setheading(self.Orientation) # Modification de l'angle de la turte (element turtle)
        self.screen.update() # Mise à jour de l'interface utilisateur (canvas)



    def EpaisseurAffichage(self, value, textEpaisseur):
        """ Méthode permettant de modifier l'épaisseur du trait de dessin
        
        Input : value (str),
                textEpaisseur (element tkinter) 
        Output : None """

        self.Epaisseur = int(value) # Actualisation de l'épaisseur au sein de la class
        textEpaisseur.config(text=f"Epaisseur trait : {value}") # Modification du text interface utilisateur
        self.turtle.pensize(self.Epaisseur) # Actualisation de la taille du curseur de la turtle



    def ActiveCurseurPosition(self):
        """ Méthode qui active simplement le get du click gauche et qui appelle la méthode privé compétente
        
        Input : None
        Output : None """

        # Activation du get de la touche click gauche sur le canvas
        canvasturtle.bind("<Button-1>", self.__ClickButtonMoveTurtle__)
    


    def LancerPauseAppel(self, typeFractale = None):
        """ Méthode permettant de lancer ou de mettre en pause en fonction de l'état de l'attribut et d'agir sur la class MainFractaleGestion
        
        Input : typeFractale : (str) None si aucune valeur envoyé
        Output : None """

        if not self.isPaused: # Si le boolean est False
            self.isPaused = True # On met en pause
            self.ModuleFractalesGestionObject.Pause() # On met à jour la class MainFractaleGestion, en pause
        else: # Si le boolean est True
            self.isPaused = False # On met en marche
            self.ModuleFractalesGestionObject.Lancer(typeFractale) # On lance avec la méthode compétente
            self.screen.update() # Assurer que l'écran est mis à jour après chaque appel
            toggle_pause() # On modifie l'affichage correcpondant pour l'interface utilisateur



    def SaveAsPng(self):
        """ Méthode permettant l'enregistrement du canvas déssiné par l'utilisateur au formet png.
        Le script prend un screen de la fenetre canvas, le sauvegarde en PostScript et puis le convertit au format png.
        Il ouvre une fenetre permettant à l'utilisteur de choisir le chemin d'enregistrement de l'image.
        
        Input : None
        Output : image.png """

        #Temps d'attente d'actualisation de la fenetre
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
            img.save(file_path) # Enregistrement de l'image au chemin indiqué




def toggle_pause(typeFractale = None):
    """ Fonction qui permet de mettre à jour l'affichage du bouton pause et 
    d'appeler la méthode compétente
    
    Input : typeFractale (str ou None si aucune valeur)
    Output : None """


    if object1.isPaused: # Si le boolean est en True
        buttonLancerPause.config(text="Pause") # On met à jour le texte
    else: # Si le boolean est en False
        buttonLancerPause.config(text="Lancer") # On met à jour le texte
    object1.LancerPauseAppel(typeFractale) # On appel la méthode pour lancer le tout
 


def LienOuvrir(lien):
    """ Fonction pour ouvrir un lien dans un navigateur
    
    Input : None
    Ouput : None """
    webbrowser.open_new(lien)


def SeparatorAdd():
    """ Fonction qui ajoute un séparateur pour épurer l'affichage
    
    Input : None
    Ouput : None """

    # Ajout d'un séparateur entre les sections
    separator = ttk.Separator(framePanelModif, orient='horizontal')
    separator.pack(fill='x', pady=5)


# --------------------------------------------------------------- #
# -------------------------- TOOL BOX --------------------------- #
# --------------------------------------------------------------- #

# Element global
widthFrameModifPanel = 200

# Initialisation de la fenetre Mère
fenetre = ttk.Window(themename = "sandstone")
fenetre.geometry("900x600")
fenetre.title("FractaloPY | © Cyanne Théo Loan Quentin")


# --------------------------------------------------------------- #
# --------------------------- CANVAS ---------------------------- #
# --------------------------------------------------------------- #

# Frame qui contient le canvas et les boutons pause
frameBoxCanvas = Frame(fenetre)
frameBoxCanvas.pack(side = RIGHT, expand=True, fill=BOTH)

# Setup des elements turtle
canvasturtle = ScrolledCanvas(frameBoxCanvas)
canvasturtle.pack(expand=True, fill=BOTH)
screen = TurtleScreen(canvasturtle)
turtle = RawTurtle(screen)
screen.tracer(0)

# Box bouton pause et génération d'image
frameBoxButton = Frame(frameBoxCanvas)
frameBoxButton.pack(side=BOTTOM, fill='x')

# Bouton lancer/pause (gauche)
buttonLancerPause = Button(frameBoxButton, width=15, text="Lancer", command=lambda: toggle_pause(fractaleType.get()))
# Utilisation de grid pour positionner
buttonLancerPause.grid(row=0, column=0, padx=10, pady=10)

# Label Titre du projet + lien GitHub, centré et bien visible
buttonTitreLienProjet = Label(frameBoxButton, text="FractaloPy", fg="black", cursor="hand2", font=("Arial", 20, "bold"))
buttonTitreLienProjet.grid(row=0, column=1, padx=10)  # Centré dans la colonne du milieu
buttonTitreLienProjet.bind("<Button-1>", lambda e: LienOuvrir("https://github.com/Gandalf0207/FractaloPy"))

# Bouton Générer une image (droite)
buttonMakePlotToImg = Button(frameBoxButton, text="Enregistrer", width=15, command=lambda: object1.SaveAsPng())
# Utilisation de grid pour positionner
buttonMakePlotToImg.grid(row=0, column=2, padx=10, pady=10)

# Optionnel: pour centrer tout dans la même ligne, ajuster les poids des colonnes
frameBoxButton.grid_columnconfigure(0, weight=1)  # Lancer bouton
frameBoxButton.grid_columnconfigure(1, weight=1)  # Titre projet
frameBoxButton.grid_columnconfigure(2, weight=1)  # Enregistrer bouton



# --------------------------------------------------------------- #
# ------------------- PANEL DE MODIFICATION --------------------- #
# --------------------------------------------------------------- #

# frame global panel modif
framePanelModif = Frame(fenetre, width=widthFrameModifPanel)
framePanelModif.pack(anchor=W, side=LEFT, expand=False, fill='y', padx=10, pady=10)

# Box1 : Profondeur
box1Profondeur = Frame(framePanelModif)
box1Profondeur.pack(padx = 5, pady = 5, fill='x')
valeurProfondeur =  StringVar()
valeurProfondeur.set(5)
textProfondeur = Label(box1Profondeur, text=f"Profondeur : {valeurProfondeur.get()}")
textProfondeur.pack(fill='x')
scrollBarProfondeur = Scale(box1Profondeur, variable=valeurProfondeur,orient='horizontal',from_=1, to=11,showvalue=0,cursor='hand2', command=lambda value:object1.ProfondeurAffichage(value=value, textProfondeur=textProfondeur))
scrollBarProfondeur.pack(fill='x')

SeparatorAdd()

# Box2 : Couleur
box2Couleur = Frame(framePanelModif)
box2Couleur.pack(pady=5, padx=5, fill='x')
bouttonChoixCouleur = Button(box2Couleur,cursor='hand2', text="Couleur : ▶️", command=lambda:object1.ChoixCouleur(cadreVisuelCouleur=cadreVisuelCouleur, bouttonChoixCouleur=bouttonChoixCouleur))
bouttonChoixCouleur.pack(fill='x')
cadreVisuelCouleur = Label(box2Couleur, bg = "#c3c3c3", text="#c3c3c3")
cadreVisuelCouleur.pack(fill='x')

SeparatorAdd()

# Box 3 : Longueur trait
box3longueurTrait = Frame(framePanelModif)
box3longueurTrait.pack(pady=5,padx=5,fill='x')
valeurlongueurTrait = StringVar()
valeurlongueurTrait.set(200)
textlongueurTrait = Label(box3longueurTrait, text=f"Longueur trait : {valeurlongueurTrait.get()}")
textlongueurTrait.pack(fill='x')
scrollBarlongueurTrait = Scale(box3longueurTrait,cursor='hand2', variable=valeurlongueurTrait, orient='horizontal', from_=100, to=400, showvalue=0, command=lambda value:object1.LongueurTraitAffichage(value = value, textlongueurTrait=textlongueurTrait))
scrollBarlongueurTrait.pack(fill='x')

SeparatorAdd()

# Box 4 : Clear Canva Matplotlib
box4Clear = Frame(framePanelModif)
box4Clear.pack(pady=5, padx=5,fill='x')
textButtonClear = Label(box4Clear, text="Nettoyage Toile")
textButtonClear.pack()
buttonClear = Button(box4Clear, text="Clear !",cursor='hand2', command=lambda:object1.ClearMake(cadreVisuelBackground=cadreVisuelBackground))
buttonClear.pack(fill='x')

SeparatorAdd()

# Box 5 : ArrièrePlan
box5Background = Frame(framePanelModif)
box5Background.pack(fill='x', padx=5, pady=5)
butttonChoixBackground = Button(box5Background,text="Arrière Plan : ▶️",cursor='hand2', command=lambda:object1.ChoixBackground(cadreVisuelBackground=cadreVisuelBackground))
butttonChoixBackground.pack(fill='x')
cadreVisuelBackground = Label(box5Background, bg = "#ffffff", text="#ffffff")
cadreVisuelBackground.pack(fill='x')

SeparatorAdd()

# box 6 : orientation mouse 
box6Orientation = Frame(framePanelModif)
box6Orientation.pack(fill='x', pady=5, padx=5)
valeurOrientation = StringVar()
valeurOrientation.set(180)
textOrientation = Label(box6Orientation, text=f"Orientation : {valeurOrientation.get()}")
textOrientation.pack(fill='x')
scrollBarOrientation = Scale(box6Orientation,cursor='hand2', variable=valeurOrientation, orient='horizontal', from_=0, to=360, showvalue=0, command=lambda value:object1.OrientationAffichage(value = value, textOrientation = textOrientation))
scrollBarOrientation.pack(fill='x')

SeparatorAdd()

#box 7 : épaisseur trait
box7Epaisseur = Frame(framePanelModif)
box7Epaisseur.pack(fill='x', pady = 5, padx = 5)
valeurEpaisseur = StringVar()
valeurEpaisseur.set(1)
textEpaisseur = Label(box7Epaisseur, text=f"Epaisseur trait : {valeurEpaisseur.get()}")
textEpaisseur.pack(fill='x')
scrollBarEpaisseur = Scale(box7Epaisseur, variable=valeurEpaisseur,cursor='hand2', orient='horizontal', from_=1, to=5, showvalue=0, command=lambda value:object1.EpaisseurAffichage(value = value, textEpaisseur = textEpaisseur))
scrollBarEpaisseur.pack(fill='x')

SeparatorAdd()

# box 8 : position curseur
box8CurseurPosition = Frame(framePanelModif)
box8CurseurPosition.pack(fill='x', pady = 5, padx=5)
textButtonCurseurPosition = Button(box8CurseurPosition, cursor='hand2', text = "Position Curseur", command=lambda:object1.ActiveCurseurPosition())
textButtonCurseurPosition.pack(fill='x')
cadreInfosPositions = Label(box8CurseurPosition, text=f"{turtle.pos()}")
cadreInfosPositions.pack(fill='x')

SeparatorAdd()

# box 9 : Ajout d'un menu pour le choix des fractales
box9ChoixFractale = Frame(framePanelModif)
box9ChoixFractale.pack(pady=5, padx=5, fill='x')
textChoixFractale = Label(box9ChoixFractale, text="Choix de la fractale :")
textChoixFractale.pack(fill='x')
fractaleType = StringVar(value=fractaleListe[0])  # Valeur par défaut
choixFractaleMenu = OptionMenu(box9ChoixFractale, fractaleType, *fractaleListe) 
choixFractaleMenu.pack(fill='x')



# --------------------------------------------------------------- #
# ----------------- INITIALISATION DE L'OBJET ------------------- #
# --------------------------------------------------------------- #

# Initialisation avec les valeurs par défault
object1 = SetupFractale(profondeur=5,couleurTrait='#c3c3c3',longueurTrait=200,couleurBackground="#ffffff", turtle=turtle, screen= screen)

# fenetre loop 
fenetre.mainloop()



# -------------------------------------------------------------------------------------- #
# ----------------------- FractaloPy © Tous droits réservés 2024 ----------------------- #
# -------------------------------------------------------------------------------------- #

# https://github.com/Gandalf0207/FractaloPy
