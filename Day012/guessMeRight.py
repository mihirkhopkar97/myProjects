import random
import art
print(art.logo)

print('Welcome to the number guessing game!!!!')
print('I am thinking of a number between 1 and 100')

number = random.randint(1, 100)
difficulty = input('Hard/Easy:')
if difficulty.lower() == 'easy':
    tries = 10
else:
    tries = 5

print(f"Great! Now you have {tries} tries to guess")
game_is_on = True
while game_is_on:
    if tries == 0:
        print(f'Oh no you lose!')
    guess = int(input('Make a guess:'))
    if guess == number:
        print(f'Great!!! There you go the number is {number}. You Win!')
        game_is_on = False
    elif guess < number:
        print('Wrong Guess! the number is greater')
        tries -= 1
    else:
        print('Wrong Guess! the number is smaller')
        tries -= 1

