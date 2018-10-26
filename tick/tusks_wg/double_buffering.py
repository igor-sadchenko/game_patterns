# Задача: Дать возможность ряду последовательных операций
# выполяться мгновенно или одновременно


class Framebuffer:
    WIDTH = 10
    HEIGHT = 10
    def __init__(self):
        self.pixels = [0 for _ in range(WIDTH * HEIGHT)]

    def clear(self):
        for i in range(WIDTH*HEIGHT):
            self.pixels[i] = 0

    def draw(self, x, y):
        self.pixels[WIDTH * y + x] = 1

    def get_pixel(self):
        return self.pixels

class Scene:
    def __init__(self):
        self.buffer = [Framebuffer() for _ in range(2)]
        self.current = self.buffer[0]
        self.next = self.buffer[1]

    def draw(self):
        self.next.clear()

        self.next.draw(1, 1)
        self.next.draw(4, 1)
        self.next.draw(1, 3) # проблема может возникнуть здесь
        self.next.draw(2, 4)
        self.next.draw(3, 4)
        self.next.draw(4, 3)

        self._swap()            # это её решает

    def getBuffer(self):
        return self.current

    def _swap(self):
        self.current, self.next = self.next, self.current