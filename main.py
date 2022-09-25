import time
import random

# SETTINGS
speed = 0.8

starting_life = 40

iterations = 100

default_size = [5, 5]
big_size = [10, 10]

class Life:
    def __init__(self, ex: bool, x, y):
        self.exists = ex
        self.x = x
        self.y = y


canvas = []


def cycle(times=None):
    if times is None:
        while True:
            time.sleep(speed)
            paint()
            modify()

    for i in range(times):
        time.sleep(speed)
        paint()
        modify()


def paint():
    for i in canvas:
        for y in i:
            print(exists(y), end=" ")
        print()
    print()


def modify():
    for i in canvas:
        for y in i:
            a = scan(y)
            if not y.exists and a == 3:
                y.exists = True
            elif y.exists and a <= 1 or a >= 4:
                y.exists = False



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


def c_canvas(w, h):
    for i in range(h):
        canvas.append([])
        for y in range(w):
            canvas[i].append(Life(False, i, y))


def exists(obj):
    if obj.exists:
        return "X"
    else:
        return "_"


def exe():
    c_canvas(big_size[0], big_size[1])
    for i in range(26):
        canvas[random.randint(0, 9)][random.randint(0, 9)].exists = True
    cycle(iterations)


exe()
