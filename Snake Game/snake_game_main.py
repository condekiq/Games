from tkinter import *
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
PITCH_SIZE = 50
SNAKE_BODY = 3
SPEED = 20
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = SNAKE_BODY
        self.coordinates = []
        self.squares = []

        for i in range(0, SNAKE_BODY):
            self.coordinates.append([0, i*PITCH_SIZE])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + PITCH_SIZE, y + PITCH_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH/PITCH_SIZE)-1)) * PITCH_SIZE
        y = random.randint(0, int((GAME_HEIGHT/PITCH_SIZE)-1)) * PITCH_SIZE
        self.coordinates = [x, y]
        self.squares = canvas.create_oval(x, y, x + PITCH_SIZE, y + PITCH_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= PITCH_SIZE
    elif direction == "down":
        y += PITCH_SIZE
    elif direction == "left":
        x -= PITCH_SIZE
    elif direction == "right":
        x += PITCH_SIZE

    if x >= GAME_WIDTH:
        x = 0
    elif x < 0:
        x = GAME_WIDTH - PITCH_SIZE

    if y >= GAME_HEIGHT:
        y = 0
    elif y < 0:
        y = GAME_HEIGHT - PITCH_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + PITCH_SIZE, y + PITCH_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if [x,y] == food.coordinates:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)

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