"""Corrected version showing frame-rate independent movement."""


class PlayerController:
    def __init__(self, camera, clock):
        self.camera = camera
        self.clock = clock
        self.speed = 12.0
        self.key_state = {"w": False, "s": False}

    def update(self, task):
        dt = self.clock.getDt()
        direction = int(self.key_state["w"]) - int(self.key_state["s"])
        self.camera.setY(self.camera.getY() + direction * self.speed * dt)
        return task.cont

