# Добавляем необходимые библиотеки
from GAME.Morkov.morkov import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
COLOR = (200, 20, 200)

# Начальные настройки
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()



class Game():
    def __init__(self) -> None:
        app.__init__(self, window)

        self.main_loop()

    def main_loop(self):
        # Main gameloop
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            window.fill(COLOR)

            app.draw(self, window=window)

            pygame.display.update()
            clock.tick(FRAMES_PER_SECOND)



Game()

    