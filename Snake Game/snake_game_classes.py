from tkinter import *
import random

class Inputs():
    def __init__(self):
        self.GAME_WIDTH = 500
        self.GAME_HEIGHT = 500
        self.GRID_SIZE = 50
        self.SNAKE_SPEED = 100
        self.SNAKE_COLOR = "#00FF00"
        self.FOOD_COLOR = "#FF0000"
        self.BACKGROUND_COLOR = "#000000"
        self.DIRECTION = "down"

class Food:
    def __init__(self, inputs, canvas):
        self.color = inputs.FOOD_COLOR

        x = random.randint(0, int((inputs.GAME_WIDTH/inputs.GRID_SIZE)-1)) * inputs.GRID_SIZE
        y = random.randint(0, int((inputs.GAME_HEIGHT/inputs.GRID_SIZE)-1)) * inputs.GRID_SIZE
        self.coordinates = [x, y]
        self.squares = canvas.create_oval(x, y, x + inputs.GRID_SIZE, y + inputs.GRID_SIZE, fill=self.color, tag="food")

class Snake:
    def __init__(self, inputs, canvas):
        self.coordinates = []
        self.squares = []
        self.color = inputs.SNAKE_COLOR

        x0 = random.randint(0, int((inputs.GAME_WIDTH/inputs.GRID_SIZE)-1)) * inputs.GRID_SIZE
        y0 = random.randint(0, int((inputs.GAME_HEIGHT/inputs.GRID_SIZE)-1)) * inputs.GRID_SIZE
        for i in range(0, 3):
            self.coordinates.append([x0, y0 + i*inputs.GRID_SIZE])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + inputs.GRID_SIZE, y + inputs.GRID_SIZE, fill=self.color, tag="snake")
            self.squares.append(square)