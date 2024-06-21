from GAME.exercises.ex_01.main import *
from GAME.Morkov.morkov import *
import random


def __init__(self, window):
    # making a rectangle
    self.rect = Rectangle(surface=window, width=100, height=100, x=100, y=280, color=(0,255,0))


def draw(self, window):

    # drawing a square
    self.rect.draw()

    # drawing a circle
    Circle(surface=window, color="purple", center_x=90, center_y=500, radius=90)
    
    # drawing an ellipse
    Ellipse(surface=window)