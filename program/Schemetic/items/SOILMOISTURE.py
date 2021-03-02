from frontend.setting import *

class SOILMOISTURE:
    def __init__(self, screen, x, y,r, rotation = 360):
        self.r = r
        self.item_img = pg.transform.flip(pg.transform.scale(pg.transform.rotate(pg.image.load("Schemetic/items/SOILMOISTURE.png"), 90),(int(46*r),int(20*r))), rotation == 180, False)
        self.item_rect = self.item_img.get_rect()
        self.item_rect.midtop = (int(x), int(y))
        self.screen = screen
        self.item = [self.item_rect[0], self.item_rect.y, self.item_rect[2], self.item_rect.y + 42*r]
        self.pin_pos_dict = {
            "0": (self.item_rect.center[0] + 18*r*(-1)**(rotation/20), self.item_rect.center[1]  +  int(4.5*r)),
            "GND": (self.item_rect.center[0] + 18*r*(-1)**(rotation/20), self.item_rect.center[1] - int(2.5*r)),
            "VCC": (self.item_rect.center[0] + 18*r*(-1)**(rotation/20), self.item_rect.center[1] - int(5.25*r)),        
        }
        


    def draw(self):
        self.screen.blit(self.item_img, self.item_rect)
        