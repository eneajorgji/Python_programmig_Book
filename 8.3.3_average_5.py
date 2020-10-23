# In the file numbers.txt are saves 7 number
# for the function average_number()


def average_number():
    file_name = input("What file are the numbers in? ")
    in_file = open(file_name, 'r')
    total = 0.0
    count = 0

    for line in in_file:
        total += float(line)
        count += 1
    print("\nThe average of the numbers is", total / count)


if __name__ == '__main__':
    average_number()
