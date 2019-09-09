import random

def start_message():
  print('Start \'rock-scissors-paper\'')

def get_my_hand():
  print('Input your hand')
  return int(input('0:rock, 1:scissors, 2:paper'))

def get_you_hand():
  return random.randint(0, 2)

def view_result(hand_diff):
  if hand_diff == 0:
    print('draw')
  elif hand_diff == -1 or hand_diff == 2:
    print('win')
  else:
    print('lose')

start_message()

my_hand = get_my_hand()
you_hand = get_you_hand()
hand_diff = my_hand - you_hand

view_result(hand_diff)
