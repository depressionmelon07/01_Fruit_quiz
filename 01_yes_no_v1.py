# Ask user if they have played before
show_instructions = input("Have you played this game before?").lower()

# If they respond yes, output 'program continues'
# If they say something else, an error message in printed
# If they respond no, output 'display instructions'
if show_instructions == "yes":
    print("Program continues")

elif show_instructions == "y":
    print("Program continues")

elif show_instructions == "no":
    print("Display instructions")

elif show_instructions == "n":
    print("Display instructions")
else:
    print("Error")
