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
    statement_creator("How to play", "*")
    print()
    statement_creator("Choose to play between 1 and 10 rounds.\n"
                      "When the questions come up, choose the right answer using 1, 2, 3 and 4.\n"
                      "Most importantly, have FUN!", "*")

    print()
    return ""


def ask_questions():
    guesses = []

    correct_answers = 0
    question_number = 1

    for k, v in questions.items():
        if question_number > how_much:
            end_game(correct_answers)
            return
        print(question_number, ".)", k)

        [print(x) for x in options_lists[question_number - 1]]
        guess = num_check("Please choose from (1, 2, 3 or 4): ", 0, 4)
        guesses.append(guess)

        correct_answers += check_guess(v, guess)
        question_number += 1

        print(f"You have answered {correct_answers} correctly.")


def num_check(question, low, high):
    error = "{} {} {} {}".format("Please enter an integer between", low, "and", high)
    # Using this formatting allows numcheck to be used in any circumstance
    # Changed from while valid = false to while True because it is not a closing loop any ways.
    while True:
        try:
            # ask the question
            response = int(input(question))
            # if amount is too high/low then give
            if low < response <= high:
                return response

                # output error
            else:
                print(error)

        except ValueError:
            print(error)


def check_guess(answer, guess):
    if answer == guess:
        print("That's correct!")
        return 1
    else:
        print("Sorry, that's incorrect")
        return 0


def end_game(final_score):
    # to put together: "thanks for playing", score, the variable for decorator:
    final_score = "{} {}".format("Thank you for playing! Your final score is ", final_score)
    statement_creator(final_score, "*")
    return final_score


def statement_creator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine under this line ******************************************


played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

# Ask user how many questions (rounds) they want to play...
how_much = num_check("How many rounds would you like to play?", 0, 10)

# The list of questions that are being asked and their respective answers
questions = {
    "Which of these fruits is red?": 3,
    "What colour is a banana?": 1,
    "Which of these fruits is green?": 2,
    "What colour are strawberries?": 4,
    "Which of these fruits is purple?": 1,
    "Which of these fruits is pink?": 3,
    "What colour is a raspberry?": 3,
    "Which of these fruits is orange?": 4,
    "What colour are lemons?": 1,
    "Which of these fruits is brown?": 2
}

# The options that are available to choose form (displayed to the user)

options_lists = [["1) Banana", "2) Pumpkin", "3) Apple", "4) Grape"],
                 ["1) Yellow", "2) Blue", "3) Green", "4) White"],
                 ["1) Peach", "2) Pear", "3) Lemon", "4) Banana"],
                 ["1) Green", "2) Purple", "3) Black", "4) Red"],
                 ["1) Grape", "2) Apple", "3) Mandarin", "4) Watermelon"],
                 ["1) Pumpkin", "2) Lemon", "3) Peach", "4) Raspberry"],
                 ["1) Blue", "2) Green", "3) Red", "4) Yellow"],
                 ["1) Watermelon", "2) Strawberries", "3) Apple", "4) Mandarin"],
                 ["1) Yellow", "2) Pink", "3) Blue", "4) Orange"],
                 ["1) Watermelon", "2) Kiwi", "3) Pumpkin", "4) Grape"]]

# The command which starts the question and answer portion of the game
ask_questions()
