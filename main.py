import time

# SETTINGS
speed = 2
default_size = [5, 5]
big_size = [10, 10]


class Life:
    def __init__(self, ex: bool, x, y, deb):
        self.exists = ex
        self.deb = deb #FOR DEBUG
        self.x = x
        self.y = y


canvas = []


def cycle(times=None):
    if times is None:
        while True:
            time.sleep(speed)
            paint()

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
            if a != 0:
                print(a, y.x, y.y)


def scan(obj):
    a = 0
    x = obj.x
    y = obj.y

    if canvas[x - 1][y].exists:
        a += 1

    # if canvas[x - 1][y + 1].exists:
    #     a += 1
    # if canvas[x + 1][y - 1].exists:
    #     a += 1
    # if canvas[x][y - 1].exists:
    #     a += 1
    # if canvas[x - 1][y - 1].exists:
    #     a += 1
    # if canvas[x][y + 1].exists:
    #     a += 1
    # if canvas[x + 1][y].exists:
    #     a += 1
    # if canvas[x + 1][y + 1].exists:
    #     a += 1

    return a


def c_canvas(w, h):
    for i in range(h):
        canvas.append([])
        for y in range(w):
            canvas[i].append(Life(False, i, y, False))


def exists(obj):
    if obj.exists:
        return "X"
    elif obj.deb:
        return "C" #FOR DEBUG
    else:
        return "_"


def exe():
    c_canvas(big_size[0], big_size[1])

    canvas[4][4].exists = True
    canvas[5][5].exists = True

    cycle(100)


exe()
