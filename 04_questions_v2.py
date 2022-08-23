# Functions under this line ******************************************
def ask_questions():
    guesses = []

    correct_answers = 0
    question_number = 1

    for k, v in questions.items():
        print(k)

        [print(x) for x in options_lists[question_number - 1]]
        guess = num_check("Please choose from (1, 2, 3 or 4): ", 0, 4)
        guesses.append(guess)

        correct_answers += check_guess(v, guess)
        question_number += 1

        print(f"You have answered {correct_answers} correctly so far.")


def check_guess(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Sorry, that's incorrect")
        return 0

    # Main routine under this line ******************************************


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

ask_questions()
