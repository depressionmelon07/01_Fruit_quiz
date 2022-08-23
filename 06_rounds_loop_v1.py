# set balance for testing purposes
rounds_left = 5

rounds_played = 0

play_again = input("Press <Enter> to play"),lower()
while play_again == "":

    # increase the number of rounds played
    rounds_played += 1

    # print the round number
    print("*** Round #{} ***".format(rounds_played))
    rounds_left -= 1
    print("Rounds left: ", rounds_left)
    print()

    if rounds_left < 1:
        play_again = "xxx"
        print("Sorry, you have played all of your rounds")
    else:

        play_again = input("Press Enter to play again or 'xxx' to quit")

