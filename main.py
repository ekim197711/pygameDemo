import pygame

from gameobject.cloud_mover import CloudMover
from gameobject.face_collision import FaceCollision
from gameobject.face_spawner import FaceSpawner
from gameobject.gameobject import GameObject
from gameobject.jukebox import JukeBox
from gameobject.score import Score


def run_game():
    FRAMES_PER_SECOND = 60
    WIDTH = 1200
    HEIGHT = 1000

    pygame.init()
    logo = pygame.image.load("assets\MikesAnsigt32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Mikes game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True

    gameobjects = {}
    gameobjects["cloud"] = GameObject("assets\\cloud497x235.png", (WIDTH * 0.2, HEIGHT * 0.1), (0, 70))
    gameobjects["cousin"] = GameObject("assets\\cusion735x208.png", (WIDTH * 0.2, HEIGHT * 0.05),
                                       (WIDTH / 2, HEIGHT - 100))
    gameobjects["cousin"].velocity = (5, 5)

    cloud_mover = CloudMover(gameobjects["cloud"], WIDTH, screen)

    jukebox = JukeBox()
    jukebox.play_game_start()

    face_spawner = FaceSpawner(screen, gameobjects["cloud"], jukebox)
    score = Score()

    face_collision = FaceCollision(face_spawner, gameobjects["cousin"], score, jukebox, HEIGHT)
    while running:
        clock.tick(FRAMES_PER_SECOND)
        cloud_mover.move()
        screen.fill((0, 0, 0))
        for key, gameobj in gameobjects.items():
            gameobj.draw(screen)
        face_spawner.maybe_spawn()
        score.draw(screen)
        pygame.display.flip()
        face_collision.check_for_collision()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            gameobjects["cousin"].move(-1, 0)
        if keys[pygame.K_RIGHT]:
            gameobjects["cousin"].move(+1, 0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left")
                    # gameobjects["cousin"].move(-1, 0)

                if event.key == pygame.K_RIGHT:
                    print("right")
                    # gameobjects["cousin"].move(1, 0)

            if event.type == pygame.QUIT:
                running = False
                jukebox.play_game_end()


if __name__ == '__main__':
    run_game()
