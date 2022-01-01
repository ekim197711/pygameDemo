import pygame
from pygame.rect import Rect


class game_object:
    image = None
    position = (0, 0)
    velocity = (1, 1)

    def __init__(self, _image, _scale, _position):
        self.image = pygame.image.load(_image)
        self.image = pygame.transform.scale(self.image, _scale)
        self.position = _position

    def draw(self, screen):
        screen.blit(self.image, self.position )
