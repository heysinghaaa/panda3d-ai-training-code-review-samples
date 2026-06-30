"""Corrected input state registration for Panda3D event callbacks."""


class InputState:
    def __init__(self, base):
        self.base = base
        self.keys = {"forward": False}
        self.base.accept("w", self.set_key, ["forward", True])
        self.base.accept("w-up", self.set_key, ["forward", False])

    def set_key(self, key, value):
        self.keys[key] = value

    def is_forward_pressed(self):
        return self.keys.get("forward", False)

