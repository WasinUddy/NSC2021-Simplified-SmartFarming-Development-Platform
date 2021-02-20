from setting import *


class Uno:
    def __init__(self, screen, WIDTH, HEIGHT,r):
        # ratio 68:53
        self.r = r
        self.board_img = pg.transform.scale(pg.transform.rotate(pg.image.load("board/UNO.png"), 270),(int(32*r),int(52*r)))
        self.board_rect = self.board_img.get_rect()
        self.board_rect.center = (int(WIDTH/2), int(HEIGHT/2))
        self.screen = screen
        self.pin_pos_dict = {
            "0": (28.3, 43.4),
            "1": (28.3, 41.9),
            "2": (28.3, 40.6),
            "3": (28.3, 39.2),
            "4": (28.3, 37.8),
            "5": (28.3, 36.6),
            "6": (28.3, 35.1),
            "7": (28.3, 33.7),
            "8": (28.3, 31.7),
            "9": (28.3, 30.2),
            "10": (28.3, 28.8),
            "11": (28.3, 27.6),
            "12": (28.3, 26.1),
            "13": (28.3, 24.6),
            "14": (3.2, 36.5),
            "15": (3.2, 37.8),
            "16": (3.2, 39.2),
            "17": (3.2, 40.4),
            "18": (3.2, 42),
            "19": (3.2, 43.3)
        }
        self.power_pos_dict = {
            "3.3V": (3.2, 28.3),
            "5V": (3.2, 29.6),
            "GND0": (3.2, 31.1),
            "GND1": (3.2, 32.4),
            "Vin": (3.2, 33.7),
            "GND2": (28.3, 23.5),
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