from tkinter import *
import random
from snake_game_classes import *

def next_turn(global_var, snake, food):
    x, y = snake.coordinates[0]

    if global_var.DIRECTION == "up":
        y -= global_var.GRID_SIZE
    elif global_var.DIRECTION == "down":
        y += global_var.GRID_SIZE
    elif global_var.DIRECTION == "left":
        x -= global_var.GRID_SIZE
    elif global_var.DIRECTION == "right":
        x += global_var.GRID_SIZE

    # Ciclic condition
    if x >= global_var.GAME_WIDTH:
        x = 0
    elif x < 0:
        x = global_var.GAME_WIDTH - global_var.GRID_SIZE

    if y >= global_var.GAME_HEIGHT:
        y = 0
    elif y < 0:
        y = global_var.GAME_HEIGHT - global_var.GRID_SIZE
    #----------

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + global_var.GRID_SIZE, y + global_var.GRID_SIZE, fill=snake.color)
    snake.squares.insert(0, square)

    if [x,y] != food.coordinates:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    else:
        inputs.SNAKE_SIZE += 1
        inputs.SCORE += 1
        del food.coordinates
        canvas.delete(food.squares)
        del food.squares
        food = Food(inputs, canvas)

    window.after(inputs.SNAKE_SPEED, next_turn, inputs, snake, food)

def change_direction(new_direction, global_var):
    if new_direction == 'left' and global_var.DIRECTION != 'right':
        inputs.DIRECTION = new_direction
    elif new_direction == 'right' and global_var.DIRECTION != 'left':
        inputs.DIRECTION = new_direction
    elif new_direction == 'up' and global_var.DIRECTION != 'down':
        inputs.DIRECTION = new_direction
    elif new_direction == 'down' and global_var.DIRECTION != 'up':
        inputs.DIRECTION = new_direction

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

inputs = GlobalVariables()

window.update()

label = Label(window, text="Score:{}".format(inputs.DIRECTION), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=inputs.BACKGROUND_COLOR, height=inputs.GAME_HEIGHT, width=inputs.GAME_WIDTH)
canvas.pack()

food = Food(inputs, canvas)
snake = Snake(inputs, canvas)

window.bind('<Left>', lambda event: change_direction('left', inputs))
window.bind('<Right>', lambda event: change_direction('right', inputs))
window.bind('<Up>', lambda event: change_direction('up', inputs))
window.bind('<Down>', lambda event: change_direction('down', inputs))

next_turn(inputs, snake, food)

window.mainloop()