# TODO:
# 1. Упростить архитектуhe World, так как каждый новый класс будет вносить свои изменения.

HEAVY_TANK = 1
MEDIUM_TANK = 2

class World:
    def __init__(self):
        self.ai_entities = []

    def gameLoop(self):
        # Обработка ввода

        # Обновление каждой Entity

        for entity in self.ai_entities:
            if entity.id_type == HEAVY_TANK:
                entity.try_push()
            elif entity.id_type == MEDIUM_TANK:
                entity.move_round()

        # Физика и рендеринг

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
    world.ai_entities.append(MediumTank())
    world.ai_entities.append(HeavyTank())

    world.gameLoop()
    world.gameLoop()
