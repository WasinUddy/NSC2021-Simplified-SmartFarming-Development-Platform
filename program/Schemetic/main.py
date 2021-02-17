from Nano import *

pg.init()
WIDTH , HEIGHT = 500,500
screen = pg.display.set_mode((WIDTH, HEIGHT))
uno = Nano(screen, WIDTH, HEIGHT, 10)
clock = pg.time.Clock()
quit = False
while not quit:
    quit = pg.event.get(pg.QUIT)
    screen.fill((255,255,255))
    uno.draw()
    pg.display.flip()
    clock.tick(60)