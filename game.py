import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Ask the player to guess the number
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    guess = int(input("Enter your guess: "))
    
    # Check if the player's guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly.")
    else:
        # If the player's guess is not correct, provide hints
        while guess != secret_number:
            if guess < secret_number:
                print("Your guess is too low. Try again.")
            elif guess > secret_number:
                print("Your guess is too high. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
            guess = int(input("Enter your guess: "))
    
    # The game ends when the player guesses the correct number
    print("Game over! The secret number was", secret_number)

if __name__ == "__main__":
    play_game()
