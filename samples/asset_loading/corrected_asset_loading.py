"""Corrected asset loading with validation and visible defaults."""

from pathlib import PurePosixPath


class SceneFactory:
    def __init__(self, loader, render, asset_root="assets"):
        self.loader = loader
        self.render = render
        self.asset_root = PurePosixPath(asset_root)

    def load_character(self, name, scale=1.0):
        if not name or PurePosixPath(name).is_absolute() or ".." in PurePosixPath(name).parts:
            raise ValueError("name must be a relative asset path")
        if scale <= 0:
            raise ValueError("scale must be positive")

        model_path = str(self.asset_root / name)
        model = self.loader.loadModel(model_path)
        if model is None:
            raise FileNotFoundError(model_path)
        model.reparentTo(self.render)
        model.setScale(scale)
        return model

