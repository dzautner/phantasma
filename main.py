import pygame
from pygame.locals import *
from sys import exit
from utils.asset_manager import AssetManager  # Adjust the import path as needed
from environment.renderer import Renderer
from environment.avatars.frog import FrogAvatar  # Import the FrogAvatar

# Initialize Pygame and AssetManager
pygame.init()
asset_manager = AssetManager('assets')

# Screen setup
s_height = 890
s_width = 1600
screen = pygame.display.set_mode((s_width, s_height), 0, 32)
pygame.display.set_caption('Tiles Test')

# Initialize Renderer and FrogAvatar
renderer = Renderer(screen, asset_manager)
frog_avatar = FrogAvatar(asset_manager)  # Initialize the FrogAvatar
# Tile setup
t_height = 32
t_width = t_height * 2
s_origin_x = int(s_width / 2) - int(t_width / 2)
s_origin_y = int(s_height / 2) - int(t_height / 2) - (t_height * 4)
m_side = 8

# Complete tile_map setup
tile_map = [
    [asset_manager.grounds.ground_grass, asset_manager.grounds.ground_grass, asset_manager.grounds.ground_grass, asset_manager.grounds.ground_grass, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt],
    [asset_manager.grounds.ground_grass, asset_manager.grounds.ground_grass, asset_manager.grounds.ground_grass, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt],
    [asset_manager.grounds.ground_grass, asset_manager.grounds.ground_grass, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt],
    [asset_manager.grounds.ground_grass, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt],
    [asset_manager.grounds.ground_asphalt_damaged, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt],
    [asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt_damaged, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt],
    [asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt],
    [asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt, asset_manager.grounds.ground_asphalt_damaged, asset_manager.grounds.ground_asphalt]
]


# Character setup
char_width = 64
char_height = 64
char_x = s_width // 2 - char_width // 2
char_y = s_height // 2 - char_height // 2
char_speed = 0.5
char_direction = "front"
animation_frame = 0

# Key mapping for character movement
key_mapping = {
    K_LEFT: (-char_speed, 0, "front"),
    K_RIGHT: (char_speed, 0, "back_mirror"),
    K_UP: (0, -char_speed, "back"),
    K_DOWN: (0, char_speed, "front_mirror")
}


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    moved = False

    for key, (dx, dy, direction) in key_mapping.items():
        if keys[key]:
            new_x = char_x + dx
            new_y = char_y + dy
            char_x = max(0, min(s_width - char_width, new_x))
            char_y = max(0, min(s_height - char_height, new_y))
            moved = True

            if char_direction != direction:
                char_direction = direction
                animation_frame = 0
            elif moved:
                animation_length = frog_avatar.get_animation_length(char_direction)
                animation_frame = (animation_frame + 1) % animation_length

    renderer.clear()
    renderer.draw_map(tile_map, t_width, t_height, s_origin_x, s_origin_y, m_side)
    sprite = frog_avatar.get_sprite(char_direction, animation_frame)
    renderer.draw_character(sprite, char_x, char_y)

    pygame.display.update()
