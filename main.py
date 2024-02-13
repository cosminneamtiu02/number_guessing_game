import random


def is_positive_whole(number):
    """
    Check if a given input is a positive whole number.

    @param number: The input to be checked.
    @type number: any
    @return: True if the input is a positive whole number, False otherwise.
    @rtype: bool
    """
    try:
        # Convert input to integer, here only for the ValueError test
        new_number = int(number)
        # Check if the number is positive and greater than -1
        return new_number > -1
    except ValueError:
        # If conversion fails or input is not a number, return False
        return False


def start_game():
    """
    Start the Number Guessing Game.
    """
    print("Hello and welcome to the Number Guessing Game!")

    max_number = -1
    # Ask the user to input the maximum number for the guessing range
    while not is_positive_whole(max_number):
        max_number = input("Please enter a positive whole number (>0 and in N) as your max guessing possibility: ")

    # Generate a random number within the specified range
    to_guess = random.randrange(0, int(max_number))
    # Prompt the user to make a guess
    print("What do you think the number is?")

    guess = -1
    ct = 1

    while guess != to_guess:
        guess = -1

        # Get the user's guess
        while not is_positive_whole(guess):
            guess = input("Please enter a whole number as a guess: ")

        guess = int(guess)

        if guess < to_guess:
            # Provide feedback if the guess is lower than the target number
            print("It's higher")
            ct += 1
        elif guess > to_guess:
            # Provide feedback if the guess is higher than the target number
            print("It's lower")
            ct += 1
        else:
            # Congratulate the user when they guess the correct number
            print("Got it!")
            # Display the number of attempts it took to guess the number
            print(f"It took you {ct} tries to guess the number.")
            break


def play_again():
    """
    Ask the user if they want to play the game again.
    """
    while True:
        again = input("Do you want to play again? (yes/no): ")
        if again.lower() == "yes":
            start_game()
        elif again.lower() == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Kick off the program by calling the start_game function.
play_again()
