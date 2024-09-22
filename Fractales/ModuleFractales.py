from turtle import*

class FractaleKoch:
    def __init__(self, profondeur, longueur):
        """Initialise la fractale de Koch avec une profondeur et une longueur de segment."""
        self.profondeur = profondeur
        self.longueur = longueur

    def dessiner_koch(self, profondeur, longueur):
        """Méthode récursive pour dessiner le flocon de Koch de profondeur profondeur et longueur longueur."""
        if profondeur == 0:
            forward(longueur)
        else:
            self.dessiner_koch(profondeur-1, longueur/3)
            left(60)
            self.dessiner_koch(profondeur-1, longueur/3)
            left(-120)
            self.dessiner_koch(profondeur-1, longueur/3)
            left(60)
            self.dessiner_koch(profondeur-1, longueur/3)
    
    def dessiner(self):
        """Méthode pour dessiner le flocon de Koch en utilisant la profondeur et la longueur initiales."""
        self.dessiner_koch(self.profondeur, self.longueur)

class Vicsek :
    def __init__(self, profondeur, longueur) :
        self.profondeur = profondeur
        self.longueur = longueur

    def carre(self, longueur):
        speed(0)
        color("black", "black")
        pendown()
        for i in range(4):
            color("black", "black")
            begin_fill()
            forward(longueur)
            left(90)
            end_fill()
        
    def Vicsek(self, profondeur, longueur):
        x = xcor()
        y = ycor()
        if profondeur == 0:
            self.carre(longueur)
            penup()
            goto(x+longueur*2,y)
            self.carre(longueur)
            penup()
            goto(x+longueur,y+longueur)
            self.carre(longueur)
            penup()
            goto(x,y+longueur*2)
            self.carre(longueur)
            penup()
            goto(x+longueur*2,y+longueur*2)
            self.carre(longueur)
            penup()
        elif profondeur > 0:
            Vicsek(profondeur-1,longueur/3)
            penup()
            goto(x+longueur*2,y)
            Vicsek(profondeur-1,longueur/3)
            penup()
            goto(x+longueur,y+longueur)
            Vicsek(profondeur-1,longueur/3)
            penup()
            goto(x,y+longueur*2)
            Vicsek(profondeur-1,longueur/3)
            penup()
            goto(x+longueur*2,y+longueur*2)
            Vicsek(profondeur-1,longueur/3)
            penup()

class Sierpinsky:
    def __init__(self, profondeur, longueur) :
        self.profondeur = profondeur
        self.longueur = longueur

    def Sierpinsky(profondeur, longueur):
        """trace un triangle de sierpinsky
        apres profondeur itérations, à partir d'un
        triangle equilatéral de côté longueur
        """
        if profondeur > 0 :
            for i in range(3):
                Sierpinsky(profondeur-1, longueur/2)
                forward(longueur)
                left(120)