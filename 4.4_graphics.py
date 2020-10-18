from graphics import *


def graph_principal():
    print("This program plots the growth of a 10-years investment")

    principal = float(input(("Enter the initial principal: ")))
    apr = float(input("Eneter the annualized interest rate: "))

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), '0.0K').draw(win)
    Text(Point(20, 180), '2.5K').draw(win)
    Text(Point(20, 130), '5.0K').draw(win)
    Text(Point(20, 80), '7.5K').draw(win)
    Text(Point(20, 30), '8.0K').draw(win)

    heigh = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - heigh))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        # calculate value f or the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        x11 = year * 25 + 40
        heigh = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11 + 25, 230 - heigh))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")


if __name__ == '__main__':
    graph_principal()
