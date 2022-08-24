

import random


class RPS:

    def __init__(self, game_list):
        self.game_list = game_list

       
    def get_winner(self, computer_choice, user_choice):

        if user_choice == computer_choice:
            winner = 'Draw'
            
        elif user_choice == 'Rock' and computer_choice == 'Scissors':
            winner = 'User'

        elif user_choice == 'Rock' and computer_choice == 'Paper':
            winner = 'Computer'
    
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            winner = 'User'
            
        elif user_choice == 'Paper' and computer_choice == 'Scissors':
            winner = 'User'
    
        elif user_choice == 'Scissors' and computer_choice == 'Rock':
            winner = 'Computer'

        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            winner = 'User'

        return winner
            
   
    def get_user_choice(self):
        user_choice = input("Enter your choice (Rock, Paper, Scissors):")
        return user_choice


    def get_computer_choice(self):
        computer_choice = random.choice(game_list)
        return computer_choice


def play(game_list):
    game = RPS(game_list)
    computer_choice = game.get_computer_choice() 
    user_choice = game.get_user_choice()
    winner = game.get_winner(computer_choice, user_choice)
    if winner == 'Draw':
        print(f'Both players selected {user_choice}, it is a tie.')
    elif winner == 'User':
        print('User wins')
    else:
        winner == 'Computer'
        print('Computer wins')

if __name__ == '__main__':
    game_list = ['Rock', 'Paper', 'Scissors']
    play(game_list)






        

