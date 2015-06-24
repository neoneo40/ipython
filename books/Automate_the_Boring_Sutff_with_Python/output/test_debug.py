import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = raw_input()
toss = random.randint(0, 1)

def return_guess(guess):
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    return guess
guess = return_guess(guess)
    
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = raw_input()
    if toss == return_guess(guess):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')