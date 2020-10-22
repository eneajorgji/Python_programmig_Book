def average_number():
    total = 0.0
    count = 0
    x = float(input("Enter a number (negative to quit): "))

    while x >= 0:
        total += x
        count += 1
        x = float(input("Eneter a number(negative to quit): "))

    print("\nThe average of the nuber is", total / count)


if __name__ == '__main__':
    average_number()
