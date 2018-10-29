# TODO: 
# 1. Необходимо подобрать нужный шаблон, упростить и дать возможноть легко добавлять
#    новые возможности персонажу.
# 2* Добавить состояние IMAGE_CROUCH_SHOOT

JUMP_VELOCITY = 5

BUTTON_SPACE = 1
BUTTON_DOWN = 2
BUTTON_LBM = 3

IMAGE_SHOOT = 'IMAGE_SHOOT'
IMAGE_JUMP = 'IMAGE_JUMP'
IMAGE_JUMP_SHOOT = 'IMAGE_JUMP_SHOOT'
IMAGE_STUN = 'IMAGE_STUN'
IMAGE_CROUCH = 'IMAGE_CROUCH'


class Hero:
    def __init__(self):
        self.isJumping = False
        self.yVelocity = 0

    def handleInput(self, input):
        if input == BUTTON_SPACE:
            if not self.isJumping:
                self.isJumping = True
                self.yVelocity = JUMP_VELOCITY
                setGraphics(IMAGE_JUMP)

        if input == BUTTON_DOWN:
            if self.isJumping:
                self.isJumping = False
                self.yVelocity = 0
                setGraphics(IMAGE_STUN)
            else:
                setGraphics(IMAGE_CROUCH)

        if input == BUTTON_LBM:
            if not self.isJumping:
                setGraphics(IMAGE_SHOOT)
            else:
                setGraphics(IMAGE_JUMP_SHOOT)
