import random

greeting = print('Hello, welcome to the number guessing game!')
name = input('What is the player name?\n')
number = str(random.randint(1, 100))

def guess_function(guess):
    num_of_guess = 1
    
    for guess in number:
        num_of_guess += 1
        if guess < number:
            print('Guess to low, try again.')
            get_guess()
        elif guess > number:
            print('Guess to high, try again.')
            get_guess()
    else:
        print(f'Correct {name}. You guessed the correct number in {num_of_guess} tries.')
        
def get_guess():
    guess = int(input("Guess a number between 1-100\n"))
    return guess
            
guess_function(get_guess())