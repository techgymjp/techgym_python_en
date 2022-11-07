import random

hands = ['rock', 'scissors', 'paper']
results = {'win': 'win', 'lose': 'lose', 'draw': 'draw'}
lives = {'you': 3, 'Rival': 3}


def start_message():
    print('Start \'rock-scissors-paper\'')


def show_life():
    print(f"Lives You: {lives['you']} / Rival:{lives['Rival']}")


def is_hand(string):
    if string.isdigit():
        number = int(string)
        if number >= 0 and number <= 2:
            return True
        else:
            return False
    else:
        return False


def get_my_hand():
    print('Input your hand')
    input_message = ''
    index = 0
    for hand in hands:
        input_message += str(index) + ':' + hand
        if index < 2:
            input_message += ', '
        index += 1
    return input(input_message)


def get_you_hand():
    return random.randint(0, 2)


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(my_hand, you_hand):
    print('My hand is ' + get_hand_name(my_hand))
    print('Rival\'s hand is ' + get_hand_name(you_hand))


def get_result(hand_diff):
    if hand_diff == 0:
        return 'draw'
    elif hand_diff == -1 or hand_diff == 2:
        return 'win'
    else:
        return 'lose'


def view_result(result):
    print(results[result])
    show_life()


def update_life(result):
    global lives
    if result == 'win':
        lives['Rival'] -= 1
    elif result == 'lose':
        lives['you'] -= 1


def play_once():
    my_hand = get_my_hand()
    while not is_hand(my_hand):
        my_hand = get_my_hand()

    my_hand = int(my_hand)
    you_hand = get_you_hand()
    hand_diff = my_hand - you_hand

    view_hand(my_hand, you_hand)
    result = get_result(hand_diff)
    update_life(result)
    view_result(result)
    if lives['you'] > 0 and lives['Rival'] > 0:
        play_once()


def play():
    start_message()
    show_life()
    play_once()


play()
