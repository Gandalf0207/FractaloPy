# Librairie Tkinter
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion
from tkinter import filedialog
# Module Turtle
from turtle import *
# Librairie Pil
from PIL import ImageGrab
# Module Time
import time
# Module Random
from random import randint
# Module Webbrowser
import webbrowser
# Module ttkbootstrap
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from os.path import join 
import os
from turtle import TurtleGraphicsError  # Import de l'erreur


# Liste du nombre de fractale pour l'interface utilisateur
fractaleListe = ("Sierpinski", "Koch", "Vicsek", "Fibonacci", "Pythagore")

cursorListe = ["sun", "leaf", "unicorn"]


# -------------------------------------------------------------------------------------- #
# ----------------------- FractaloPy © Tous droits réservés 2024 ----------------------- #
# -------------------------------------------------------------------------------------- #

# https://github.com/Gandalf0207/FractaloPy