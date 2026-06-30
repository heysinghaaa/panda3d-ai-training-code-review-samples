"""Intentionally flawed input handling snippet for review."""


class InputState:
    def __init__(self, base):
        self.base = base
        self.keys = {}
        self.base.accept("w", self.keys.update({"forward": True}))
        self.base.accept("w-up", self.keys.update({"forward": False}))

    def is_forward_pressed(self):
        return self.keys["forward"]

