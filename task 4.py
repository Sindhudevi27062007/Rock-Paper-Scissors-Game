import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    # Score tracking
    user_score = 0
    computer_score = 0

    # List of valid choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # Display instructions
        print("\nRock, Paper, Scissors Game!")
        print("Choose one: rock, paper, or scissors.")

        # User input
        user_choice = input("Enter your choice: ").lower()

        # Check for valid input
        if user_choice not in choices:
            print("Invalid choice, please select rock, paper, or scissors.")
            continue

        # Computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner and update scores
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the current score
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        # Ask if the user wants to play another round
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()
