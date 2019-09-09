import random

print('Start \'rock-scissors-paper\'')

print('Input your hand')
my_hand = int(input('0:rock, 1:scissors, 2:paper'))
you_hand = random.randint(0, 2)

if my_hand == 0:
  if you_hand == 0:
    print('draw')
  elif you_hand == 1:
    print('win')
  elif you_hand == 2:
    print('lose')
elif my_hand == 1:
  if you_hand == 0:
    print('lose')
  elif you_hand == 1:
    print('draw')
  elif you_hand == 2:
    print('win')
elif my_hand == 2:
  if you_hand == 0:
    print('win')
  elif you_hand == 1:
    print('lose')
  elif you_hand == 2:
    print('draw')
