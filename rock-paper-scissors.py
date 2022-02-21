rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

random.seed()

is_game_over = False

game_choices = ["rock", "paper", "scissors"]

number_of_choices = len(game_choices)

while is_game_over == False:

    computer_choice = game_choices[random.randint(0, number_of_choices - 1)]
    player_choice = input("Type your choice: ")
    player_choice = player_choice.lower()

    if player_choice not in game_choices:
        print("Not a available choice.")
    else:
        if player_choice == "rock" and computer_choice == "rock":
            print(f"PLAYER:\n{rock}\nCOMPUTER:\n{rock}")
            print("Draw!")
        elif player_choice == "rock" and computer_choice == "paper":
            print(f"PLAYER:\n{rock}\nCOMPUTER:\n{paper}")
            print("You Lose!")
        elif player_choice == "rock" and computer_choice == "scissors":
            print(f"PLAYER:\n{rock}\nCOMPUTER:\n{scissors}")
            print("You Won!")

        if player_choice == "scissors" and computer_choice == "scissors":
            print(f"PLAYER:\n{scissors}\nCOMPUTER:\n{scissors}")
            print("Draw!")
        elif player_choice == "scissors" and computer_choice == "rock":
            print(f"PLAYER:\n{scissors}\nCOMPUTER:\n{rock}")
            print("You Lose!")
        elif player_choice == "scissors" and computer_choice == "paper":
            print(f"PLAYER:\n{scissors}\nCOMPUTER:\n{paper}")
            print("You Won!")

        if player_choice == "paper" and computer_choice == "paper":
            print(f"PLAYER:\n{paper}\nCOMPUTER:\n{paper}")
            print("Draw!")
        elif player_choice == "paper" and computer_choice == "scissors":
            print(f"PLAYER:\n{paper}\nCOMPUTER:\n{scissors}")
            print("You Lose!")
        elif player_choice == "paper" and computer_choice == "rock":
            print(f"PLAYER:\n{paper}\nCOMPUTER:\n{rock}")
            print("You Won!")
    play_again = input("Do you want to play again? [Y] or [N].")
    if play_again == 'N':
        is_game_over = True


#import random
 
# items = [ "scissors", "rock", "paper" ]
# images = [ scissors, rock, paper ]
# my_choice = input('Enter your choice: "rock", "paper", "scissors" ').lower()
 
# if my_choice not in items:
#   print("ERROR: Please enter the correct item")
#   exit(1)
 
# print(f"My choice is: {my_choice}")
# row = items.index(my_choice)
 
# comp_choice = random.choice(items)
# col = items.index(comp_choice)
# print(f"Computer choice is: {comp_choice}")
 
# result_matrix = [
#   ["Draw", "Lost!", "Won"],
#   ["Won", "Draw", "Lost!"],
#   ["Lost!", "Won", "Draw" ]
# ]
 
# print(images[row])
# print(images[col])
# print(f"Result is: {result_matrix[row][col]}")
# #exit(0)