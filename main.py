import time

# SETTINGS
speed = 1.5
default_size = [5, 5]
big_size = [10, 10]


class Life:
    def __init__(self, ex: bool):
        self.exists = ex


canvas = []


def cycle(times=None):
    if times is None:
        while True:
            time.sleep(speed)
            paint()

    for i in range(times):
        time.sleep(speed)
        paint()


def paint():
    for i in canvas:
        for y in i:
            print(exists(y), end=" ")
        print()
    print()


def c_canvas(w, h):
    for i in range(h):
        canvas.append([])
        for y in range(w):
            canvas[i].append(Life(False))


def exists(obj):
    if obj.exists:
        return "X"
    else:
        return "_"


def exe():
    c_canvas(big_size[0], big_size[1])
    cycle(100)


exe()
