# Задача: Устранить зависимость игрового времени от 
# пользовательского ввода и скорости процессора
# small change
 
import time 

MS_PER_UPDATE = 10

previous = time.time()
lag = 0

while True:
    current = time.time()
    elapsed = current - previous
    previous = current
    lag += elapsed

    processInput()

    while lag >= MS_PER_UPDATE:
        update()
        lag -= MS_PER_UPDATE

    render()