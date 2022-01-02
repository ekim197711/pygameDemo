import gameobject
from gameobject.gameobject import GameObject


class CloudMover:
    cloud: GameObject
    x_direction: int = 1
    screen_width: int
    cloud_velocity = 7

    def __init__(self, _cloud: GameObject, _screen_width: int, _screen):
        self.cloud = _cloud
        self.screen_width = _screen_width
        self.screen = _screen

    def move(self):
        self.cloud.move(self.x_direction*self.cloud_velocity, 0)
        if self.x_direction > 0 and self.cloud.position[0] >= (self.screen_width - self.cloud.image.get_width()):
           self.x_direction = -1
        if self.x_direction < 0 and self.cloud.position[0] <= 0:
           self.x_direction = 1
        self.cloud.draw(self.screen)
