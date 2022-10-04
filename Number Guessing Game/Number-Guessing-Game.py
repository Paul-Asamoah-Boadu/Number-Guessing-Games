# Import random and logo:
import random
from art import logo

# Create a global scope:
EASY_LEVEL = 10
HARD_LEVEL = 5


# To compare your guess with the answer:
def check_answer(guess, answer, turn):
    """To check whether the user's guess is correct or worng by comparing it to
 the answer and dedict the number of turn if the guess is wrong"""
    if guess < answer:
        print("	Too low 😤")
        return turn - 1
    elif guess > answer:
        print("	Too high 😤")
        return turn - 1
    else:
        print(f"You got it! The answer was {answer} 🥳🥳")


# Select the level you want:
def choose_level():
    """To choose the perfered level my inputing easy or hard by the user"""
    while True:
        try:
            level = input("Choose a difficulty. Type 'easy' or 'hard': ")
            if level == "easy":
                return EASY_LEVEL
            if level == "hard":
                return HARD_LEVEL
                break
        except ValueError:
            print("Sorry you didnt elect the right level, Please try again 😔")


def game():
    """Excute the entire game"""
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("	I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)

    turn = choose_level()

    guess = 0
    while guess != answer:
        print(f"	You have {turn} attempts remaining to guess the number 🤯")
        while True:
            try:
                guess = int(input("Make a guess "))
                break
            except ValueError:
                print("Sorry you didnt enter a number, Please try again 😔")
        turn = check_answer(guess, answer, turn)
        if turn == 0:
            print("You have run out of guess. You loss! 😥😢")
            return
        elif guess != answer:
            print("Guess again")


game()
