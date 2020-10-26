from graphics import *


def color_pick():
    win = GraphWin("Color Window", 1000, 1000)

    while True:
        key = win.getKey()
        if key == "q":
            break

        if key == "r":
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("lightgray")
        elif key == "b":
            win.setBackground("lightblue")

    win.close()


if __name__ == '__main__':
    color_pick()
