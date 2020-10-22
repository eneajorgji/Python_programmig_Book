def average_number():
    total = 0.0
    count = 0
    more_data = "yes"

    while more_data[0] == "y":
        x = float(input("Enter a number: "))
        total += x
        count += 1
        more_data = input("Do you have more numbers? (yes or no) ")
    print("\nThe average of the number is,", round(total / count, 2))

if __name__ == '__main__':
    average_number()
