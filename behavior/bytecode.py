# Задача: Обеспечить поведению гибкость данных, декодируемых 
# в виде инструкций для виртуальной машины.
from functools import wraps
from enum import IntEnum

class Entity:
    def __init__(self, health=10, wisdom=1, agility=1):
        self.health = health
        self.wisdom = wisdom
        self.agility = agility


class World:
    def __init__(self):
        self.map = None
        self.entitys = [Entity(), Entity()]

    def catch_if_not_exist(func):
        # assert 'ent_id' in func.__code__.co_varnames
        @wraps(func)
        def wrap(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except IndexError:
                print('Entity ID not exist, return -1')
                return -1
        return wrap

    @catch_if_not_exist
    def setHealth(self, ent_id, amount):
        self.entitys[ent_id].health = amount
        print('Set health of entity {0} to {1}'.format(ent_id, amount))

    @catch_if_not_exist
    def setWisdom(self, ent_id, amount):
        self.entitys[ent_id].wisdom = amount
        print('Set wisdom of entity {0} to {1}'.format(ent_id, amount))

    @catch_if_not_exist
    def setAgility(self, ent_id, amount):
        self.entitys[ent_id].agility = amount
        print('Set agility of entity {0} to {1}'.format(ent_id, amount))

    @catch_if_not_exist
    def getHealth(self, ent_id):
        return self.entitys[ent_id].health

    @catch_if_not_exist
    def getWisdom(self, ent_id):
        return self.entitys[ent_id].wisdom

    @catch_if_not_exist
    def getAgility(self, ent_id):
        return self.entitys[ent_id].agility

    def play_sound(self, num):
        print('Plays sound: {0}'.format(num))

    def spawn_particles(self, num):
        print('Spawn particles: {0}'.format(num))


class VM:
    MAX_STACK = 100

    class Instruction(IntEnum):
        INST_SET_HEALTH = 0x00,
        INST_SET_WISDOM = 0x01,
        INST_SET_AGILITY = 0x02,
        INST_GET_HEALTH = 0x03,
        INST_GET_WISDOM = 0x04,
        INST_GET_AGILITY = 0x05,
        INST_PLAY_SOUND = 0x06,
        INST_SPAWN_PARTICLES = 0x07,
        INST_LITERAL = 0x08

    def __init__(self):
        self.Functions = {
            self.Instruction.INST_SET_HEALTH: self.set_health,
            self.Instruction.INST_SET_WISDOM: self.set_wisdom,
            self.Instruction.INST_SET_AGILITY: self.set_agility,
            self.Instruction.INST_GET_HEALTH: self.get_health,
            self.Instruction.INST_GET_WISDOM: self.get_wisdom,
            self.Instruction.INST_GET_AGILITY: self.get_agility,
            self.Instruction.INST_PLAY_SOUND: self.play_sound,
            self.Instruction.INST_SPAWN_PARTICLES: self.spawn_particles,
            self.Instruction.INST_LITERAL: self.literal
        }
        self.world = World()
        self.stack = []
        self.cur_byte = 0
        self.bytecode = None

    def set_health(self):
        amount = self.__pop()
        ent_id = self.__pop()
        self.world.setHealth(ent_id, amount)

    def set_wisdom(self):
        amount = self.__pop()
        ent_id = self.__pop()
        self.world.setWisdom(ent_id, amount)

    def set_agility(self):
        amount = self.__pop()
        ent_id = self.__pop()
        self.world.setAgility(ent_id, amount)

    def get_health(self):
        ent_id = self.__pop()
        self.__push(self.world.getHealth(ent_id))

    def get_wisdom(self):
        ent_id = self.__pop()
        self.__push(self.world.getWisdom(ent_id))

    def get_agility(self):
        ent_id = self.__pop()
        self.__push(self.world.getAgility(ent_id))

    def play_sound(self):
        num = self.__pop()
        self.world.play_sound(num)

    def spawn_particles(self):
        num = self.__pop()
        self.world.spawn_particles(num)

    def literal(self):
        self.cur_byte += 1
        self.__push(self.bytecode[self.cur_byte])

    def no_op(self):
        print('Miss instruction for this')

    def __push(self, value):
        assert len(self.stack) < self.MAX_STACK, 'Stack is full'
        self.stack.append(value)

    def __pop(self):
        assert len(self.stack) > 0, 'Stack is empty'
        return self.stack.pop()

    def interpret(self, bytecode):
        self.cur_byte = 0
        self.bytecode = bytecode
        while self.cur_byte < len(bytecode):
            func = self.Functions.get(bytecode[self.cur_byte], self.no_op)
            print('execute ', func.__name__)
            func()
            print(self.stack)
            self.cur_byte += 1


if __name__ == '__main__':
    vm = VM()
    with open('test.bc', 'rb') as f:
        code = f.read()
    vm.interpret(code)


def test_1():
    world = World()
    world.setHealth(1, 5)
    assert world.getHealth(1) == 5


def test_2():
    world = World()
    world.setHealth(2, 3)
    assert world.getHealth(2) == -1