from tkinter import *
import random
from snake_game_classes import *

GAME_WIDTH = 500
GAME_HEIGHT = 500
PITCH_SIZE = 50
SNAKE_BODY = 3
SPEED = 20
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

snake = Snake()
food = Food()

score = 0
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

direction = 'down'
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

next_turn(snake, food)