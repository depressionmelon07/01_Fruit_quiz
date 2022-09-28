''' PROGRAM DESC*****************
 Program is a base for fruit_quiz game. 
 Program asks user if they have played game before.
 If they respond 'yes:'program continues'
 If they respond 'no': display instructions
 If they say anything else: error message displayed 
 V1 - laying base with first component 
 Pari Rao 11/08/22 
 PROGRAM DESC*****************'''

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
    print("The rules of the game will be here")
    print()
    return ""


# Main routine under this line ******************************************

played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

print("Program continues ")
