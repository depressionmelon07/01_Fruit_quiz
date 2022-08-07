# PROGRAM JOBS*****************
# If they respond yes, output 'program continues'
# If they say something else, an error message in printed
# If they respond no, output 'display instructions'
# PROGRAM JOBS*****************

# Functions under this line **********************************************
def yes_no(question):
    valid = False
    while not valid:
        response = input("Have you played this game before?").lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer with Yes or No")


def instructions():
    print("***** How to play *****")
    print()
    print("The rules of the game will go here")
    print()
    return ""


# Main routine under this line ******************************************

played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

print("Program continues")
