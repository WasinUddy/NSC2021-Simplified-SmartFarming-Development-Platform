from frontend.gui import Gui
import os
from backend.scrapper import check_library
from threading import Thread
# Set Environment Path
import pygame as pg

start_quit = False
def check():
    global start_quit
    check_library()
    start_quit = True

def start_up():
    global start_quit
    size = (700,490)
    start = pg.transform.scale(pg.image.load("frontend/pictures/Start.png"),size)
    pg.init()
    screen = pg.display.set_mode(size, pg.NOFRAME) 
    clock = pg.time.Clock()
    count = 0
    font = pg.font.SysFont('helvetica', 15)
    t_list = ['starting.', 'starting..', 'starting...']
    while not start_quit:
        count +=1
        if count < 10:
            txt = font.render(t_list[0], True, (255,255,255))
        elif count < 20:
            txt = font.render(t_list[1], True, (255,255,255))
        elif count < 30:
            txt = font.render(t_list[2], True, (255,255,255))
        else:
            count = 0
        
        
        start_quit = pg.event.get(pg.QUIT)
        screen.blit(start, (0,0))
        screen.blit(txt, (40, size[1] - 30))
        clock.tick(60)
        pg.display.flip()

if __name__ == "__main__":
    Thread(target=check).start()
    Thread(target=start_up())


g = Gui()


while g.running:
    g.run()

