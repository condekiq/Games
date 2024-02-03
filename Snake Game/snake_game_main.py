from tkinter import *
import random
from snake_game_classes import *

from PIL import ImageTk, Image

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if snake.direction == "up":
        y -= GlobalVariables.GRID_SIZE
    elif snake.direction == "down":
        y += GlobalVariables.GRID_SIZE
    elif snake.direction == "left":
        x -= GlobalVariables.GRID_SIZE
    elif snake.direction == "right":
        x += GlobalVariables.GRID_SIZE

    # Ciclic condition
    if x >= GlobalVariables.GAME_WIDTH:
        x = 0
    elif x < 0:
        x = GlobalVariables.GAME_WIDTH - GlobalVariables.GRID_SIZE

    if y >= GlobalVariables.GAME_HEIGHT:
        y = 0
    elif y < 0:
        y = GlobalVariables.GAME_HEIGHT - GlobalVariables.GRID_SIZE
    #----------

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + GlobalVariables.GRID_SIZE, y + GlobalVariables.GRID_SIZE, fill=snake.color)
    snake.squares.insert(0, square)

    if [x,y] != food.coordinates:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        if (x,y) in snake.coordinates[1:]:
            return True
    else:
        snake.size += 1
        GlobalVariables.score += 1
        del food.coordinates
        canvas.delete(food.squares)
        del food.squares
        food = Food(canvas)
        label.config(text="Score: {}".format(GlobalVariables.score))

    window.after(snake.speed, next_turn, snake, food)

def change_direction(new_direction, snake):
    if new_direction == 'left' and snake.direction != 'right':
        snake.direction = new_direction
    elif new_direction == 'right' and snake.direction != 'left':
        snake.direction = new_direction
    elif new_direction == 'up' and snake.direction != 'down':
        snake.direction = new_direction
    elif new_direction == 'down' and snake.direction != 'up':
        snake.direction = new_direction

window = Tk()
window.title("Snake Game")
window.resizable(False, False)
#window.geometry("700x500")

label = Label(window, text="Score: {}".format(GlobalVariables.score), font=('consolas', 40))
label.pack(padx=0, pady=15, side=TOP)

canvas = Canvas(window, bg=GlobalVariables.background_color, height=GlobalVariables.GAME_HEIGHT, width=GlobalVariables.GAME_WIDTH)
canvas.pack()

food = Food(canvas)
snake = Snake(canvas)

window.update()

window.bind('<Left>', lambda event: change_direction('left', snake))
window.bind('<Right>', lambda event: change_direction('right', snake))
window.bind('<Up>', lambda event: change_direction('up', snake))
window.bind('<Down>', lambda event: change_direction('down', snake))

next_turn(snake, food)

window.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# # Create a photoimage object of the image in the path
# image1 = Image.open("C:\\Users\\conde\\OneDrive\\Documentos\\GitHub\\Games\\Snake Game\\pp.jpg")
# test = ImageTk.PhotoImage(image1)
# label1 = Label(image=test)
# label1.image = test
# # Position image
# label1.pack()
# root.mainloop()