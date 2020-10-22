def average_number():
    n = int(input("How many numbers do you have? "))
    total = 0.0
    for i in range(n):
        x = float(input("Enter a number: "))
        total = total + x

    average = round(total / n, 2)

    print("\nThe average of the number is", average)


if __name__ == '__main__':
    average_number()
