import pygame
from pygame.locals import *
from sys import exit
from utils.asset_manager import AssetManager  # Adjust the import path as needed

# Initialize AssetManager with the path to the assets folder
asset_manager = AssetManager('assets')

pygame.init()

s_height = 890
s_width = 1600

t_height = 32
t_width = t_height * 2

s_origin_x = int(s_width/2) - int(t_width/2)
s_origin_y = int(s_height/2) - int(t_height/2) - (t_height*4)

m_side = 8

screen = pygame.display.set_mode((s_width, s_height), 0, 32)
pygame.display.set_caption('Tiles Test')

hovered_tile = (None, None)

# Initialize AssetManager
asset_manager = AssetManager('assets')

grass = asset_manager.tiles.blocks_1
stone = asset_manager.tiles.blocks_38
hover_tile = asset_manager.tiles.blocks_35

tile_map = [
    [grass, grass, grass, grass, stone, stone, stone, stone],
    [grass, grass, grass, stone, stone, stone, stone, stone],
    [grass, grass, stone, stone, stone, stone, stone, stone],
    [grass, stone, stone, stone, stone, stone, stone, stone],
    [stone, stone, stone, stone, stone, stone, stone, stone],
    [stone, stone, stone, stone, stone, stone, stone, stone],
    [stone, stone, stone, stone, stone, stone, stone, stone],
    [stone, stone, stone, stone, stone, stone, stone, stone]
]

# Define the existing sprite indices for each category
existing_back_indices = range(9)  # 0 through 8
existing_front_indices = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # 4 is missing
existing_back_mirrored_indices = range(9)  # 0 through 8
existing_front_mirrored_indices = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Skipping 4 as it's missing

# Load frog sprites using the hierarchical AssetManager, with corrected indices
frog_sprites = {
    "back": [getattr(asset_manager.frog, f'frog_back_{i}') for i in existing_back_indices],
    "front": [getattr(asset_manager.frog, f'frog_front_{i}') for i in existing_front_indices],
    "back_mirror": [getattr(asset_manager.frog, f'frog_back_mirrored_{i}') for i in existing_back_mirrored_indices],
    "front_mirror": [getattr(asset_manager.frog, f'frog_front_mirrored_{i}') for i in existing_front_mirrored_indices]
}



# Filter out None sprites
for direction, sprites in frog_sprites.items():
    frog_sprites[direction] = [sprite for sprite in sprites if sprite is not None]

char_width = 64
char_height = 64
char_x = s_width // 2 - char_width // 2
char_y = s_height // 2 - char_height // 2
char_speed = 0.5
char_direction = "front"
animation_frame = 0

key_mapping = {
    K_LEFT: (-char_speed, 0, "front"),
    K_RIGHT: (char_speed, 0, "back_mirror"),
    K_UP: (0, -char_speed, "back"),
    K_DOWN: (0, char_speed, "front_mirror")
}

def update_character(keys):
    global char_x, char_y, char_direction, animation_frame

    moved = False

    for key, (dx, dy, direction) in key_mapping.items():
        if keys[key]:
            new_x = char_x + dx
            new_y = char_y + dy

            # Ensure the character stays within screen bounds
            char_x = max(0, min(s_width - char_width, new_x))
            char_y = max(0, min(s_height - char_height, new_y))
            moved = True

            if char_direction != direction:
                char_direction = direction
                animation_frame = 0
            elif moved:
                sprite_list = frog_sprites[char_direction]
                if sprite_list:
                    animation_frame = (animation_frame + 1) % len(sprite_list)
                else:
                    animation_frame = 0 

def draw_character():
    global animation_frame
    if frog_sprites[char_direction]:
        sprite_list = frog_sprites[char_direction]
        if sprite_list:
            sprite = sprite_list[animation_frame]
            screen.blit(sprite, (char_x, char_y))

def draw_map():
    screen.fill((0, 0, 0))
    hover_x, hover_y = hovered_tile
    for m_x in range(m_side):
        for m_y in range(m_side):
            s_x = (m_x - m_y) * int(t_width/2) + s_origin_x
            s_y = (m_x + m_y) * int(t_height/2) + s_origin_y
            screen.blit(tile_map[m_x][m_y], (s_x, s_y))

# Main game loop
while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    update_character(keys)
    draw_map()
    draw_character()

    pygame.display.update()
