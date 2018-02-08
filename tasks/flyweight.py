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
