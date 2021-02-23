from frontend.setting import *

class UNO:
    def __init__(self, screen, WIDTH, HEIGHT,r):
        # ratio 68:53
        self.r = r
        self.board_img = pg.transform.scale(pg.transform.rotate(pg.image.load("Schemetic/board/UNO.png"), 270),(int(32*r),int(46*r)))
        self.board_rect = self.board_img.get_rect()
        self.board_rect.center = (int(WIDTH/2), int(HEIGHT/2))
        self.screen = screen
        self.board = [self.board_rect[0], self.board_rect.y, self.board_rect[2], self.board_rect.y + 47*r]
        self.pin_pos_dict = {
            "0": (self.board_rect.x + 30*r, self.board_rect.y + 42.2*r),
            "1": (self.board_rect.x + 30*r, self.board_rect.y + 41*r),
            "2": (self.board_rect.x + 30*r, self.board_rect.y + 39.2*r),
            "3": (self.board_rect.x + 30*r, self.board_rect.y + 37.5*r),
            "4": (self.board_rect.x + 30*r, self.board_rect.y + 36*r),
            "5": (self.board_rect.x + 30*r, self.board_rect.y + 34.6*r),
            "6": (self.board_rect.x + 30*r, self.board_rect.y + 33.1*r),
            "7": (self.board_rect.x + 30*r, self.board_rect.y + 31.6*r),
            "8": (self.board_rect.x + 30*r, self.board_rect.y + 29.1*r),
            "9": (self.board_rect.x + 30*r, self.board_rect.y + 27.4*r),
            "10": (self.board_rect.x + 30*r, self.board_rect.y + 25.9*r),
            "11": (self.board_rect.x + 30*r, self.board_rect.y + 24.3*r),
            "12": (self.board_rect.x + 30*r, self.board_rect.y + 22.7*r),
            "13": (self.board_rect.x + 30*r, self.board_rect.y + 21.3*r),
            "14": (self.board_rect.x + 1.2*r, self.board_rect.y + 34.5*r),
            "15": (self.board_rect.x + 1.2*r, self.board_rect.y + 36*r),
            "16": (self.board_rect.x + 1.2*r, self.board_rect.y + 37.6*r),
            "17": (self.board_rect.x + 1.2*r, self.board_rect.y + 39.3*r),
            "18": (self.board_rect.x + 1.2*r, self.board_rect.y + 40.8*r),
            "19": (self.board_rect.x + 1.2*r, self.board_rect.y + 42.3*r)
        }
        self.power_pos_dict = {
            "3.3V": (self.board_rect.x + 1.2*r, self.board_rect.y + 25.3*r),
            "5V": (self.board_rect.x + 1.2*r, self.board_rect.y +  27*r),
            "GND0": (self.board_rect.x + 1.2*r, self.board_rect.y + 28.5*r),
            "GND1": (self.board_rect.x + 1.2*r, self.board_rect.y + 30.1*r),
            "Vin": (self.board_rect.x + 1.2*r, self.board_rect.y + 31.6*r),
            "GND2": (self.board_rect.x + 30*r, self.board_rect.y + 19.8*r),
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