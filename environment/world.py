import arcade
import math

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player_sprite_list = None
        self.player = None
        self.background = None
        self.time = 0

    def setup(self):
        # Set up the game world here
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.player_sprite_list = arcade.SpriteList()

        # Load different textures for different directions
        self.player_textures = {
            "up": arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png"),
            "down": arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk1.png"),
            "left": arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk2.png"),
            "right": arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk3.png"),
        }

        # Create the player sprite
        self.player = arcade.Sprite()
        self.player.center_x = self.width / 2
        self.player.center_y = self.height / 2
        self.player.texture = self.player_textures["up"]
        self.player_sprite_list.append(self.player)

    def draw(self):
        # Draw the background
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

        # Draw the player
        self.player_sprite_list.draw()

    def update(self, delta_time):
        # Update the game world
        self.time += delta_time
        radius = 50  # Radius of the circle

        # Calculate new position in the circle
        new_x = self.width / 2 + math.cos(self.time) * radius
        new_y = self.height / 2 + math.sin(self.time) * radius

        # Determine direction based on movement
        direction = self.get_direction(new_x - self.player.center_x, new_y - self.player.center_y)
        self.player.texture = self.player_textures[direction]

        # Update player position
        self.player.center_x = new_x
        self.player.center_y = new_y

    def get_direction(self, delta_x, delta_y):
        # Determine the direction based on the deltas of x and y
        if abs(delta_x) > abs(delta_y):
            # Moving more horizontally
            return "right" if delta_x > 0 else "left"
        else:
            # Moving more vertically
            return "up" if delta_y > 0 else "down"


o