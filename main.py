import pygame

from gameobject.game_object import game_object


def run_game():
    pygame.init()
    logo = pygame.image.load("assets\MikesAnsigt32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Mikes game")
    WIDTH=1000
    HEIGHT=1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    clock = pygame.time.Clock()
    FRAMES_PER_SECOND = 60
    gameobjects = {}
    gameobjects["cloud"] = game_object("assets\\cloud497x235.png", (WIDTH*0.2, HEIGHT*0.1), (0, 0))
    gameobjects["cousin"] = game_object("assets\\cusion735x208.png", (WIDTH*0.2, HEIGHT*0.05), (WIDTH/2, HEIGHT-100))

    while running:
        clock.tick(FRAMES_PER_SECOND)
        screen.fill((0, 0, 0))
        for key, gameobj in gameobjects.items():
            gameobj.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            # if event.type == pygame.KEYUP:

            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    run_game()