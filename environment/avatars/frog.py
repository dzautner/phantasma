import pygame

class FrogAvatar:
    def __init__(self, asset_manager):
        self.sprites = self.load_sprites(asset_manager)

    def load_sprites(self, asset_manager):
        """Loads all frog-related sprites using the asset_manager."""
        # Correctly prefix the sprite names with 'frog_' to match the filenames
        sprites = {
            "back": [getattr(asset_manager.frog, f'frog_back_{i}') for i in range(9)],
            "front": [getattr(asset_manager.frog, f'frog_front_{i}') for i in range(14) if i != 4],  # Assuming 0-13, skipping 4
            "back_mirror": [getattr(asset_manager.frog, f'frog_back_mirrored_{i}') for i in range(9)],
            "front_mirror": [getattr(asset_manager.frog, f'frog_front_mirrored_{i}') for i in range(14) if i != 4]
        }
        return sprites

    def get_sprite(self, direction, frame):
        """Returns the correct sprite for the given direction and animation frame."""
        return self.sprites[direction][frame]

    def get_animation_length(self, direction):
        """Returns the number of frames in the animation for a given direction."""
        return len(self.sprites[direction])
