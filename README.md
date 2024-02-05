# Rock_Paper_Scrissors
The Rock paper Scrissors is a classic game played where 2 players have to choose a a hand out of tree. The capabilities are described below:
1. User Input:
The get_user_choice() function prompts the user to enter their choice (rock, paper, or scissors) through the console.
It ensures that the user's input is valid and keeps asking until a valid choice is provided.

2. Computer Choice:
The get_computer_choice() function randomly selects a choice (rock, paper, or scissors) for the computer.

3. Determine Winner:
The who_is_winner(user_choice, computer_choice) function compares the user's choice with the computer's choice to determine the winner based on the Rock, Paper, Scissors rules.
It returns a string indicating whether the user wins, loses, or if it's a tie.

4. Main Game Loop:
The main() function is the entry point of the program.
It welcomes the user to the game and enters into a loop where the user can play the game repeatedly.
It calls the functions mentioned above to get user input, generate computer choice, determine the winner, and display the result.
After each round, the user is asked if they want to play again. If the response is not 'yes', the loop breaks, and the game ends.

5.Execution:
The if __name__ == '__main__': block ensures that the main() function is executed when the script is run, but not when it's imported as a module.

6.Randomness:
The random.choice() function is used to randomly select the computer's choice.

7. Error Handling:
The code handles invalid user input by prompting the user to enter a valid choice.
