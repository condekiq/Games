from tkinter import *
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
GRID_SIZE = 50
SNAKE_SPEED = 100
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Food:
    def __init__(self, canvas):
        self.color = FOOD_COLOR

        x = random.randint(0, int((GAME_WIDTH/GRID_SIZE)-1)) * GRID_SIZE
        y = random.randint(0, int((GAME_HEIGHT/GRID_SIZE)-1)) * GRID_SIZE
        self.coordinates = [x, y]
        self.squares = canvas.create_oval(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=self.color, tag="food")