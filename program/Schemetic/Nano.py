import pygame as pg
import numpy as np


class Nano:
    def __init__(self, screen, WIDTH, HEIGHT,r):
        # ratio 68:53
        self.r = r
        self.board_img = pg.transform.scale(pg.transform.rotate(pg.image.load("board/NANO.png"), 270),(int(32*r),int(52*r)))
        self.board_rect = self.board_img.get_rect()
        self.board_rect.center = (int(WIDTH/2), int(HEIGHT/2))
        self.screen = screen
        self.pin_pos_dict = {
            "0": (21.2, 39.3),
            "1": (21.2, 37.9),
            "2": (21.2, 32),
            "3": (21.2, 30.2),
            "4": (21.2, 28.3),
            "5": (21.2, 26.2),
            "6": (21.2, 24.3),
            "7": (21.2, 22.6),
            "8": (21.2, 20.5),
            "9": (21.2, 18.6),
            "10": (21.2, 16.9),
            "11": (21.2, 15),
            "12": (21.2, 13.1),
            "13": (10, 13.1),
            "14": (10, 18.8),
            "15": (10, 20.7),
            "16": (10, 22.4),
            "17": (10, 24),
            "18": (10, 26),
            "19": (10, 28),
            "20": (10, 30),
            "21": (10, 31.7)
        }
        
        self.power_pos_dict = {
            "3.3V": (10, 15),
            "5V": (10,33.5),
            "GND0": (21.2, 33.4),
            "GND1": (10, 37.3),
            "Vin": (10, 39)
        }
        



    def draw(self):
        self.screen.blit(self.board_img, self.board_rect)
        # 294, 437
        for pin in self.pin_pos_dict.keys():    
            pg.draw.rect(
                self.screen,
                (255,0,0),
                (self.board_rect.x + int(self.pin_pos_dict[pin][0]*self.r),
                self.board_rect.y + int(self.pin_pos_dict[pin][1]*self.r) ,
                self.r, self.r)
                )

        for power in self.power_pos_dict.keys():    
            pg.draw.rect(
                self.screen,
                (255,0,0),
                (self.board_rect.x + int(self.power_pos_dict[power][0]*self.r),
                self.board_rect.y + int(self.power_pos_dict[power][1]*self.r) ,
                self.r, self.r)
                )
           