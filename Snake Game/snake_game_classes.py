import random

class GlobalVariables:
    GAME_WIDTH = 500
    GAME_HEIGHT = 500
    GRID_SIZE = 50
    background_color = "#000000"
    score = 0
class Food:
    def __init__(self, canvas):
        self.color = "#FF0000"

        x = random.randint(0, int((GlobalVariables.GAME_WIDTH/GlobalVariables.GRID_SIZE)-1)) * GlobalVariables.GRID_SIZE
        y = random.randint(0, int((GlobalVariables.GAME_HEIGHT/GlobalVariables.GRID_SIZE)-1)) * GlobalVariables.GRID_SIZE
        self.coordinates = [x, y]
        self.squares = canvas.create_oval(x, y, x + GlobalVariables.GRID_SIZE, y + GlobalVariables.GRID_SIZE, fill=self.color)
class Snake:
    def __init__(self, canvas):
        self.color = "#00FF00"
        self.speed = 100
        self.direction = "down"
        self.size = 1

        self.coordinates = []
        for i in range(0, self.size):
            self.coordinates.append([0, i*GlobalVariables.GRID_SIZE])

        self.squares = []
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + GlobalVariables.GRID_SIZE, y + GlobalVariables.GRID_SIZE, fill=self.color)
            self.squares.append(square)