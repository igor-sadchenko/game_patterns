# Данный шаблон затрагивает концепцию конечных автоматов
# (finite state machines) (или "FSM")
# Очень неудобно писать всю логику управления в if-ах.
# Поэтому применим шаблон Состояние
class HeroState:
    standing = StandState
    jumping = JumpState

    @classmethod
    def handleInput(hero, input):
        pass


class StandState(HeroState):
    @classmethod
    def handleInput(hero, input):
        if input == UP:
           self.yVelocity = JUMP_VELOCITY;
           setGraphics(IMAGE_JUMP)
           return HeroState.jumping


class JumpState(HeroState):
    @classmethod
    def handleInput(hero, input):
        if input == DOWN:
           self.yVelocity = STUN_VELOCITY;
           setGraphics(IMAGE_STUN)
           return HeroState.standing


class Hero:
    def __init__(self):
        self.state = HeroState.standing

    def handleInput(self, input):
        state = self.state.handleInput(self, input)
        if state is not None:
            self.state = state
