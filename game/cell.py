import pygame

from game.organism import Organism


class Cell(pygame.Rect):
    def __init__(self, width: int, x: int = 0, y: int = 0, color_alive: pygame.Color = pygame.Color('red'),
                 color_dead: pygame.Color = pygame.Color('forestgreen'),
                 border_width_alive: int = 0, border_width_dead: int = 1, state: bool = False):
        super().__init__((x, y), (width, width))

        self.color_dead = color_dead
        self.color_alive = color_alive
        self.border_width_dead = border_width_dead
        self.border_width_alive = border_width_alive
        self.organism = Organism(state)

    def draw(self, surface: pygame.surface.Surface):
        color = self.color_alive if self.organism.is_alive else self.color_dead
        border_width = self.border_width_alive if self.organism.is_alive else self.border_width_dead

        pygame.draw.rect(surface=surface, color=color, rect=self, width=border_width)