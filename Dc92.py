import random

teams = []

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

def play():
  create_teams()
  show_teams()

play()
