class Organism:
    MAX_NEIGHBORS = 8
    MIN_NEIGHBORS = 0

    def __init__(self, state: bool = False):
        self.__number_neighbors = Organism.MIN_NEIGHBORS
        self.__is_alive: bool = state

    @property
    def number_neighbors(self):
        return self.__number_neighbors

    @number_neighbors.setter
    def number_neighbors(self, value):
        if value > Organism.MAX_NEIGHBORS:
            raise ValueError(f"{value} > MAX_NEIGHBORS = {Organism.MAX_NEIGHBORS}")
        if value < Organism.MIN_NEIGHBORS:
            raise ValueError(f"{value} < MAX_NEIGHBORS = {Organism.MIN_NEIGHBORS}")

        self.__number_neighbors = value

    @property
    def is_alive(self):
        return self.__is_alive

    def kill(self):
        self.__is_alive = False

    def resurrect(self):
        self.__is_alive = True