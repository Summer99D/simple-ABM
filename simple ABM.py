##the packages we need to install:
    
import random
import numpy as np
import matplotlib.pyplot as plt
##the package for cmap: 
import matplotlib.colors as mcolors
import time


## first we should create the agent
class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
##I asked GPT how to define their next destination
    def move(self, empty_spots):
        destination = random.choice(empty_spots)
        self.x, self.y = destination

##now the world!!!
class World:
    def __init__(self, width, height, agent_count):
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height))
        self.agents = []
        for i in range(agent_count):
            x, y = self.get_random_empty_spots()
            agent = Agent(i, x, y)
            self.agents.append(agent)
            self.grid[x, y] = 1  # Mark the agent's position on the grid

    def get_random_empty_spots(self):
        empty_spots = list(zip(*np.where(self.grid == 0)))
        return random.choice(empty_spots)

    def move_agents(self):
        for agent in self.agents:
            self.grid[agent.x, agent.y] = 0  # Clear the current position
            empty_spots = list(zip(*np.where(self.grid == 0)))
            agent.move(empty_spots)
            self.grid[agent.x, agent.y] = 1  # Mark the new position
### I was looking at all the possible ways they can move and this is what I found:
    ##interpolations = [
    #'none', 'nearest', 'bilinear', 'bicubic',
    #'spline16', 'spline36', 'hanning', 'hamming',
  #  'hermite', 'kaiser', 'quadric', 'catrom',
   # 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

    def display(self, cmap):
        plt.imshow(self.grid, cmap=cmap, interpolation='catrom')
        plt.draw()
        plt.pause(1)  # Pause for a second to see the change

# Define custom colormap: empty patches as white, agents as blue
colors = ['green', 'pink']
cmap = mcolors.ListedColormap(colors) #in order to run this I need a new package


world = World(6, 6, 20)
world.display(cmap)


for _ in range(6):
    world.move_agents()
    world.display(cmap)
    
    
##THIS is soooo cool but I think it owuld have been better if dedicated more time to learning it