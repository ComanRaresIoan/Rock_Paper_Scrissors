# Rock, Paper, Scrissors

import random

def get_user_choice():
    user_choice = input("Enter your choice: \na) Rock\nb) Paper\nc) Scrissors\n")
    while user_choice not in ['rock','paper','scrissors']:
        print("Your choice is not a part of the options. Please Enter your choice: a) Rock\n b) Paper\n c) Scrissors")
        user_choice = input("Enter your choice:\na) Rock\nb) Paper\nc) Scrissors")
    return user_choice

def get_computer_choice():
    return random.choice(['rock','paper','scrissors'])

def who_is_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scrissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scrissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scrissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.\n Computer chose {computer_choice}")

        result = who_is_winner(user_choice,computer_choice)
        print(result)

        play_again = input("Do you want to play again ? (yes/no)").lower()
        if play_again != 'yes':
            break

if __name__ == '__main__':
    main()