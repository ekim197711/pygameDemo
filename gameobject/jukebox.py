import pygame


class JukeBox:
    snd_cork = None
    snd_firecracker = None
    snd_bell = None
    snd_game_start = None

    def __init__(self):
        pygame.mixer.init()
        self.snd_cork = pygame.mixer.Sound('assets\\FOODGware_Champagne.wav')
        self.snd_firecracker = pygame.mixer.Sound('assets\\FRWKRec_Firecracker.wav')
        self.snd_bell = pygame.mixer.Sound('assets\\BELLHand_Bell_bike_5.wav')
        self.snd_game_start = pygame.mixer.Sound('assets\\BELLHand_Bell_bike_5.wav')

    def play_not_good(self):
        self.snd_firecracker.play()

    def play_spawn(self):
        self.snd_cork.play()

    def play_good(self):
        self.snd_bell.play()

    def play_game_start(self):
        self.snd_bell.play()

    def play_game_end(self):
        self.snd_firecracker.play()
