# Ключевой мыслью шаблона прототип является создание
# объекта, который может порождать объекты, похожие на себя

class Spawner:
    def __init__(self, prot):
        self.prototype = prot

    def spawnMonster(self):
        return self.prototype()

class GhostPrototype:
    num = 0
    def __init__(self):
        self.health = 20
        self.speed = 3
        self.__class__.num += 1
        print("spawn {} monster".format(self.__class__.num))

if __name__ == '__main__':
    ghostSpawner = Spawner(GhostPrototype)
    ghostSpawner.spawnMonster()
    ghostSpawner.spawnMonster()
    ghostSpawner.spawnMonster()