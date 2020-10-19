# Program to create a f ile of usernames in bat ch mode .


def userfile():
    print("This program creates a f ile of usernames from a file of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the username go in? ")

    # open the f iles
    infileName = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file

    for line in infile:
        first, last = line.split()
        uname = (first[0] + last[:7].lower())
        infile.close()
        outfile.close()

    print("Usernames have been written to", outfileName)


if __name__ == '__main__':
    userfile()
