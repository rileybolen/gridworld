import random
import operator

class Agent:

    def __init__(self, world):
        self.position = [6,1]
        self.world = world
        # self.policy = {}
        # self.create_initial_policy()

        self.expected_rewards = {}
        self.observations = {}
        self.init_expected_rewards()

        self.actions_taken = {}

    def act(self):
        actions = self.world.actions(self.position)
        self.position, reward = self.world.move(self.position, self.choose_action(self.position, actions))
        if reward == 1 or reward == -1:
            return True, reward
        else:
            return False, reward

    def choose_action(self, position, actions):
        chosen_action = random.choice(actions)
        self.record_action(position, chosen_action)
        return chosen_action

    def record_action(self, position, action):
        self.actions_taken['({0},{1}),({2},{3})'.format(position[0], position[1], action[0], action[1])] = \
                {
                    "position": '({0},{1})'.format(position[0], position[1]),
                    "action": '({0},{1})'.format(action[0], action[1]),
                }

    def update_policy(self, reward):
        for key, dict in self.actions_taken.items():
            n = self.observations[dict["position"]][dict["action"]] + 1
            mean = self.expected_rewards[dict["position"]][dict["action"]]
            self.expected_rewards[dict["position"]][dict["action"]] = (mean * ((n-1)/n)) + (reward * (1/n))
            self.observations[dict["position"]][dict["action"]] = n

    def create_initial_policy(self):
        for r in range(0, len(self.world.grid)):
            for c in range(0, len(self.world.grid[r])):
                if not self.world.grid[r][c]:
                    actions = self.world.actions([r,c])
                    self.policy['({0},{1})'.format(r, c)] = {}
                    for action in actions:
                        self.policy['({0},{1})'.format(r, c)]['({0},{1})'.format(action[0],action[1])] = 1 / len(actions)

    def init_expected_rewards(self):
        for r in range(0, len(self.world.grid)):
            for c in range(0, len(self.world.grid[r])):
                if not self.world.grid[r][c]:
                    actions = self.world.actions([r,c])
                    self.expected_rewards['({0},{1})'.format(r, c)] = {}
                    self.observations['({0},{1})'.format(r, c)] = {}
                    for action in actions:
                        self.expected_rewards['({0},{1})'.format(r, c)]['({0},{1})'.format(action[0],action[1])] = 0
                        self.observations['({0},{1})'.format(r, c)]['({0},{1})'.format(action[0], action[1])] = 0

    def reset(self):
        self.actions_taken = {}
        self.position = [3,1]

    def display_policy(self):
        print("\nBest Action")
        for r in range(0, len(self.world.grid)):
            display_row = ""
            for c in range(0, len(self.world.grid[r])):
                if not self.world.grid[r][c]:
                    if self.world.rewards[r][c] == 1:
                        display_row += " W "
                    elif self.world.rewards[r][c] == -1:
                        display_row += " F "
                    else:
                        expected_action = max(self.expected_rewards['({0},{1})'.format(r, c)].items(),
                                              key=operator.itemgetter(1))[0]
                        action_text = {"(1,0)": "D", "(-1,0)": "U", "(0,1)": "R", "(0,-1)": "L"}
                        display_row += " " + action_text[expected_action] + " "
                else:
                    display_row += "|||"
            print(display_row)
        print("\n")
        print("Expected Reward")
        for r in range(0, len(self.world.grid)):
            display_row = ""
            for c in range(0, len(self.world.grid[r])):
                if not self.world.grid[r][c]:
                    expected_action = max(self.expected_rewards['({0},{1})'.format(r, c)].items(),
                                          key=operator.itemgetter(1))[0]
                    display_row += " {:5.2f} ".format(self.expected_rewards['({0},{1})'.format(r, c)][expected_action])
                else:
                    display_row += "|||||||"
            print(display_row)


