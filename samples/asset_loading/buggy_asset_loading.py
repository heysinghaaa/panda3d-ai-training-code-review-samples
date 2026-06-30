"""Intentionally flawed asset loading snippet for review."""


class SceneFactory:
    def __init__(self, loader, render):
        self.loader = loader
        self.render = render

    def load_character(self, name):
        model = self.loader.loadModel("assets/" + name)
        model.reparentTo(self.render)
        model.setScale(0)
        return model

