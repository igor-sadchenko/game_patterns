# TODO:
# 1. Необходимо подобрать нужный шаблон, который поможет упростить добавление
#    новых возможностей для персонажа.
# 2* Добавить статус CROUCH_SHOOT

JUMP_VELOCITY = 11
GRAVITY = 10

BUTTON_SPACE = 1
BUTTON_DOWN = 2
BUTTON_LBM = 3

WAIT_STATUS = 'WAIT'
SHOOT_STATUS = 'SHOOT'
JUMP_STATUS = 'JUMP'
JUMP_SHOOT_STATUS = 'JUMP_SHOOT'
STUN_STATUS = 'STUN'
CROUCH_STATUS = 'CROUCH'


class Hero:
    def __init__(self):
        self.__is_jumping = False
        self.__y = 0
        self.__velocity_y = 0

        self.__status = WAIT_STATUS

    @property
    def status(self):
        return self.__status

    def applyPhysX(self):
        self.__velocity_y -= GRAVITY
        self.__y = max(0, self.__y + self.__velocity_y)

        if self.__y > 0:
            self.__is_jumping = True
        else:
            self.__is_jumping = False
            self.__velocity_y = 0

    def handleInput(self, input_btn, isDown):
        if not isDown:
            if self.__is_jumping:
                self.__setStatus(JUMP_STATUS)
            else:
                self.__setStatus(WAIT_STATUS)
        else:
            if input_btn == BUTTON_SPACE:
                if not self.__is_jumping:
                    self.__is_jumping = True
                    self.__velocity_y = JUMP_VELOCITY
                    self.__setStatus(JUMP_STATUS)

            if input_btn == BUTTON_DOWN:
                if self.__is_jumping:
                    self.__is_jumping = False
                    self.__velocity_y -= JUMP_VELOCITY
                    self.__setStatus(STUN_STATUS)
                else:
                    self.__setStatus(CROUCH_STATUS)

            if input_btn == BUTTON_LBM:
                if not self.__is_jumping:
                    self.__setStatus(SHOOT_STATUS)
                else:
                    self.__setStatus(JUMP_SHOOT_STATUS)

    def __setStatus(self, status):
        self.__status = status


if __name__ == '__main__':
    hero = Hero()

    hero.handleInput(BUTTON_DOWN, True)
    hero.applyPhysX()
    hero.handleInput(BUTTON_DOWN, False)
    hero.applyPhysX()
