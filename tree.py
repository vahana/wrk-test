"""Defines a Tree object."""

import random

from world import World
from life import Life

class Tree(Life):
    """A Tree is an entity that just sits around and does nothing but grows slowly."""

    TREE_STR = '\033[38;5;10mT\033[0m'
    CALORIES = 10
    SPAWN_CHANCE = 0.005


    def render(self):
        print(self.TREE_STR, end="")

    def update(self, world: World):
        """Acts for this tree. Grows with a small probability."""
        self.spawn(world, self)
