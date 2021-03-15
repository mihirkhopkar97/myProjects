import random
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
choices = [rock,paper,scissors]
UserInput = input('What do you choose? type 0 for rock, 1 for paper and 2 for scissors')

iUserInput = int (UserInput)
print(choices[iUserInput])


iComputerInput = random.randint(0,2)
print('Computer chose:')
print(choices[iComputerInput])

if(iUserInput == iComputerInput):
  print('Draw')
elif(iUserInput == 0):
  if(iComputerInput == 1):
    print('You lose')
  else:
    print('You Win')
elif(iUserInput == 1):
  if(iComputerInput == 2):
    print('You lose')
  else:
    print('you win')
else:
  if(iComputerInput == 0):
    print('you lose')
  else:
    print('you win')
