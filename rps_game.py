import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])
user_choice = input('Rock, Papers, Scissors, Shoot! \n')
winner = ('win, the computer had ' + computer_choice)

if computer_choice == user_choice:
    print('tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(winner)
elif user_choice == 'paper' and computer_choice == 'rock':
    print(winner)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(winner)
else:
    print('You lose')