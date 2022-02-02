from random import randint


def get_the_number():
    """
    Getting the number from user till he writes it correctly

    :return: users_number:int
    """
    while True:
        try:
            number = int(input("Guess the number: "))
            return number
        except (ValueError, TypeError):
            print("It's not a number!")


def guess_the_number():
    """Main function for guessing the number"""
    number_to_guess = randint(1, 100)
    guessed = False
    while not guessed:
        user_number = get_the_number()
        if user_number == number_to_guess:
            print("You win!")
            guessed = True
        elif user_number > number_to_guess:
            print("To big!")
        else:
            print("To small!")


if __name__ == "__main__":
    guess_the_number()
