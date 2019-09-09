import random

print('Start \'rock-scissors-paper\'')

print('Input your hand')
my_hand = int(input('0:rock, 1:scissors, 2:paper'))
you_hand = random.randint(0, 2)

hand_diff = my_hand - you_hand

if hand_diff == 0:
  print('draw')
elif hand_diff == -1 or hand_diff == 2:
  print('win')
else:
  print('lose')
