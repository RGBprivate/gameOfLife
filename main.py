import time
import random

# SETTINGS

# Speed of repainting canvas
speed = 0.8

# Amount of random life to generate at start
starting_life = 50

# Number of life circles. Set to None for infinity
iterations = 100

# Prebuilt maps, fell free to add out own
classic_size = [10, 10]
big_size = [30, 30]
big_huge = [60, 60]

# Chose map for game
current_size = classic_size


# PROGRAM STARTS

# Life object
class Life:
    def __init__(self, ex: bool, x, y):
        self.exists = ex
        self.x = x
        self.y = y


# Creating global canvas parameter

canvas = []


# Function for looping over game
def cycle(times):
    if times is None:
        while True:
            time.sleep(speed)
            paint()
            if modify():
                print("There is no life left!")
                break
    else:
        for i in range(times):
            time.sleep(speed)
            paint()
            if modify():
                print("There is no life left!")
                break


# Function for rendering canvas
def paint():
    for i in canvas:
        for y in i:
            print(exists(y), end=" ")
        print()
    print()


# Function for checking if any change needs to be done on any object on canvas
def modify():
    # Value to check if there is any life left
    wallE = True
    for i in canvas:
        for y in i:
            a = scan(y)
            if a != 0:
                wallE = False
            if not y.exists and a == 3:
                y.exists = True
            elif y.exists and a <= 1 or a >= 4:
                y.exists = False
    if wallE:
        return True
    else:
        return False


# Function for checking neighbors of object
def scan(obj):
    a = 0
    x = obj.x
    y = obj.y

    if x != 0 and canvas[x - 1][y].exists:
        a += 1

    if x != 0 and y + 1 < len(canvas[0]) and canvas[x - 1][y + 1].exists:
        a += 1

    if x + 1 < len(canvas) and y != 0 and canvas[x + 1][y - 1].exists:
        a += 1

    if y != 0 and canvas[x][y - 1].exists:
        a += 1

    if x != 0 and y != 0 and canvas[x - 1][y - 1].exists:
        a += 1

    if y + 1 < len(canvas[0]) and canvas[x][y + 1].exists:
        a += 1

    if x + 1 < len(canvas) and canvas[x + 1][y].exists:
        a += 1

    if y + 1 < len(canvas[0]) and x + 1 < len(canvas) and canvas[x + 1][y + 1].exists:
        a += 1

    return a


# Function creates canvas on start
def c_canvas(w, h):
    for i in range(h):
        canvas.append([])
        for y in range(w):
            canvas[i].append(Life(False, i, y))


# Depending on exists parameter, returns "O" for alive and "_" for death
def exists(obj):
    if obj.exists:
        return "O"
    else:
        return "_"


# Starts program and creates first random life on canvas
def exe():
    c_canvas(current_size[0], current_size[1])
    for i in range(starting_life):
        canvas[random.randint(0, current_size[0] - 1)][random.randint(0, current_size[1] - 1)].exists = True
    cycle(iterations)


exe()
