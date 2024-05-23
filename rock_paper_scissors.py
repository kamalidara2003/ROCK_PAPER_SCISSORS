import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please choose rock, paper, or scissors.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__== "__main__":
    main()