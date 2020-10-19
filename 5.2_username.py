def username():
    print("THIS PROGRAM CREATES USERNAMES\n")
    first = input("Please enter your fist name (all lowercase): ")
    last = input("Please enter last fist name (all lowercase): ")

    user_name_creation = first[:3] + last[:3]

    print("Your username is: ", user_name_creation)

if __name__ == '__main__':
    username()
