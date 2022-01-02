import pygame

from gameobject.face_spawner import FaceSpawner
from gameobject.gameobject import GameObject
from gameobject.jukebox import JukeBox
from gameobject.score import Score


class FaceCollision:
    face_spawner: FaceSpawner
    cushion: GameObject
    score: Score
    jukebox: JukeBox
    screenheight: int

    def __init__(self, _face_spawner, _cushion, _score, _jukebox, _screenheight):
        self.face_spawner = _face_spawner
        self.cushion = _cushion
        self.score = _score
        self.jukebox = _jukebox
        self.screenheight = _screenheight

    def check_for_collision(self):
        for face in self.face_spawner.faces:
            facerect = pygame.Rect(face.position[0], face.position[1], face.image.get_width(), face.image.get_height())
            cousinrect = pygame.Rect(self.cushion.position[0], self.cushion.position[1], self.cushion.image.get_width(),
                                     self.cushion.image.get_height())

            if face.position[1] >= self.screenheight:
                self.jukebox.play_not_good()
                self.score.value -= 2;
                self.face_spawner.destroy_face(face)
            elif (facerect.colliderect(cousinrect)):
                self.jukebox.play_good()
                self.score.value += 10;
                self.face_spawner.destroy_face(face)
