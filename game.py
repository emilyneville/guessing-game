
def number_guessing_game():
    """A number-guessing game."""
    import random


    # TODO -- validate user input (make sure it's an int btwn 1 and 100)

    user_name = input("What is your name?\n> ")
    print(f"{user_name}, I am thinking of a number between 1 and 100.\nTry to guess my number!")

    magic_number = random.randint(1,100)
    high_num = 100
    low_num = 1
    counter = 0

    while True:
    
        try: guess = int(input(f"Choose a number between {low_num} and {high_num}: "))
        except ValueError:
            print("Invalid input. Please try again!")

        # print(f"pssssst... the number is {magic_number}")
        counter += 1
        if guess == magic_number:
            print(f"You won the game!!!!! You got my number in {counter} tries.")
            break
        elif guess < magic_number:
            print("The number you picked is too low! Try again.\n")
            low_num = guess
        elif guess > magic_number:
            print("The number you picked is too high! Try again.\n")
            high_num = guess
        else:
            print("Error - try again.")

number_guessing_game()


