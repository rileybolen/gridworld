class World:

    def __init__(self):
        self.grid = [
            #0  1  2  3  4  5
            [1, 1, 1, 1, 1, 1],#0
            [1, 0, 0, 0, 0, 1],#1
            [1, 0, 1, 0, 0, 1],#2
            [1, 0, 0, 0, 0, 1],#3
            [1, 1, 1, 1, 1, 1]#4
        ]
        self.rewards = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

    def actions(self, position):
        grid = self.grid
        available = []
        if not grid[position[0] - 1][position[1]]:
            available.append([-1, 0])
        if not grid[position[0] + 1][position[1]]:
            available.append([1, 0])
        if not grid[position[0]][position[1] - 1]:
            available.append([0, -1])
        if not grid[position[0]][position[1] + 1]:
            available.append([0, 1])
        return available

    def move(self, position, action):
        newPosition = [position[0] + action[0], position[1] + action[1]]
        print("Agent moves to {0}".format(newPosition))
        return newPosition, self.rewards[newPosition[0]][newPosition[1]]
