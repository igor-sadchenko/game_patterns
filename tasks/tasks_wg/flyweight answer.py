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

        x = randint(0, WIDTH - 1)
        for y in range(HEIGHT):
            self.tiles[y][x] = self.riverTerrain


if __name__ == '__main__':
    world = World()
    world.generate_terrain()
    pprint(world.tiles)
