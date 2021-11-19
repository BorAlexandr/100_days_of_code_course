# day 4 of challenge 100 days programming course
# In this projects i wrote game rock, paper, scissors.



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

#Write your code below this line 👇
import random


player_choose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
comp_choose = random.randint(0,2)
signals = [rock, paper, scissors]

if player_choose > 2:
  print('Incorrect value, you lose')
else:
  if player_choose == comp_choose:
    print(signals[player_choose])
    print(f'Computer choose:\n{signals[comp_choose]}')
    print('You have drow')
  elif player_choose == 0 and comp_choose == 2:
    print(signals[player_choose])
    print(f'Computer choose:\n{signals[comp_choose]}')
    print('You have win')
  elif player_choose == 1 and comp_choose == 0:
    print(signals[player_choose])
    print(f'Computer choose:\n{signals[comp_choose]}')
    print('You have win')
  elif player_choose == 2 and comp_choose == 1:
    print(signals[player_choose])
    print(f'Computer choose:\n{signals[comp_choose]}')
    print('You have win')
  else:
    print(signals[player_choose])
    print(f'Computer choose:\n{signals[comp_choose]}')
    print('You lose')

