def username():
    print("THIS PROGRAM CREATES USERNAMES\n")
    first = input("Please enter your fist name (all lowercase): ")
    last = input("Please enter last fist name (all lowercase): ")

    user_name_creation = first[:3] + last[:3]

    print("Your username is: ", user_name_creation)


def months():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec "

    n = int(input("Enter a month number ( 1-12) : "))

    pos = (n - 1) * 3

    month_abbreviation = months[pos:pos + 3]

    print("The month abbreviationis ", month_abbreviation + ".")


if __name__ == '__main__':
    username()
    months()
