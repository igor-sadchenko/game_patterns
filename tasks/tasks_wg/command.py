# Задача: Улучшить обработчик ввода (InputHandler) описанный ниже

BUTTON_W = 1
BUTTON_A = 2
BUTTON_S = 3
BUTTON_D = 4

BUTTON_LBM = 5
BUTTON_RBM = 6


BUTTON_PRESSED = 1

def isPressed(button):
    if button == BUTTON_PRESSED:
        return True
    return False

def moveForward():
    print('Move forward')

def moveBackward():
    print('Move backward')

def moveLeft():
    print('Move left')

def moveRight():
    print('Move right')

def shoot():
    print('Shoot the gun!!')

def setAutoTarget():
    print('Automatic targeting')

class InputHandler:

    def handle_input(self):
        if (isPressed(BUTTON_W)):
            moveForward()
        elif (isPressed(BUTTON_A)):
            moveLeft()
        elif (isPressed(BUTTON_S)):
            moveBackward()
        elif (isPressed(BUTTON_D)):
            moveRight()
        elif (isPressed(BUTTON_LBM)):
            shoot()
        elif (isPressed(BUTTON_RBM)):
            setAutoTarget()


# 1. Необходимо реализовать так, что бы можно было изменить настройки, например
#    поставить выстрел на ПКМ.
# 2* Так же нужно добавить возможность передавать в метод параметр(ы) 
# 3* Для возможности реализовать реплеи, необходимо реализовать "отменяемые" методы перемещения.
#    Для примера дан класс Unit.

### Реализация 1 ###


class InputHandler_1:

    def __init__(self):
        self.button_w = moveForward
        self.button_a = moveLeft
        self.button_s = moveBackward
        self.button_d = moveRight
        self.button_lbm = shoot
        self.button_rbm = setAutoTarget

    def handle_input(self):
        if (isPressed(BUTTON_W)):
            self.button_w()
        elif (isPressed(BUTTON_A)):
            self.button_a()
        elif (isPressed(BUTTON_S)):
            self.button_s()
        elif (isPressed(BUTTON_D)):
            self.button_d()
        elif (isPressed(BUTTON_LBM)):
            self.button_lbm()
        elif (isPressed(BUTTON_RBM)):
            self.button_rbm()


def example_1():
    inputHandler = InputHandler_1()

    inputHandler.handle_input()

### Реализация 2 ###


def moveRight_(unit):
    unit.moveRight()


class Unit1:
    def moveRight(self):
        print('Run unit.moveRight()')


class InputHandler_2:

    def __init__(self):
        self.button_d = moveRight_

    def handle_input(self):
        if (isPressed(BUTTON_D)):
            return self.button_d

def example_2():
    unit = Unit1()
    inputHandler = InputHandler_2()

    command = inputHandler.handle_input()
    if command:
        command(unit)

### Реализация 3 ###


class MoveCommand:
    def __init__(self, unit, x, y):
        self.unit = unit
        self.x_before = 0
        self.y_before = 0
        self.x_ = x
        self.y_ = y

    def execute(self):
        self.x_before = self.unit.x
        self.y_before = self.unit.y
        self.unit.moveTo(self.x_, self.y_)

    def undo(self):
        self.unit.moveTo(self.x_before, self.y_before)


class Unit2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        print('Move to ({}, {})'.format(x, y))


class InputHandler_3:
    def __init__(self, unit):
        self.unit = unit

    def handle_input(self):
        if (isPressed(BUTTON_W)):
            return MoveCommand(self.unit, self.unit.x, self.unit.y+1)
        elif (isPressed(BUTTON_D)):
            return MoveCommand(self.unit, self.unit.x+1, self.unit.y)
        elif (isPressed(BUTTON_S)):
            return MoveCommand(self.unit, self.unit.x, self.unit.y-1)
        elif (isPressed(BUTTON_A)):
            return MoveCommand(self.unit, self.unit.x-1, self.unit.y)

        return None


def example_3():
    unit = Unit2()
    inputHandler = InputHandler_3(unit)
    command_list = []
    global BUTTON_PRESSED
    BUTTON_PRESSED = 2
    command = inputHandler.handle_input()
    if command:
        command_list.append(command)
        command.execute()
    BUTTON_PRESSED = 3
    command = inputHandler.handle_input()
    if command:
        command_list.append(command)
        command.execute()
    BUTTON_PRESSED = 4
    command = inputHandler.handle_input()
    if command:
        command_list.append(command)
        command.execute()
    command_list.pop().undo()
    command_list.pop().undo()
    command_list.pop().undo()



if __name__ == '__main__':
    example_1()
    example_2()
    example_3()

# Вывод: Было представлено две реализации использования патерна Команда
#        В Питоне функции являются объектами, поэтому не нужно создавать что-либо
#        дополнительно, кроме случая когда команда создается динамически
