# Задача: Карта 100х100, только 3 типа поверхности. Нужно написать чистый
#         и легко поддерживаемый код. Неправельный пример:

# from enum import Enum
# import random
# class Terrain(Enum):
#     TERRAIN_GRASS = 1
#     TERRAIN_HILL = 2
#     TERRAIN_RIVER = 3

# class World:

#     def __init__(self):
#         self.tiles = [[random.choice(list(Terrain)) for x in range(100)] for y in range(100)]

#     def get_move_cost(self, x, y):
#         tile = self.tiles[y][x]
#         if tile == Terrain.TERRAIN_GRASS:
#             return 1
#         if tile == Terrain.TERRAIN_HILL:
#             return 3
#         if tile == Terrain.TERRAIN_RIVER:
#             return 2

#     def is_water(self, x, y):
#         tile = self.tiles[y][x]
#         if tile == Terrain.TERRAIN_GRASS:
#             return False
#         if tile == Terrain.TERRAIN_HILL:
#             return False
#         if tile == Terrain.TERRAIN_RIVER:
#             return True
from random import randint
from pprint import pprint

WIDTH = 20
HEIGHT = 20

class Terrain:

    def __init__(self, move_cost, is_water, texture):
        self.move_cost = move_cost
        self.is_water = is_water
        self.texture = texture

    def __repr__(self):
        return self.texture

class World:

    def __init__(self):
        self.grassTerrain = Terrain(1, False, "g")
        self.hillTerrain = Terrain(3, False, "h")
        self.riverTerrain = Terrain(2, True, "r")

        self.tiles = [[None for x in range(WIDTH)] for y in range(HEIGHT)]

    def generate_terrain(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if randint(0, 9) == 0:
                    self.tiles[y][x] = self.hillTerrain
                else:
                    self.tiles[y][x] = self.grassTerrain

        x = randint(0, WIDTH-1)
        for y in range(HEIGHT):
            self.tiles[y][x] = self.riverTerrain

if __name__ == '__main__':
    world = World()
    world.generate_terrain()
    pprint(world.tiles)