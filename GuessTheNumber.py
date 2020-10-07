import random
guessestaken = 0
print('Enter your name')
myname = input()
number= random.randint(1,50)
print('Well',myname,',I am thinking of a number between 1 and 50')
print('Take a guess and I will give you hints to reach my number')
while guessestaken < 5:
    guess = input("\nWhich number do you think i am thinking: ")
    guess = int(guess)
    guessestaken += 1
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        break
if guess == number:
    guesstaken=str(guessestaken)
    print('Good Job',myname,'You guessed my number in',guessestaken,'guesses.')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was',number)
