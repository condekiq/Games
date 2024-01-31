from tkinter import *
import random

class GlobalVariables():
    def __init__(self):
        self.GAME_WIDTH = 500
        self.GAME_HEIGHT = 500
        self.GRID_SIZE = 50
        self.SNAKE_SPEED = 100
        self.SNAKE_SIZE = 3
        self.SNAKE_COLOR = "#00FF00"
        self.FOOD_COLOR = "#FF0000"
        self.BACKGROUND_COLOR = "#000000"
        self.SCORE = 0
        self.DIRECTION = "down"

class Food:
    def __init__(self, global_var, canvas):
        self.color = global_var.FOOD_COLOR

        x = random.randint(0, int((global_var.GAME_WIDTH/global_var.GRID_SIZE)-1)) * global_var.GRID_SIZE
        y = random.randint(0, int((global_var.GAME_HEIGHT/global_var.GRID_SIZE)-1)) * global_var.GRID_SIZE
        self.coordinates = [x, y]
        self.squares = canvas.create_oval(x, y, x + global_var.GRID_SIZE, y + global_var.GRID_SIZE, fill=self.color)

class Snake:
    def __init__(self, global_var, canvas):
        self.color = global_var.SNAKE_COLOR

        self.coordinates = []
        for i in range(0, global_var.SNAKE_SIZE):
            self.coordinates.append([0, i*global_var.GRID_SIZE])

        self.squares = []
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + global_var.GRID_SIZE, y + global_var.GRID_SIZE, fill=self.color)
            self.squares.append(square)