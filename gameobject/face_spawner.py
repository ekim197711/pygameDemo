from gameobject.gameobject import GameObject


class FaceSpawner:
    screen = None
    faces = []
    frequency = 200
    count_down = frequency
    cloud = None
    jukebox = None

    def __init__(self, screen, cloud, jukebox):
        self.screen = screen
        self.cloud = cloud
        self.jukebox = jukebox

    def maybe_spawn(self):
        self.count_down -= 1
        if self.count_down <= 0:
            self.count_down = self.frequency
            self.faces.append(GameObject("assets\\MikesAnsigt.png", (50, 50), self.cloud.position))
            self.jukebox.play_spawn()
        else:
            self.count_down -= 1
        self.move_all()

    def move_all(self):
        for face in self.faces:
            face.move(0, 2)
            face.draw(self.screen)

    def destroy_face(self, face):
        self.faces.remove(face)
