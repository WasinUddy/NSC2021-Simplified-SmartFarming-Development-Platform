from Nano import *
from line_generator import line_generator

pg.init()
WIDTH , HEIGHT = 500,500
screen = pg.display.set_mode((WIDTH, HEIGHT))
uno = Nano(screen, WIDTH, HEIGHT, 6)
sen = pg.Rect(30,350,50,50)
pos2 = (350,50)
clock = pg.time.Clock()
quit = False
while not quit:
    quit = pg.event.get(pg.QUIT)
    screen.fill((255,255,255))
    #pg.draw.rect(screen, red, (50,50,100,200))
    uno.draw()
    pg.draw.rect(screen, blue,sen)
    line_generator(screen,[uno.pin_pos_dict["9"],uno.pin_pos_dict["7"],uno.pin_pos_dict["13"], uno.pin_pos_dict["15"]],[(30,360),(80,360), (80, 370),(80, 380)], grey, uno,sen, 3)
    #for pos1 in uno.pin_pos_dict.keys():
    #   pg.draw.lines(screen,(0,0,255),False,(uno.pin_pos_dict[pos1],(pos2[0] - int(pos1)*10,uno.pin_pos_dict[pos1][1]),(pos2[0] - int(pos1)*10,pos2[1]),pos2), 5)
    pg.display.flip()
    clock.tick(60)