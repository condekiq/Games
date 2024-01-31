from tkinter import *
import random

from snake_game_classes import *

GAME_WIDTH = 500
GAME_HEIGHT = 500
GRID_SIZE = 50
SNAKE_SPEED = 100
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= GRID_SIZE
    elif direction == "down":
        y += GRID_SIZE
    elif direction == "left":
        x -= GRID_SIZE
    elif direction == "right":
        x += GRID_SIZE

    if x >= GAME_WIDTH:
        x = 0
    elif x < 0:
        x = GAME_WIDTH - GRID_SIZE

    if y >= GAME_HEIGHT:
        y = 0
    elif y < 0:
        y = GAME_HEIGHT - GRID_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=snake.color)
    snake.squares.insert(0, square)

    if [x,y] != food.coordinates:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    else:
        del food.coordinates
        canvas.delete(food.squares)
        del food.squares
        food = Food(canvas)

    window.after(SNAKE_SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

food = Food(canvas)
snake = Snake(canvas)

direction = 'down'

window.update()

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

next_turn(snake, food)

window.mainloop()