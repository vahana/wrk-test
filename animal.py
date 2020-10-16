import random

from life import Animal
from tree import Tree


class Deer(Animal):
    CALORIES = 30
    SPAWN_CHANCE = 0.1
    MOVE_CALORIES = 5

    def render(self):
        print('\033[93;5;10mD\033[0m', end="")
        # print('\033[93;5;10m%s\033[0m' % self.hunger, end="")

    def is_food(self, entity):
        return isinstance(entity, Tree)


class Lion(Animal):
    CALORIES = 30
    SPAWN_CHANCE = 0.1
    MOVE_CALORIES = 5

    def render(self):
        print('\033[31;5;10mL\033[0m', end="")
        # print('\033[31;5;10m%s\033[0m' % self.hunger, end="")

    def is_food(self, entity):
        return isinstance(entity, Deer)

