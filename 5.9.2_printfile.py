# Prints a file to the screen,

def print_to_the_screen():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)


if __name__ == '__main__':
    print_to_the_screen()
