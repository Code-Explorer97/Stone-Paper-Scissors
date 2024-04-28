import random

def get_computer_choice():
    choices = ["Stone", "Paper", "Scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Stone/Paper/Scissors): ").capitalize()
        if user_choice in ["Stone", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter Stone, Paper, or Scissors.")

def determine_winner(user_choice, computer_choice):
    print(f"Computer's choice: {computer_choice}")
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Stone" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Stone") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to the Stone-Paper-Scissors game!")
    print("You'll be playing against the computer.")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
