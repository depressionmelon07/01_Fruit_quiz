show_instructions = ""
while show_instructions.lower() != "xxx":

    # Ask user if they have played before
    show_instructions = input("Have you played this game before?").lower()

    # If they respond yes, output 'program continues'
    # If they say something else, an error message in printed
    # If they respond no, output 'display instructions'

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("Display instructions")

    else:
        print("Error")
