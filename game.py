from random import randint


def guess_the_number():
    """Main function for guessing the number"""
    number_to_guess = randint(1, 100)
    guessed = False
    while not guessed:
        try:
            users_number = int(input("Guess the number: "))
            if users_number == number_to_guess:
                print("You win!")
                guessed = True
            elif users_number > number_to_guess:
                print("To big!")
            else:
                print("To small!")
        except (ValueError, TypeError):
            print("It's not a number!")


if __name__ == "__main__":
    guess_the_number()
