import pygame


def main():
    print("My game begins")

    FRAMES_PER_SECOND = 60
    WIDTH = 900
    HEIGHT = 800

    pygame.init()
    logo = pygame.image.load("assets\MikesAnsigt32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Demo game 2 - Let us see what we will make")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_is_running = True

    font = pygame.font.SysFont("Times New Roman", 64)
    text = font.render("Hello there", 1, (255, 100, 200))
    text_position = (0,0)
    mike_position = (WIDTH/2,HEIGHT/2)
    mikes_face = pygame.image.load("assets\MikesAnsigt.png")

    pygame.mixer.init()
    snd_cork = pygame.mixer.Sound('assets\FOODGware_Champagne.wav')
    snd_firecracker = pygame.mixer.Sound('assets\\FRWKRec_Firecracker.wav')
    snd_bell = pygame.mixer.Sound('assets\\BELLHand_Bell_bike_5.wav')

    while game_is_running:
        clock.tick(FRAMES_PER_SECOND)

        screen.fill((255, 255, 255))
        screen.blit(text, text_position)
        screen.blit(mikes_face, mike_position)
        pygame.display.flip()
        # text_position = (text_position[0]+1, text_position[1]+1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mike_position = (mike_position[0] -2, mike_position[1])
        elif keys[pygame.K_RIGHT]:
            mike_position = (mike_position[0] + 2, mike_position[1])

        if keys[pygame.K_UP]:
            mike_position = (mike_position[0], mike_position[1]-2)
        elif keys[pygame.K_DOWN]:
            mike_position = (mike_position[0], mike_position[1]+2)

        rect_mike = pygame.Rect(mike_position[0], mike_position[1], mikes_face.get_width(), mikes_face.get_height())
        rect_text = pygame.Rect(text_position[0], text_position[1], text.get_width(), text.get_height())
        if rect_mike.colliderect(rect_text):
            text = font.render("HEY YOU JUST COLLIDED WITH ME!!!", 1, (255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    text = font.render("You pressed Three COOL!", 1, (50, 200, 200))
                if event.key == pygame.K_1:
                    text = font.render("Have a nice day!", 1, (0, 0, 200))
                if event.key == pygame.K_2:
                    text = font.render("Good bye!", 1, (200, 0, 0))
                if event.key == pygame.K_q:
                    game_is_running = False
                if event.key == pygame.K_UP:
                    snd_cork.play()
                if event.key == pygame.K_DOWN:
                    snd_firecracker.play()
                if event.key == pygame.K_LEFT:
                    snd_bell.play()
            if event.type == pygame.QUIT:
                game_is_running = False


    print("My game ends")




if __name__ == '__main__':
    main()





