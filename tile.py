import pygame.sprite
from pathlib import Path
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(Path('..')/'src'/'level'/'graphics'/'test'/'rock.png').convert_alpha()
        self.rect = self.image.get_rect(toplef=position)




