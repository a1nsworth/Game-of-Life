from game.game_field import GameField
from game.game_rule import GameRule


class GameEngine:
    def __init__(self, game_field: GameField):
        self.game_field = game_field

    def count_neighbors(self):
        for i, row in enumerate(self.game_field.current_field):
            for j, cell in enumerate(row):
                cell.organism.number_neighbors = self.game_field.count_neighbors((i, j))

    def run(self):
        self.count_neighbors()
        for row in self.game_field.current_field:
            for cell in row:
                GameRule().run(cell)
