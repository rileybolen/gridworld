from World import World
from Agent import Agent

world = World()
agent = Agent(world)

for e in range(5000):
    done = False
    result = 0
    while not done:
        done, result = agent.act()
    agent.update_policy(result)
    agent.reset()
    #
    # if result > 0:
    #     print("Agent has won :)")
    # else:
    #     print("Agent has lost :(")

agent.display_policy()