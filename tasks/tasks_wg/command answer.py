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

# Вывод: Было представлено две реализации использования патерна Команда
#        В Питоне функции являются объектами, поэтому не нужно создавать что-либо
#        дополнительно, кроме случая когда команда создается динамически
