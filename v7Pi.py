import random

print('Start \'rock-paper-scissors\'')

print('Input your hand')
your_hand = int(input('0:rock, 1:scissors, 2:paper'))
computer_hand = random.randint(0, 2)

if your_hand == 0:
    if computer_hand == 0:
        print('draw')
    elif computer_hand == 1:
        print('win')
    elif computer_hand == 2:
        print('lose')
elif your_hand == 1:
    if computer_hand == 0:
        print('lose')
    elif computer_hand == 1:
        print('draw')
    elif computer_hand == 2:
        print('win')
elif your_hand == 2:
    if computer_hand == 0:
        print('win')
    elif computer_hand == 1:
        print('lose')
    elif computer_hand == 2:
        print('draw')
