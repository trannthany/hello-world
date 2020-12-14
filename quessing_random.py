import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('sorry, guess again. Too high.')
    
    print (f'Congrated you got it right {random_number}') #the f-string doesn't work with ""?


def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c' and low !=high:
        if low != high:
            guess = random.randint(low, high)#random will throw error when low == high
        else:
            guess = low
        feedback = input(f'Is {guess} too high (h), too low (L), or correct (C)??'.lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print (f'the computer got your number right, {guess}')



#guess(10)
computer_guess(23)