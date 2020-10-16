
from cell import Cell
EMPTY_STR = '.'

class World:
    """Represents the entire world, which is a grid of cells."""

    def __init__(self, width: int, height: int):
        self._cells = [
            [
                Cell(x, y)
                for y in range(height)
            ]
            for x in range(width)
        ]
        self.width = width
        self.height = height

    def get_cell(self, x: int, y: int, dx: int = 0, dy: int = 0) -> Cell:
        cell_x = (x + dx) % self.width
        cell_y = (y + dy) % self.height
        return self._cells[cell_x][cell_y]

    def update(self) -> None:
        for x in range(self.width):
            for y in range(self.height):
                cell = self.get_cell(x, y)
                if not cell.entity:
                    continue

                cell.entity.update(self)

    def stats(self):
        stats = {
            'Tree': 0,
            'Deer': 0,
            'Lion': 0
        }

        for each in self._cells:
            for it in each:
                if it.entity:
                    stats[type(it.entity).__name__] += 1

        return dict(stats)

    def render(self):
        """Renders the world."""
        for y in range(self.height):
            for x in range(self.width):
                cell = self.get_cell(x, y)

                if cell.entity is None:
                    print(EMPTY_STR, end="")
                    continue
                cell.entity.render()

            print("")

        print("")
        print("Trees:{Tree}, Deer:{Deer}, Lions:{Lion}".format(**self.stats()))

