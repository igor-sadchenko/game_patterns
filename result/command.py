# TODO: Улучшить обработчик ввода (InputHandler) описанный ниже.
# 1. Необходимо добавить возможность измение настройки кнопок. (Например поставить выстрел на ПКМ.)
# 2* Добавить возможность передавать в метод параметр(ы). (Например можно передавать юнит, который будет выполнять, команду)
# 3* Для возможности реализовать реплеи, необходимо реализовать "отменяемые" методы (хотя бы перемещения). Для примера дан класс Unit.

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

class InputHandler(object):

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


class Unit(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        print('Move to ({}, {})'.format(x, y))
