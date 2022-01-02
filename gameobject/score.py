import pygame


class Score:
    value = 0
    font = None
    scoreText = ""

    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont("Times New Roman", 54)
        self.scoreText = self.font.render("Score: 0", 1, (255, 255, 0))

    def faceCaptured(self):
        self.value += 1

    def draw(self, screen):
        self.scoreText = self.font.render("Score: " + str(self.value), 1, (255, 255, 0))
        screen.blit(self.scoreText, (10, 10))
