from tkinter import *
import random
import snake_game_classes as sgc

GAME_WIDTH = 500
GAME_HEIGHT = 500
PITCH_SIZE = 50
SPEED = 20
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

snake = sgc.Snake()
food = sgc.Food()

direction = 'down'
window.bind('<Left>', lambda event: sgc.change_direction('left'))
window.bind('<Right>', lambda event: sgc.change_direction('right'))
window.bind('<Up>', lambda event: sgc.change_direction('up'))
window.bind('<Down>', lambda event: sgc.change_direction('down'))

sgc.next_turn(snake, food, PITCH_SIZE, GAME_WIDTH, GAME_HEIGHT, SPEED)