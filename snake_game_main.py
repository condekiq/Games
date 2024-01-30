#---------- PACKAGES ----------
from tkinter import *
import random

from snake_game_classes import *
from snake_game_inputs import *

#---------- MAIN ----------
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

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

direction = 'down'
next_turn(snake, food)