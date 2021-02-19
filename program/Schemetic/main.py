from Nano import *

pg.init()
WIDTH , HEIGHT = 500,500
screen = pg.display.set_mode((WIDTH, HEIGHT))
uno = Nano(screen, WIDTH, HEIGHT, 10)

pos2 = (350,50)
clock = pg.time.Clock()
quit = False
while not quit:
    quit = pg.event.get(pg.QUIT)
    screen.fill((255,255,255))
    uno.draw()
    #for pos1 in uno.pin_pos_dict.keys():
    #   pg.draw.lines(screen,(0,0,255),False,(uno.pin_pos_dict[pos1],(pos2[0] - int(pos1)*10,uno.pin_pos_dict[pos1][1]),(pos2[0] - int(pos1)*10,pos2[1]),pos2), 5)
    pg.display.flip()
    clock.tick(60)