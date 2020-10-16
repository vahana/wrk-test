import random
import time
from os import system

from tree import Tree
from animal import Deer, Lion
from world import World

NUM_ITERATIONS = 500
NUM_TREES = 200
NUM_DEERS = 20
NUM_LIONS = 10
SLEEP_TIME = 0.2

WIDTH = 80
HEIGHT = 40

def populate(world, entity_type, size):
    for i in range(size):
        x = random.randrange(world.width)
        y = random.randrange(world.height)
        cell = world.get_cell(x, y)

        if cell.entity is None:
            cell.entity = entity_type(x, y)


def main():
    width = WIDTH
    height = HEIGHT

    w = World(width=width, height=height)

    populate(w, Tree, NUM_TREES)
    populate(w, Deer, NUM_DEERS)
    populate(w, Lion, NUM_LIONS)

    for i in range(NUM_ITERATIONS):
        w.update()
        w.render()
        time.sleep(SLEEP_TIME)


main()
