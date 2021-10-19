import gym
from gym import error, spaces, utils
from gym.spaces import space
from gym.utils import seeding

import random

class TicTacToeEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.state = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
        ]

  def hash(self):
    return "".join([item for sublist in self.state for item in sublist])


  def available_actions(self):
    return [i for i, x in enumerate(self.hash()) if x == "-"]

  def available_states(self, player):
    states = []
    actions = self.available_actions()
    for action in actions:
      state_list = list(self.hash())
      state_list[action] = player
      state = "".join(state_list)
      _, reward = self.check_done(state)
      states.append((state, reward))
    return states

    
  def check_done(self, state):
    winner = ""
    for player in ["X", "O"]:
        if (state[0:3] == 3*player):
            winner = player
        elif (state[3:6] == 3*player):
            winner = player
        elif (state[6:9] == 3*player):
            winner = player
        elif (state[0] == player and state[3] == player and state[6] == player):
            winner = player
        elif (state[1] == player and state[4] == player and state[7] == player):
            winner = player
        elif (state[2] == player and state[5] == player and state[8] == player):
            winner = player
        elif (state[0] == player and state[4] == player and state[8] == player):
            winner = player
        elif (state[2] == player and state[4] == player and state[6] == player):
            winner = player
            
    if (winner == "X"):
      return True, (10, -10)
    elif (winner == "O"):
      return True, (-10, 10)
    elif ("-" not in self.hash()):
      return True, (0, 0)
    else:
      return False, (0, 0)

  def step(self, action, player):

    self.state[action//3][action%3] = player

    done, reward = self.check_done(self.hash())

    return self.hash(), reward, done, {}

  def reset(self):
    self.state = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
        ]


  def render(self, mode='human'):
    print("Board")
    for row in self.state:
      print(row)