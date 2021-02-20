from setting import *


class Nano:
    def __init__(self, screen, WIDTH, HEIGHT,r):
        # ratio 68:53
        self.r = r
        self.board_img = pg.transform.scale(pg.transform.rotate(pg.image.load("board/NANO.png"), 270),(int(32*r),int(52*r)))
        self.board_rect = self.board_img.get_rect()
        self.board_rect.center = (int(WIDTH/2), int(HEIGHT/2))
        self.screen = screen
        self.pin_pos_dict = {
            "0": (self.board_rect.x + 21.2*r, self.board_rect.y + 39.3*r),
            "1": (self.board_rect.x + 21.2*r, self.board_rect.y + 37.9*r),
            "2": (self.board_rect.x + 21.2*r, self.board_rect.y + 32*r),
            "3": (self.board_rect.x + 21.2*r, self.board_rect.y + 30.2*r),
            "4": (self.board_rect.x + 21.2*r, self.board_rect.y + 28.3*r),
            "5": (self.board_rect.x + 21.2*r, self.board_rect.y + 26.2*r),
            "6": (self.board_rect.x + 21.2*r, self.board_rect.y + 24.3*r),
            "7": (self.board_rect.x + 21.2*r, self.board_rect.y + 22.6*r),
            "8": (self.board_rect.x + 21.2*r, self.board_rect.y + 20.5*r),
            "9": (self.board_rect.x + 21.2*r, self.board_rect.y + 18.6*r),
            "10": (self.board_rect.x + 21.2*r, self.board_rect.y + 16.9*r),
            "11": (self.board_rect.x + 21.2*r, self.board_rect.y + 15*r),
            "12": (self.board_rect.x + 21.2*r, self.board_rect.y + 13.1*r),
            "13": (self.board_rect.x + 10*r, self.board_rect.y + 13.1*r),
            "14": (self.board_rect.x + 10*r, self.board_rect.y + 18.8*r),
            "15": (self.board_rect.x + 10*r, self.board_rect.y + 20.7*r),
            "16": (self.board_rect.x + 10*r, self.board_rect.y + 22.4*r),
            "17": (self.board_rect.x + 10*r, self.board_rect.y + 24*r),
            "18": (self.board_rect.x + 10*r, self.board_rect.y + 26*r),
            "19": (self.board_rect.x + 10*r, self.board_rect.y + 28*r),
            "20": (self.board_rect.x + 10*r, self.board_rect.y + 30*r),
            "21": (self.board_rect.x + 10*r, self.board_rect.y + 31.7*r)
        }
        
        self.power_pos_dict = {
            "3.3V": (self.board_rect.x + 10*r, self.board_rect.y + 15*r),
            "5V": (self.board_rect.x + 10*r,self.board_rect.y + 33.5*r),
            "GND0": (self.board_rect.x + 21.2*r, self.board_rect.y + 33.4*r),
            "GND1": (self.board_rect.x + 10*r, self.board_rect.y + 37.3*r),
            "Vin": (self.board_rect.x + 10*r, self.board_rect.y + 39*r)
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
           