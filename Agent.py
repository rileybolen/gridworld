import random


class Agent:

    def __init__(self, world):
        self.position = [3,1]
        self.world = world
        self.policy = {}
        self.create_initial_policy()

    def act(self):
        actions = self.world.actions(self.position)
        self.position, reward = self.world.move(self.position, self.choose_action(self.position, actions))
        if reward != 0:
            return True, reward
        else:
            return False, 0

    def create_initial_policy(self):
        for r in range(0, len(self.world.grid)):
            for c in range(0, len(self.world.grid[r])):
                if not self.world.grid[r][c]:
                    actions = self.world.actions([r,c])
                    self.policy['({0},{1})'.format(r, c)] = {}
                    for action in actions:
                        self.policy['({0},{1})'.format(r, c)]['({0},{1})'.format(action[0],action[1])] = 1 / len(actions)

    def choose_action(self, position, actions):
        action_weights = []
        for action in actions:
            action_weights.append(
                self.policy['({0},{1})'.format(position[0], position[1])]['({0},{1})'.format(action[0], action[1])])
        return random.choices(actions, weights=action_weights)[0]
