# tta funkcja 4! = 4*3*2*1 = 24


def factorial():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor

    print("The factorial of", n, "is", fact)


if __name__ == '__main__':
    factorial()
