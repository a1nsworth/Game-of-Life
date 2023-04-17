import copy

import pygame

from game.cell import Cell

CELL_SIZE = 30
BORDER_WIDTH = 1


class GameField:
    def __init__(self, surface: pygame.surface.Surface):
        self.__surface = surface
        self.current_field = self.__make_base_map()
        self.next_field = self.__make_base_map()

    def __make_base_map(self):
        return [[Cell(width=CELL_SIZE, color_alive=pygame.Color('red'), color_dead=pygame.Color('forestgreen'),
                      border_width_alive=0, border_width_dead=BORDER_WIDTH) for y in
                 range(self.__surface.get_height() // CELL_SIZE)] for x in
                range(self.__surface.get_width() // CELL_SIZE)]

    def __draw_map(self):
        for i, row in enumerate(self.current_field):
            for j, cell in enumerate(row):
                cell.topleft = (i * CELL_SIZE, j * CELL_SIZE)
                cell.draw(self.__surface)

    @staticmethod
    def deepcopy(source: list[list[Cell]], other: list[list[Cell]]):
        for i, row in enumerate(source):
            for j, cell in enumerate(row):
                source[i][j] = other[i][j]

    def find_collide_cell(self, position: tuple[int, int]):
        for i, row in enumerate(self.current_field):
            for j, cell in enumerate(row):
                if cell.collidepoint(position):
                    return cell, (i, j)
        return None

    def left(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x - 1][y].organism.is_alive

    def right(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x + 1][y].organism.is_alive

    def down(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x][y + 1].organism.is_alive

    def up(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x][y - 1].organism.is_alive

    def left_up(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x - 1][y - 1].organism.is_alive

    def left_down(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x - 1][y + 1].organism.is_alive

    def right_up(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x + 1][y - 1].organism.is_alive

    def right_down(self, position: tuple[int, int]):
        x, y = position
        return self.current_field[x + 1][y + 1].organism.is_alive

    def count_neighbors(self, position: tuple[int, int]):
        n, m = len(self.current_field) - 1, len(self.current_field[0]) - 1

        if position == (0, 0):
            count = self.right(position) + self.down(position) + self.right_down(position)
        elif position == (n, m):
            count = self.up(position) + self.left(position) + self.left_up(position)
        elif position == (0, m):
            count = self.up(position) + self.right(position) + self.right_up(position)
        elif position == (n, 0):
            count = self.left(position) + self.down(position) + self.left_down(position)
        else:
            if position[0] == 0:
                count = self.right(position) + self.up(position) + self.right_up(position) + self.right_down(
                    position) + self.down(position)
            elif position[0] == n:
                count = self.up(position) + self.down(position) + self.left(position) + self.left_down(
                    position) + self.left_up(position)
            elif position[1] == 0:
                count = self.left(position) + self.right(position) + self.down(position) + self.left_down(
                    position) + self.right_down(position)
            elif position[1] == m:
                count = self.left(position) + self.right(position) + self.up(position) + self.left_up(
                    position) + self.right_up(position)
            else:
                count = self.left(position) + self.right(position) + self.up(position) + self.down(
                    position) + self.left_up(position) + self.left_down(position) + self.right_up(
                    position) + self.right_down(position)

        return count

    def update(self):
        self.deepcopy(self.current_field, self.next_field)

    def render(self):
        self.__draw_map()
