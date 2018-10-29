# TODO: 
# 1. Устранить зависимость игрового времени от пользовательского ввода и скорости рендера
# 2* Обрабатывать случаи фризовлагов)


while True:
    processInput()
    update()        # вызывается для обновления игрового времени.
    render()        # fps может быть 20 или 120, но игра должна идти с одинаковой скоростью.


# import time
#
# MS_PER_UPDATE = 10
#
# previous = time.time()
# lag = 0
#
# while True:
#     current = time.time()
#     elapsed = current - previous
#     previous = current
#     lag += elapsed
#
#     processInput()
#
#     while lag >= MS_PER_UPDATE:
#         update()
#         lag -= MS_PER_UPDATE
#
#     render()
