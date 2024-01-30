from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
PITCH_SIZE = 50
SNAKE_BODY = 3
SPEED = 50
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = SNAKE_BODY
        self.coordinates = []
        self.squares = []

        for i in range(0, SNAKE_BODY):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + PITCH_SIZE, y + PITCH_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH/PITCH_SIZE)-1)) * PITCH_SIZE
        y = random.randint(0, int((GAME_HEIGHT/PITCH_SIZE)-1)) * PITCH_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + PITCH_SIZE, y + PITCH_SIZE, fill=FOOD_COLOR, tag="food")

class next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= PITCH_SIZE

    elif direction == "down":
        y += PITCH_SIZE

    elif direction == "left":
        x -= PITCH_SIZE

    elif direction == "right":
        x += PITCH_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + PITCH_SIZE, y + PITCH_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    del snake.coordinates[-1]

    canvas.delete(snake.squares[-1])

    del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()