import pygame


def mygame():
    WIDTH=600
    HEIGHT=800
    FPS=60
    isPlaying=True
    pygame.init()
    logo = pygame.image.load("assets\MikesAnsigt32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("New awesome game!!!")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    img = pygame.image.load("assets\MikesAnsigt.png")
    myposition = (0,0)
    velocity = 4

    pygame.mixer.init()
    snd_cork = pygame.mixer.Sound('assets\FOODGware_Champagne.wav')
    snd_fire = pygame.mixer.Sound('assets\FRWKRec_Firecracker.wav')

    font = pygame.font.SysFont("Times New Roman", 40)
    text = font.render("Test 1 2 3", 1, (100, 200, 10))
    txt_position = (100,300)
    while(isPlaying):
        clock.tick(FPS)

        rect_mike = pygame.Rect(myposition[0], myposition[1], img.get_width(), img.get_height())
        rect_text = pygame.Rect(txt_position[0], txt_position[1], text.get_width(), text.get_height())

        if rect_mike.colliderect(rect_text):
            text = font.render("Boing ding hello trallalal!!", 1, (0, 0, 255))
        else:
            text = font.render("No collision!", 1, (255, 0, 255))

        screen.fill((200, 100, 255))
        screen.blit(img,myposition)
        screen.blit(text, txt_position)
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            myposition = (myposition[0] - velocity, myposition[1])
        elif keys[pygame.K_RIGHT]:
            myposition = (myposition[0] + velocity, myposition[1])
        if keys[pygame.K_UP]:
            myposition = (myposition[0], myposition[1] - velocity)
        elif keys[pygame.K_DOWN]:
            myposition = (myposition[0], myposition[1] + velocity)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Event triggered: QUIT!!!")
                isPlaying = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    snd_cork.play()

    print("Game has ended!!")

if __name__ == '__main__':
    mygame()

