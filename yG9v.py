import random

teams = []
playing_teams = {'myself': False, 'enemy': False}

class Team:
  def __init__(self, name, attack, defense):
    self.name = name
    self.attack = attack
    self.defense = defense

  def info(self):
    print(self.name + ': Offensive power:' + str(self.attack) + ' / Defensive power:' + str(self.defense))

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

def play():
  create_teams()
  show_teams()
  choice_team('myself')
  choice_team('enemy')

play()
