from turtle import*

class FractaleKoch:
    def __init__(self, profondeur, longueur):
        """Initialise la fractale de Koch avec une profondeur et une longueur de segment."""
        self.profondeur = profondeur
        self.longueur = longueur

    def dessiner_koch(self, n, l):
        """Méthode récursive pour dessiner le flocon de Koch de profondeur n et longueur l."""
        if n == 0:
            forward(l)
        else:
            self.dessiner_koch(n-1, l/3)
            left(60)
            self.dessiner_koch(n-1, l/3)
            left(-120)
            self.dessiner_koch(n-1, l/3)
            left(60)
            self.dessiner_koch(n-1, l/3)
    
    def dessiner(self):
        """Méthode pour dessiner le flocon de Koch en utilisant la profondeur et la longueur initiales."""
        self.dessiner_koch(self.profondeur, self.longueur)


class FractaleVicsek:
    def __init__(self, nombre, longueur):
        """Initialisation de la fractale de Vicsek"""
        self.nombre = nombre
        self.longueur = longueur
        
    def carre(self, l):
        pendown()
        for i in range(4):
            forward(l)
            left(90)

    def dessiner_Vicsek(self, n, l):
        x = xcor()
        y = ycor()
        if n == 0:
            self.carre(l)
            penup()
            goto(x+l*2,y)
            self.carre(l)
            penup()
            goto(x+l,y+l)
            self.carre(l)
            penup()
            goto(x,y+l*2)
            self.carre(l)
            penup()
            goto(x+l*2,y+l*2)
            self.carre(l)
            penup()
        elif n > 0:
            self.dessiner_Vicsek(n-1,l/3)
            penup()
            goto(x+l*2,y)
            self.dessiner_Vicsek(n-1,l/3)
            penup()
            goto(x+l,y+l)
            self.dessiner_Vicsek(n-1,l/3)
            penup()
            goto(x,y+l*2)
            self.dessiner_Vicsek(n-1,l/3)
            penup()
            goto(x+l*2,y+l*2)
            self.dessiner_Vicsek(n-1,l/3)
            penup()
    def dessiner(self):
        """Méthode pour dessiner la fractale"""
        self.dessiner_Vicsek(self.nombre, self.longueur)

class Fractale_Fibonacci:
    def __init__(self, nombre, longueur):
        """Initialisation de la fractale du mot de fibonacci"""
        self.nombre = nombre
        self.longueur = longueur
    def liste(self,n):
        if n == 1:
            return "B"
        elif n == 2:
            return self.liste(n-1) + "A"
        elif n > 2:
            return self.liste(n-1) + self.liste(n-2)
    def dessiner_Fibonacci(self, nombre, l):
        pendown()
        mot = self.liste(nombre)
        mot = list(mot)
        for i in range(len(mot)):
            if mot[i] == "B":
                forward(l)
            elif mot[i] == "A":
                if (i+1)%2 == 0:
                    right(90)
                elif (i+1)%2 != 0:
                    left(90)
                forward(l)
    def dessiner(self):
        self.dessiner_Fibonacci(self.nombre, self.longueur)
        
if __name__ == "__main__":
    fractale = Fractale_Fibonacci(30, 2)  # CrÃ©er une instance de FractaleKoch avec profondeur 3 et longueur 200
    penup()
    goto(-100,0)
    pendown()
    fractale.dessiner()  # Dessiner la fractale
    mainloop()

if __name__ == "__main__":
    fractale = FractaleVicsek(3, 200)  # Créer une instance de FractaleKoch avec profondeur 3 et longueur 200
    fractale.dessiner()  # Dessiner la fractale
    mainloop()

# Utilisation de la classe FractaleKoch
if __name__ == "__main__":
    fractale = FractaleKoch(3, 200)  # Créer une instance de FractaleKoch avec profondeur 3 et longueur 200
    fractale.dessiner()  # Dessiner la fractale
    mainloop()