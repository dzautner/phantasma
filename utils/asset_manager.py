import os
import pygame

class AssetNamespace:
    def __init__(self, base_path):
        self._base_path = base_path
        self._loaded_sprites = {}

    def __getattr__(self, item):
        new_path = os.path.join(self._base_path, item)
        if os.path.isdir(new_path):
            return AssetNamespace(new_path)  # Return a new namespace for the directory
        else:
            # Try to load the sprite, assuming it is a file
            return self._load_sprite(item)

    def _load_sprite(self, name):
        # Here we assume that the sprite's file extension is .png
        # This could be adapted to support multiple file types
        file_path = f"{self._base_path}/{name}.png"
        if file_path in self._loaded_sprites:
            return self._loaded_sprites[file_path]
        if os.path.isfile(file_path):
            sprite = pygame.image.load(file_path).convert_alpha()
            self._loaded_sprites[file_path] = sprite
            return sprite
        else:
            raise AttributeError(f"No such sprite: {name}")

class AssetManager(AssetNamespace):
    def __init__(self, base_path):
        super().__init__(base_path)