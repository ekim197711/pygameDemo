import pygame
from pygame.rect import Rect


class GameObject:
    image = None
    position = (0, 0)
    velocity = (1, 1)

    def __init__(self, _image, _scale, _position):
        self.image = pygame.image.load(_image)
        self.image = pygame.transform.scale(self.image, _scale)
        self.position = _position

    def move(self, x: int, y: int):
        self.position = (self.position[0] + x*self.velocity[0], self.position[1] + y*self.velocity[1])

    def draw(self, screen):
        screen.blit(self.image, self.position)
