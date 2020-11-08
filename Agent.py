import random


class Agent:

    def __init__(self, world):
        self.position = [3,1]
        self.world = world

    def act(self):
        actions = self.world.actions(self.position)
        self.position, reward = self.world.move(self.position, random.choice(actions))
        if reward != 0:
            return True, reward
        else:
            return False, 0
