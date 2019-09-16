# TODO:
# 1 Упростить архитектуру World таким образом, чтобы gameLoop
# не изменялся при расширении классифирации танков.
# 2* Упростить архитектуру так, чтобы класс World не изменялся
# при добавлении новых механик.

HEAVY_TANK = 1
MEDIUM_TANK = 2


class World:
    def __init__(self):
        self.npc_tanks = []

    def gameLoop(self):
        # Обновление каждого типа танка
        for entity in self.npc_tanks:
            if entity.id_type == HEAVY_TANK:
                entity.try_push()
            elif entity.id_type == MEDIUM_TANK:
                entity.move_round()


class Entity:
    def __init__(self):
        self.x = 0
        self.y = 0


class HeavyTank(Entity):
    def __init__(self):
        super().__init__()
        self.id_type = HEAVY_TANK
        self.retreat = False

    def try_push(self):
        if self.retreat:
            self.x -= 1
            if self.x == 0: 
                self.retreat = False
        else:
            self.x += 1
            if self.x == 100:
                self.patrol_left = True


class MediumTank(Entity):
    def __init__(self):
        super().__init__()
        self.id_type = MEDIUM_TANK
        self.up = False
        self.left = False

    def move_round(self):
        if self.up:
            self.y -= 1
            if self.y == 0: 
                self.up = False
        else:
            self.y += 1
            if self.y == 100:
                self.up = True
        if self.left:
            self.x -= 1
            if self.x == 0: 
                self.left = False
        else:
            self.x += 1
            if self.x == 100:
                self.left = True


if __name__ == '__main__':
    world = World()
    world.npc_tanks.append(MediumTank())
    world.npc_tanks.append(HeavyTank())

    world.gameLoop()
    world.gameLoop()
