# This code has been taken for educational purposes from
# https://cognitiveclass.ai/courses/course-v1:IBM+GPXX0XENEN+v1

# Gym is a library that will allow us to initialize and work with the TicTacToe environment
import gym
# Random allows us to make random choices when interacting with the environment
import random
# Custom tictactoe environment
import gym_tictactoe

env = gym.make("TicTacToe-v0")

# When our environment is created we initialize an environment variable called state which represents the state of the
# game in terms of where the X's, O's, and empty spaces are. As you can see below it starts empty.
print(env.state)
# The hash function turns the 'state' environment variable into a string that will be used to represent the current
# state.
# When the agent interacts with the environment it will use the hash. A hash is used because in many situations not
# every single aspect of the environment is needed to be saved thus the hash acts as a summarized format of the
# environment saving space and making the representation of the environment easy to read.
print(env.hash())

new_state, reward, done, info = env.step(0, "X")
print(new_state)
print(reward)
print(done)
print(info)

print(env.render())
print(env.available_actions())

print(env.available_states("O"))

print(env.check_done(env.hash()))
# `reset(self)`: Resets the board so a new game can be played
env.reset()
env.render()

# variable to keep track of if the game is over
done = False
# Good practice to reset environment before you play a game to clear any old game
env.reset()
# Print the initial board
env.render()
# Want to keep playing untill game is over
while not done:
    # Make a random action from the list of available actions for X
    new_state, reward, done, info = env.step(random.choice(env.available_actions()), "X")
    # Print board after X action
    env.render()

    # If the game is done on X action we dont want O to make an action
    if not done:
        # Make a random action from the list of available actions for O
        new_state, reward, done, info = env.step(random.choice(env.available_actions()), "O")
        # Print board after O action
        print(env.render())

# Print the reward after the game is done, reward for X is the first value and O is the second value
print(reward)

# Reinforcement Learning
# Reinforcement learning is training a robot/agent to learn what to do in certain situations. An Agent learns through
# interaction with the environment to decide what actions to take in situations by maximizing the reward it receives.

# Agent
# An agent is an algorithm that interacts and uses information from the environment such as state and reward to decide
# what actions to take. An agent's goal is to learn how to maximize reward by selecting the optimal actions in response
# to the current state. In our example, our agent will implement Temporal Difference Learning to learn and an Epsilon
# Greedy Policy to choose actions.

# State
# A scenario that the agent can get into with respect to the environment, below are all examples of states in TicTacToe
# remember we are using the hash of the board as the state.

# variable to keep track of if the game is over
done = False
# Good practice to reset environment before you play a game to clear any old game
env.reset()
# Want to keep playing untill game is over
while not done:
    # Make a random action from the list of available actions for X
    new_state, reward, done, info = env.step(random.choice(env.available_actions()), "X")
    # Print state
    print(env.hash())

    # If the game is done on X action we dont want O to make an action
    if not done:
        # Make a random action from the list of available actions for O
        new_state, reward, done, info = env.step(random.choice(env.available_actions()), "O")
        # Print state
        print(env.hash())

# Environment
# The environment is the surroundings or the conditions that the agent operates in and that the states are contained
# in. The environment takes actions provided by the agent and returns the next state and reward earned by performing
# hat action.

env.reset()
env.render()

# Reward
# The reward is the value or signal returned by the environment as a result of an action taken by the agent. To make
# an agent perform a particular task or achieve a particular goal, we must provide a reward structure for it to
# maximize. A typical structure is to have a positive, negative, and neutral reward. The reward is your way of
# communicating to the agent what you want it to achieve.
print(reward)

# Action
# Action is how the agent interacts with the environment, as you can see there are 9 options for the 9 available spaces
# on an empty TicTacToe board.
print(env.available_actions())


class Agent:

    def __init__(self, env, player="X", alpha=.4, gamma=.9):
        self.alpha = alpha
        self.gamma = gamma
        self.env = env
        self.player = player
        self.player_number = 0 if player == "X" else 1
        self.V = {}


class Agent(Agent):

    def select_action(self, epsilon=.1):
        # generates random number between 0 and 1 if it is below epsilon we take random action otherwise a greedy action
        if (random.random() < epsilon):
            # gets a random action from list of available actions
            action = random.choice(self.env.available_actions())
        else:
            # list to store action calculations
            q_values = []
            # loops through the list of available states and rewards
            for state in self.env.available_states(self.player):
                # calculates gamma*V(S') + Reward for the state
                # example: state = (("X--O-----"), (0,0))
                q_values.append(self.gamma*self.V[state[0]] + state[1][self.player_number])
            # find the max value of the action calculations
            max_value = max(q_values)
            # selects indexs of values in q_values that are the max_value
            max_indexs = [i for i, j in enumerate(q_values) if j == max_value]
            # select a random action from the actions that all have the max_value
            action = self.env.available_actions()[random.choice(max_indexs)]
        return action


class Agent(Agent):

    def add_states(self):
        # adds current state to state value function
        if (self.env.hash() not in self.V):
            self.V[self.env.hash()] = 0
        # adds all states X can get to
        for state in self.env.available_states("X"):
            if (state[0] not in self.V):
                self.V[state[0]] = 0
        # adds all states O can get to
        for state in self.env.available_states("O"):
            if (state[0] not in self.V):
                self.V[state[0]] = 0


class Agent(Agent):

    def update_state_values(self, new_state, old_state, reward):
        # V(S) = V(S) + alpha*(R + gamma*(V(S') - V(S)))
        self.V[old_state] = self.V[old_state] + self.alpha * (
                    reward + self.gamma * self.V[new_state] - self.V[old_state])


# number of games (episodes)
def train(episodes):
    # create our agents
    agent_x = Agent(env, "X")
    agent_o = Agent(env, "O")
    # loops for a certain number of games (episodes)
    for episode in range(episodes):
        # stops while loop when game is done
        done = False
        # resets environment when game is done
        env.reset()
        # while loop for a single game
        while not done:

            # X agents turn

            # adds states for both agents
            agent_x.add_states()
            agent_o.add_states()

            # records the state we are in before action
            old_state = env.hash()
            # get an action using policy
            action = agent_x.select_action()
            # performs an action
            new_state, reward, done, _ = env.step(action, agent_x.player)

            # update state values for both agents
            agent_x.update_state_values(new_state, old_state, reward[agent_x.player_number])
            agent_o.update_state_values(new_state, old_state, reward[agent_o.player_number])

            # if the game ends on X move, we don't want to make an O move
            if not done:
                # O agents turn

                # adds states for both agents
                agent_x.add_states()
                agent_o.add_states()

                # records the state we are in before action
                old_state = env.hash()
                # get an action using policy
                action = agent_o.select_action()
                # performs an action
                new_state, reward, done, _ = env.step(action, agent_o.player)

                # update state values for both agents
                agent_x.update_state_values(new_state, old_state, reward[agent_x.player_number])
                agent_o.update_state_values(new_state, old_state, reward[agent_o.player_number])

    return agent_x, agent_o


agent_x, agent_o = train(110000)


# number of games (episodes)
def test_x(episodes):
    # counters to keep track of results
    win = 0
    tie = 0
    loss = 0
    # loops for a certain number of games (episodes)
    for episode in range(episodes):
        # stops while loop when game is done
        done = False
        # resets environment when game is done
        env.reset()
        while not done:

            # adds states for X only because we are acting randomly and not updating state values for O
            agent_x.add_states()

            # always get the best action
            x_action = agent_x.select_action(epsilon=0)
            # performs an action
            new_state, reward, done, _ = env.step(x_action, agent_x.player)

            # if the game ends on X move, we don't want to make an O move
            if (not done):
                # O agents turn

                # adds states for X only because we are acting randomly and not updating state values for O
                agent_x.add_states()

                # O always makes a random action from the available actions
                o_action = random.choice(env.available_actions())
                new_state, reward, done, _ = env.step(o_action, "O")

        # record results when game is done
        if (reward == (10, -10)):
            win += 1
        elif (reward == (-10, 10)):
            loss += 1
        elif (reward == (0, 0)):
            tie += 1
    return win, loss, tie


episodes = 10000

win, loss, tie = test_x(episodes)

print("Win:", win, "Tie:", tie, "Loss:", loss)
print("Win Rate:", win/episodes*100, "Tie Rate:", tie/episodes*100, "Loss Rate:", loss/episodes*100)


# number of games (episodes)
def test_o(episodes):
    # counters to keep track of results
    win = 0
    tie = 0
    loss = 0
    # loops for a certain number of games (episodes)
    for episode in range(episodes):
        # stops while loop when game is done
        done = False
        # resets environment when game is done
        env.reset()
        while not done:

            # adds states for O only because we are acting randomly and not updating state values for X
            agent_o.add_states()

            # X always makes a random action from the available actions
            x_action = random.choice(env.available_actions())
            # performs an action
            new_state, reward, done, _ = env.step(x_action, "X")

            # if the game ends on X move, we don't want to make an O move
            if (not done):
                # O agents turn

                # adds states for O only because we are acting randomly and not updating state values for X
                agent_o.add_states()

                # always get the best action
                o_action = agent_o.select_action(epsilon=0)
                new_state, reward, done, _ = env.step(o_action, agent_o.player)

        # record results when game is done
        if (reward == (-10, 10)):
            win += 1
        elif (reward == (10, -10)):
            loss += 1
        elif (reward == (0, 0)):
            tie += 1
    return win, loss, tie


episodes = 10000

win, loss, tie = test_o(episodes)

print("Win:", win, "Tie:", tie, "Loss:", loss)
print("Win Rate:", win/episodes*100, "Tie Rate:", tie/episodes*100, "Loss Rate:", loss/episodes*100)


# number of games (episodes)
def test(episodes):
    # counters to keep track of results
    x_win = 0
    o_win = 0
    tie = 0
    # loops for a certain number of games (episodes)
    for episode in range(episodes):
        # stops while loop when game is done
        done = False
        # resets environment when game is done
        env.reset()
        while not done:

            # adds states for both agents because we are using select_action on both
            agent_x.add_states()
            agent_o.add_states()

            # always get the best action
            x_action = agent_x.select_action(epsilon=0)
            # performs an action
            new_state, reward, done, _ = env.step(x_action, "X")

            # if the game ends on X move, we don't want to make an O move
            if (not done):
                # O agents turn

                # adds states for both agents because we are using select_action on both
                agent_x.add_states()
                agent_o.add_states()

                # always get the best action
                o_action = agent_o.select_action(epsilon=0)
                new_state, reward, done, _ = env.step(o_action, "O")

        # record results when game is done
        if (reward == (-10, 10)):
            o_win += 1
        elif (reward == (10, -10)):
            x_win += 1
        elif (reward == (0, 0)):
            tie += 1
    return x_win, o_win, tie

episodes = 10000

x_win, o_win, tie = test(episodes)

print("X Win:", x_win, "Tie:", tie, "O Win:", o_win)
print("X Win Rate:", x_win/episodes*100, "Tie Rate:", tie/episodes*100, "O Win Rate:", o_win/episodes*100)

# PLAYING AS X

# number of games (episodes)
def play_as_x(episodes=1):
    # counters to keep track of results
    x_win = 0
    o_win = 0
    tie = 0
    # loops for a certain number of games (episodes)
    for episode in range(episodes):
        # stops while loop when game is done
        done = False
        # resets environment when game is done
        env.reset()
        while not done:

            # print the environment before you go
            env.render()
            # print available actions
            print(env.available_actions())

            # adds states for O only because we are controlling X
            agent_o.add_states()

            # get user input
            x_action = int(input())
            # performs an action
            new_state, reward, done, _ = env.step(x_action, "X")

            # if the game ends on X move, we don't want to make an O move
            if (not done):
                # O agents turn

                # adds states for O only because we are controlling X
                agent_o.add_states()

                # always get the best action
                o_action = agent_o.select_action(epsilon=0)
                new_state, reward, done, _ = env.step(o_action, "O")

        env.render()
        # record results when game is done
        if (reward == (-10, 10)):
            print("You Lose")
        elif (reward == (10, -10)):
            print("You Win")
        elif (reward == (0, 0)):
            print("Tie")


play_as_x()


# PLAYING AS O
# number of games (episodes)
def play_as_o(episodes=1):
    # counters to keep track of results
    x_win = 0
    o_win = 0
    tie = 0
    # loops for a certain number of games (episodes)
    for episode in range(episodes):
        # stops while loop when game is done
        done = False
        # resets environment when game is done
        env.reset()
        while not done:

            # adds states for X only because we are controlling O
            agent_x.add_states()

            # always get the best action
            x_action = agent_x.select_action(epsilon=0)
            # performs an action
            new_state, reward, done, _ = env.step(x_action, "X")

            # if the game ends on X move, we don't want to make an O move
            if (not done):
                # O agents turn

                # print the environment before you go
                env.render()
                # print available actions
                print(env.available_actions())

                # adds states for X only because we are controlling O
                agent_x.add_states()

                # get user input
                o_action = int(input())
                new_state, reward, done, _ = env.step(o_action, "O")

        env.render()
        # record results when game is done
        if (reward == (-10, 10)):
            print("You Win")
        elif (reward == (10, -10)):
            print("You Lose")
        elif (reward == (0, 0)):
            print("Tie")


play_as_o()


def train_o_against_random(episodes):
    # create a single O agent
    agent_o = Agent(env, "O")

    for episode in range(episodes):

        # set the done variable to false
        done = False

        # reset the environemnt
        env.reset()

        while not done:

            # adds states for the O agent
            agent_o.add_states()

            # record the state we are in before action
            old_state = env.hash()
            # get an random action from the list of available actions (Hint: test_o function)
            action = random.choice(env.available_actions())
            # perform an action using the step function
            new_state, reward, done, _ = env.step(action, "X")

            # update state values for O agent
            agent_o.update_state_values(new_state, old_state, reward[agent_o.player_number])

            if not done:

                # adds states for the O agent
                agent_o.add_states()

                # record the state we are in before action
                old_state = env.hash()
                # have the o_agent select an action
                action = agent_o.select_action()
                # perform an action using the step function
                new_state, reward, done, _ = env.step(action, agent_o.player)

                # update state values for O agent
                agent_o.update_state_values(new_state, old_state, reward[agent_o.player_number])

    return agent_o


agent_o = train_o_against_random(110000)

episodes = 10000

win, loss, tie = test_o(episodes)

print("Win:", win, "Tie:", tie, "Loss:", loss)
print("Win Rate:", win/episodes*100, "Tie Rate:", tie/episodes*100, "Loss Rate:", loss/episodes*100)
