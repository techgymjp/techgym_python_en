import random

print('Start \'rock-scissors-paper\' game')

print('Input your hand choice')
my_hand = int(input('0:rock, 1:scissors, 2:paper'))
you_hand = random.randint(0, 2)

if my_hand == 0:
  if you_hand == 0:
    print('Draw')
  elif you_hand == 1:
    print('Win')
elif my_hand == 1:
  if you_hand == 0:
    print('Lose')
  elif you_hand == 1:
    print('Draw')
