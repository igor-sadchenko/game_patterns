# Задача: Симуляция коллекции независимых объектов с помощью указания
# каждому объекту обработки одного кадра поведения за раз

class World:
    def __init__(self):
        self.entities = []

    def gameLoop(self):
        # Обработка ввода

        # Обновление каждой Entity
        for entity in self.entities:
            entity.update()

        # Физика и рендеринг

class Entity:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        raise NotImplemented

class Skeleton(Entity):
    def __init__(self):
        super().__init__()
        self.patrol_left = False

    def update(self):
        if self.patrol_left:
            self.x -= 1
            if self.x == 0: 
                self.patrol_left = False
        else:
            self.x += 1
            if self.x == 100:
                self.patrol_left = True

if __name__ == '__main__':
    world = World()
    world.entities.append(Skeleton())
    world.entities.append(Skeleton())

    world.gameLoop()
    world.gameLoop()