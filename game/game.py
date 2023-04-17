import pygame

from game.event_controller import EventController
from game.game_engine import GameEngine
from game.main_window import MainWindow

FPS = 10

WIDTH = 1500
HEIGHT = 900

BLACK = pygame.Color('black')


class Game:
    def __init__(self):
        self.__main_window = MainWindow(WIDTH, HEIGHT, BLACK)
        self.__game_engine = GameEngine(self.__main_window.game_field)

    def __update_event(self):
        EventController().run(self.__game_engine, self.__main_window)

    def __render(self):
        self.__main_window.render()

    def __update(self):
        self.__main_window.update()
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    def run(self):
        while True:
            self.__update()
            self.__render()
            self.__update_event()
