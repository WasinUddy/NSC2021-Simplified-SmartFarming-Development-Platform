import pygame as pg
import json
import numpy as np
from os import path
pg.init()


TXT_FILE = "pin.txt"

TITLE = "Smart Farming"
WIDTH = 700
HEIGHT = 650
FPS = 120
FONTNAME =  "LilyUPC"

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
purple = (190, 0, 190)
blue = (0, 0, 255)
green = (0, 255, 0)
whiteblue = (130, 150, 255)
darkpurple = (25, 6, 47)
grey = (170, 170, 170)
grey2 = (100, 100, 100)
darkgrey = (70, 70, 70)
txtblue = (0, 102, 204)
txtbrown = (89, 61, 30)
butgreen = (177,216,183)
bgcolor = (47,82,51)
donecolor = (207,167,112)
COLOR_INACTIVE = white
#COLOR_ACTIVE = pg.Color('dodgerblue2')
COLOR_ACTIVE = blue
table_header = (148, 201, 115)
table_body = (79, 146, 115)


Down = pg.image.load("frontend/pictures/down.png")
HEAD = pg.image.load('frontend/pictures/arrow.png')
CHECK = pg.image.load('frontend/pictures/check.png')
UNCHECK = pg.image.load('frontend/pictures/uncheck.png')
'''for i in [Down, HEAD, UNCHECK, CHECK]:
    i.set_colorkey(white)'''

LOGO = pg.image.load("frontend/pictures/logo.png")
ICON = pg.image.load("frontend/pictures/icon.png")


PAGE3 = ['ชื่อ','อุปกรณ์ให้ค่า', 'อุปกรณ์เเสดงค่า', "เเถว"]
PAGE2 = ['อุปกรณ์เเสดงค่า', 'อุปกรณ์ให้ค่า', "เงื่อนไข", "ค่า"]
PAGE1 = ['อุปกรณ์', 'จํานวน', 'ช่องดิจิตอล', "ช่องอนาล็อก"]


#cut corner (It has better performance than using drawtext also Itim-Regular font can't be used for some reason)

BOARD_CONTROLLER = pg.transform.scale(pg.image.load("frontend/pictures/1.png"),(170, 81))
SENSOR = pg.transform.scale(pg.image.load("frontend/pictures/2.png"),(100, 62))
OUTPUT_TAG = pg.transform.scale(pg.image.load("frontend/pictures/3.png"),(287, 40))
OPERATE = pg.transform.scale(pg.image.load("frontend/pictures/4.png"),(64, 40))
ARE = pg.transform.scale(pg.image.load("frontend/pictures/5.png"),(33, 25))
DISPLAY_OUTPUT_TAG = pg.transform.scale(pg.image.load("frontend/pictures/6.png"),(269, 40))
DISPLAY = pg.transform.scale(pg.image.load("frontend/pictures/7.png"),(60, 19))
