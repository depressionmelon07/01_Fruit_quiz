# Functions under this line ******************************************


# Main routine under this line ******************************************

error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("How many rounds would you like you play? "))
        # if amount is too high/low then give
        if 0 < response <= 10:
            print("You have asked to play " "{} rounds".format(response))

            # output error
        else:
            print(error)

    except ValueError:
        print(error)

