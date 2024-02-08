import pygame

class Renderer:
    def __init__(self, screen, asset_manager):
        self.screen = screen
        self.asset_manager = asset_manager

    def draw_map(self, tile_map, t_width, t_height, s_origin_x, s_origin_y, m_side):
        for m_x in range(m_side):
            for m_y in range(m_side):
                tile = tile_map[m_x][m_y]
                s_x = (m_x - m_y) * t_width // 2 + s_origin_x
                s_y = (m_x + m_y) * t_height // 2 + s_origin_y
                self.screen.blit(tile, (s_x, s_y))

    def draw_character(self, sprite, char_x, char_y):
        self.screen.blit(sprite, (char_x, char_y))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def clear_screen(self):
        self.clear()
