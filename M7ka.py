import random
import math

teams = []
playing_teams = {'myself': False, 'enemy': False}


class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def info(self):
        print(self.name + ': Offensive power:' + str(self.attack) +
              ' / Defensive power:' + str(self.defense))

    def get_hit_rate(self):
        return random.randint(10, self.attack)

    def get_out_rate(self):
        return random.randint(10, self.defense)


def create_teams():
    global teams
    team1 = Team('Atackers', 80, 20)
    team2 = Team('Defenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]


def show_teams():
    index = 1
    print('Information of all teams')
    for team in teams:
        print(str(index))
        team.info()
        index += 1


def choice_team(player):
    if player == 'myself':
        player_name = 'Your'
    elif player == 'enemy':
        player_name = 'Opponent\'s'

    choice_team_number = int(input('Select ' + player_name + ' team(1-3) '))
    playing_teams[player] = teams[choice_team_number - 1]
    print(player_name + ' team is \'' + playing_teams[player].name + '\'')


def get_play_inning(inning):
    if inning == 'top':
        hit_rate = playing_teams['myself'].get_hit_rate()
        out_rate = playing_teams['enemy'].get_out_rate()
    elif inning == 'bottom':
        hit_rate = playing_teams['enemy'].get_hit_rate()
        out_rate = playing_teams['myself'].get_out_rate()
    inning_score = math.floor((hit_rate - out_rate) / 10)
    if inning_score < 0:
        inning_score = 0
    return inning_score


def play():
    create_teams()
    show_teams()
    choice_team('myself')
    choice_team('enemy')
    for i in range(9):
        inning_score = get_play_inning('top')
        print('Debug: top of ' + str(i + 1) + ' ' + str(inning_score))
        inning_score = get_play_inning('bottom')
        print('Debug: bottom of ' + str(i + 1) + ' ' + str(inning_score))


play()
