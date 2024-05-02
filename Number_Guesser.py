# Import the random module for random numbers and time module for adding delays
import random
import time

# Function to get valid input from user
def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print('Please type a number next time.')

# Function to play the game 
    # Ask the user for maximum number in the range
    # Validate the maximum number
    # Generate a random number within the specified range
def play_game():
    print("\n** Welcome to the Number Guesser! **")
    playing = input("\nDo you want to play? (yes/no): ").strip().lower()
    if playing != "yes":
        quit()

    print("\nOkay! Lets play :)")
    time.sleep(1.5)

    top_of_range = get_valid_input("\nType the maximum number for the range: ")

    if top_of_range <= 0:
        print('\nPlease type a number larger than 0 next time.')
        return

    random_number = random.randint(0, top_of_range)
    guesses = 0

    # Start the guessing loop
        # Ask the user to make a guess
        # Check if the guess is correct
        # Provide feedback based on the guess
    while True:
        guesses += 1
        user_guess = get_valid_input("\nMake a guess: ")
        
        if user_guess == random_number:
            print("\nYou got it!")
            break
        elif user_guess > random_number:
            print("Oops! You guessed too high!")
        else: 
            print("Oops! You guessed too low!")

    # Display the number of guesses it took to guess correctly 
    print("You got it in", guesses, "guesses!!")

# Entry point of the program
    # Start the game
if __name__ == "__main__":
    play_game()