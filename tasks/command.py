# Задача: Упростить обработчик нажатий описанный ниже

# class InputHandler:
#     ...
#     def handle_input(self):
#         if (isPressed(BUTTON_X)):
#             jump()
#         elif (isPressed(BUTTON_Y)):
#             fireGun()
#         elif (isPressed(BUTTON_A)):
#             swapWeapon()
#         elif (isPressed(BUTTON_B)):
#             lurchIneffectively()

BUTTON_X = 1
BUTTON_Y = 2
BUTTON_A = 3
BUTTON_B = 4

BUTTON_PRESSED = 1
### Реализация 1 ###


def isPressed(button):
    if button == BUTTON_PRESSED:
        return True
    return False


def jump():
    print('Run jump()')


def fireGun():
    print('Run fireGun()')


def swapWeapon():
    print('Run swapWeapon()')


def lurchIneffectively():
    print('Run lurchIneffectively()')


class InputHandler_1:

    def __init__(self):
        self.button_x = jump
        self.button_y = fireGun
        self.button_a = swapWeapon
        self.button_b = lurchIneffectively

    def handle_input(self):
        if (isPressed(BUTTON_X)):
            self.button_x()
        elif (isPressed(BUTTON_Y)):
            self.button_y()
        elif (isPressed(BUTTON_A)):
            self.button_a()
        elif (isPressed(BUTTON_B)):
            self.button_b()

### Реализация 2 ###


def jump_(actor):
    actor.jump()


class Actor:
    def jump(self):
        print('Run actor.jump()')


class InputHandler_2:

    def __init__(self):
        self.button_x = jump_

    def handle_input(self):
        if (isPressed(BUTTON_X)):
            return self.button_x
        elif (isPressed(BUTTON_Y)):
            return self.button_y
        elif (isPressed(BUTTON_A)):
            return self.button_a
        elif (isPressed(BUTTON_B)):
            return self.button_b

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


class Unit:
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
        if (isPressed(BUTTON_X)):
            return MoveCommand(self.unit, self.unit.x, self.unit.y+1)
        elif (isPressed(BUTTON_Y)):
            return MoveCommand(self.unit, self.unit.x+1, self.unit.y)
        elif (isPressed(BUTTON_A)):
            return MoveCommand(self.unit, self.unit.x, self.unit.y-1)
        elif (isPressed(BUTTON_B)):
            return MoveCommand(self.unit, self.unit.x-1, self.unit.y)

        return None


def example_1():
    inputHandler = InputHandler_1()

    inputHandler.handle_input()


def example_2():
    actor = Actor()
    inputHandler = InputHandler_2()

    command = inputHandler.handle_input()
    if command:
        command(actor)


def example_3():
    unit = Unit()
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
