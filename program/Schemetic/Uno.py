from setting import *


class Uno:
    def __init__(self, screen, WIDTH, HEIGHT,r):
        # ratio 68:53
        self.r = r
        self.board_img = pg.transform.scale(pg.transform.rotate(pg.image.load("board/UNO.png"), 270),(int(32*r),int(52*r)))
        self.board_rect = self.board_img.get_rect()
        self.board_rect.center = (int(WIDTH/2), int(HEIGHT/2))
        self.screen = screen
        self.board = [self.board_rect[0], self.board_rect.y + 8*r, self.board_rect[2], self.board_rect.y + 47*r]
        self.pin_pos_dict = {
            "0": (self.board_rect.x + 28.3*r, self.board_rect.y + 43.4*r),
            "1": (self.board_rect.x + 28.3*r, self.board_rect.y + 41.9*r),
            "2": (self.board_rect.x + 28.3*r, self.board_rect.y + 40.6*r),
            "3": (self.board_rect.x + 28.3*r, self.board_rect.y + 39.2*r),
            "4": (self.board_rect.x + 28.3*r, self.board_rect.y + 37.8*r),
            "5": (self.board_rect.x + 28.3*r, self.board_rect.y + 36.6*r),
            "6": (self.board_rect.x + 28.3*r, self.board_rect.y + 35.1*r),
            "7": (self.board_rect.x + 28.3*r, self.board_rect.y + 33.7*r),
            "8": (self.board_rect.x + 28.3*r, self.board_rect.y + 31.7*r),
            "9": (self.board_rect.x + 28.3*r, self.board_rect.y + 30.2*r),
            "10": (self.board_rect.x + 28.3*r, self.board_rect.y + 28.8*r),
            "11": (self.board_rect.x + 28.3*r, self.board_rect.y + 27.6*r),
            "12": (self.board_rect.x + 28.3*r, self.board_rect.y + 26.1*r),
            "13": (self.board_rect.x + 28.3*r, self.board_rect.y + 24.6*r),
            "14": (self.board_rect.x + 3.2*r, self.board_rect.y + 36.5*r),
            "15": (self.board_rect.x + 3.2*r, self.board_rect.y + 37.8*r),
            "16": (self.board_rect.x + 3.2*r, self.board_rect.y + 39.2*r),
            "17": (self.board_rect.x + 3.2*r, self.board_rect.y + 40.4*r),
            "18": (self.board_rect.x + 3.2*r, self.board_rect.y + 42*r),
            "19": (self.board_rect.x + 3.2*r, self.board_rect.y + 43.3*r)
        }
        self.power_pos_dict = {
            "3.3V": (self.board_rect.x + 3.2*r, self.board_rect.y + 28.3*r),
            "5V": (self.board_rect.x + 3.2*r, self.board_rect.y +  29.6*r),
            "GND0": (self.board_rect.x + 3.2*r, self.board_rect.y + 31.1*r),
            "GND1": (self.board_rect.x + 3.2*r, self.board_rect.y + 32.4*r),
            "Vin": (self.board_rect.x + 3.2*r, self.board_rect.y + 33.7*r),
            "GND2": (self.board_rect.x + 28.3*r, self.board_rect.y + 23.5*r),
        }



    def draw(self):
        self.screen.blit(self.board_img, self.board_rect)
        # 294, 437
        for pin in self.pin_pos_dict.keys():    
            pg.draw.rect(
                self.screen,
                (255,0,0),
                (int(self.pin_pos_dict[pin][0]),
                int(self.pin_pos_dict[pin][1]) ,
                self.r, self.r)
                )


        for power in self.power_pos_dict.keys():    
            pg.draw.rect(
                self.screen,
                (255,0,0),
                (int(self.power_pos_dict[power][0]),
                int(self.power_pos_dict[power][1]) ,
                self.r, self.r)
                )