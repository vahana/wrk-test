import random

from world import World

class Life:

    SPAWN_CHANCE = 0 # chances of creating an offspring
    CALORIES = 0 # calories the life form has

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def spawn(self, world, entity):
        grow = (random.random() < self.SPAWN_CHANCE)

        if not grow:
            return

        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)

        cell = world.get_cell(self.x, self.y, dx, dy)
        if cell.entity is None:
            cell.entity = type(self)(cell.x, cell.y)

    def die(self, world):
        del world.get_cell(self.x, self.y).entity
        world.get_cell(self.x, self.y).entity = None


class Animal(Life):

    MOVE_CALORIES = 0  # calories spend for moving around
    INITIAL_HUNGER = 0 # born full ?
    MAX_HUNGER = 100 # max hunger value after which the animal has chances to die
    HUNGER_THR = 50  # hunger threshold when passed animal will try to only eat not mate
    DIYING_CHANCE = 0.01 # chances of dying of starvation


    def __init__(self, x: int, y: int, hunger=None):
        super().__init__(x,y)
        self.hunger = hunger or self.INITIAL_HUNGER
        self.sex = random.randint(0,1)

    def create_animal(self, x, y, hunger=None):
        return type(self)(x,y,hunger)

    def is_hungry(self):
        return self.hunger > 0

    def is_food(self, entity):
        pass

    def is_mate(self, entity):
        return isinstance(entity, type(self)) and self.sex != entity.sex

    def is_super_hungry(self):
        return self.hunger >= self.HUNGER_THR

    def might_die(self):
        return self.hunger >= self.MAX_HUNGER and \
                    (random.random() < self.DIYING_CHANCE)

    def next_cell(self, world):
        return world.get_cell(self.x, self.y,
                random.randint(-1, 1), random.randint(-1, 1))

    def move(self, world, cell):
        "Moves to the new cell and gets little bit hungrier"

        if not cell.entity:
            world.get_cell(self.x, self.y).entity = None
            cell.entity = self.create_animal(cell.x, cell.y,
                                min(self.hunger+self.MOVE_CALORIES, self.MAX_HUNGER))

    def eat(self, world, entity):
        self.hunger = max(self.hunger-entity.CALORIES, 0)
        entity.die(world)

    def update(self, world:World):

        if self.might_die():
            self.die(world)
            return

        new_cell = self.next_cell(world)

        if not new_cell.entity:
            self.move(world, new_cell)
            return

        if self.is_hungry() and self.is_food(new_cell.entity):
            self.eat(world, new_cell.entity)

        if self.is_mate(new_cell.entity) and not self.is_super_hungry():
            self.spawn(world, new_cell.entity)

