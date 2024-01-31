from tkinter import *
import random

from snake_game_classes import *

def next_turn(inputs, snake, food):
    x, y = snake.coordinates[0]

    if inputs.DIRECTION == "up":
        y -= inputs.GRID_SIZE
    elif inputs.DIRECTION == "down":
        y += inputs.GRID_SIZE
    elif inputs.DIRECTION == "left":
        x -= inputs.GRID_SIZE
    elif inputs.DIRECTION == "right":
        x += inputs.GRID_SIZE

    if x >= inputs.GAME_WIDTH:
        x = 0
    elif x < 0:
        x = inputs.GAME_WIDTH - inputs.GRID_SIZE

    if y >= inputs.GAME_HEIGHT:
        y = 0
    elif y < 0:
        y = inputs.GAME_HEIGHT - inputs.GRID_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + inputs.GRID_SIZE, y + inputs.GRID_SIZE, fill=snake.color)
    snake.squares.insert(0, square)

    if [x,y] != food.coordinates:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    else:
        del food.coordinates
        canvas.delete(food.squares)
        del food.squares
        food = Food(inputs, canvas)

    window.after(inputs.SNAKE_SPEED, next_turn, inputs, snake, food)

def change_direction(new_direction, inputs):
    if new_direction == 'left' and inputs.DIRECTION != 'right':
        inputs.DIRECTION = new_direction
    elif new_direction == 'right' and inputs.DIRECTION != 'left':
        inputs.DIRECTION = new_direction
    elif new_direction == 'up' and inputs.DIRECTION != 'down':
        inputs.DIRECTION = new_direction
    elif new_direction == 'down' and inputs.DIRECTION != 'up':
        inputs.DIRECTION = new_direction

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

inputs = Inputs()

canvas = Canvas(window, bg=inputs.BACKGROUND_COLOR, height=inputs.GAME_HEIGHT, width=inputs.GAME_WIDTH)
canvas.pack()

food = Food(inputs, canvas)
snake = Snake(inputs, canvas)

window.update()

window.bind('<Left>', lambda event: change_direction('left', inputs))
window.bind('<Right>', lambda event: change_direction('right', inputs))
window.bind('<Up>', lambda event: change_direction('up', inputs))
window.bind('<Down>', lambda event: change_direction('down', inputs))

next_turn(inputs, snake, food)

window.mainloop()