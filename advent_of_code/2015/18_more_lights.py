import numpy as np
from utils.inputs import get_data_set
get_data_set(2015,18)

class Game(object):
    def __init__(self, initial_state, broken=False):
        self._state = self.parse(initial_state)
        shape = self.state.shape
        self.x_max = shape[0] - 1
        self.y_max = shape[1] - 1
        self.broken = broken
        self._set_broken_lights()

    def _set_broken_lights(self):
        if self.broken:
            for x in (0, self.x_max):
                for y in (0, self.y_max):
                    self.state[x, y] = 1

    @property
    def state(self):
        return self._state[1:-1, 1:-1]

    @state.setter
    def state(self, new_state):
        self._state[1:-1, 1:-1] = new_state

    @staticmethod
    def parse(initial_state):
        size_x = initial_state.index("\n")
        size_y = initial_state.strip().count("\n") + 1
        state = np.zeros((size_x + 2, size_y + 2), dtype=np.uint8)
        for i, line in enumerate(initial_state.strip().split("\n")):
            for j, char in enumerate(line):
                state[i + 1, j + 1] = 0 if char == "." else 1
        return state

    def get_n_neighbours(self):
        return (self._state[0:-2, 0:-2] + self._state[0:-2, 1:-1] +
                self._state[0:-2, 2:] + self._state[1:-1, 0:-2] +
                self._state[1:-1, 2:] + self._state[2:, 0:-2] +
                self._state[2:, 1:-1] + self._state[2:, 2:])

    def step(self, n_steps=1):
        for i in range(n_steps):
            n_neighbours = self.get_n_neighbours()

            birth = (n_neighbours == 3) & (self._state[1:-1, 1:-1] == 0)
            survive = (((n_neighbours == 2) | (n_neighbours == 3)) &
                    (self._state[1:-1, 1:-1] == 1))

            self._state[...] = 0
            self._state[1:-1, 1:-1][birth | survive] = 1
            self._set_broken_lights()

    @property
    def n_lights_on(self):
        return np.sum(self.state)


with open("inputs/18_task.txt") as fin:
    game = Game(fin.read())
game.step(100)
print("{} lights on".format(game.n_lights_on))


with open("inputs/18_task.txt") as fin:
    game = Game(fin.read(), broken=True)
game.step(100)
print("{} lights on".format(game.n_lights_on))