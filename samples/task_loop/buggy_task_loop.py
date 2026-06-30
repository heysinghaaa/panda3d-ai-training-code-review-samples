"""Intentionally flawed Panda3D-style task loop snippet for review."""


class PlayerController:
    def __init__(self, camera):
        self.camera = camera
        self.speed = 12

    def update(self, task):
        if self.is_key_down("w"):
            self.camera.setY(self.camera.getY() + self.speed)
        if self.is_key_down("s"):
            self.camera.setY(self.camera.getY() - self.speed)
        return task.cont

    def is_key_down(self, key):
        return False

