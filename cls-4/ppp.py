import random


def number_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    while True:
        # Step 2: Get user input and handle potential input errors
        try:
            guess = int(input("Enter your guess (1 to 100): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Step 4: Provide feedback based on the user's guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            # Step 5: If the guess is correct, congratulate the user and end the game
            print(f"Congratulations! You guessed the number {target_number} correctly.")
            print(f"It took you {attempts} attempts.")
            break


# Call the function to start the game
number_guessing_game()

