import random

hands = ['rock', 'scissors', 'paper']

def start_message():
  print('Start \'rock-scissors-paper\'')

def get_my_hand():
  print('Input your hand')
  input_message = ''
  index = 0
  for hand in hands:
    input_message += str(index) + ':' + hand
    if index < 2:
      input_message += ', '
    index += 1
  return int(input(input_message))

def get_you_hand():
  return random.randint(0, 2)

def get_hand_name(hand_number):
  return hands[hand_number]

def view_hand(my_hand, you_hand):
  print('My hand is ' + get_hand_name(my_hand))
  print('Rival\'s hand is ' + get_hand_name(you_hand))

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

view_hand(my_hand, you_hand)
view_result(hand_diff)
