import pygame

from game.game_engine import GameEngine
from game.main_window import MainWindow


class EventController:
    @staticmethod
    def run(game_engine: GameEngine, window: MainWindow):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                value = window.game_field.find_collide_cell(pygame.mouse.get_pos())
                if value is not None:
                    _, position = value
                    window.game_field.next_field[position[0]][position[1]].organism.resurrect()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                game_engine.run()
