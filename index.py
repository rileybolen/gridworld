from World import World
from Agent import Agent

world = World()
agent = Agent(world)

done = False
result = 0

while not done:
    done, result = agent.act()

if result > 0:
    print("Agent has won :)")
else:
    print("Agent has lost :(")