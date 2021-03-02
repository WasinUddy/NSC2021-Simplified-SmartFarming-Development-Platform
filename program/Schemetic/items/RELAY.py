from frontend.setting import *

class RELAY:
    def __init__(self, screen, x, y,r, rotation = 360):
        self.r = r
        self.item_img = pg.transform.scale(pg.transform.rotate(pg.image.load("Schemetic/items/RELAY.png"), rotation + 90),(int(23*2*r),int(16*2*r)))
        self.item_rect = self.item_img.get_rect()
        self.item_rect.midtop = (int(x), int(y))
        self.screen = screen
        self.item = [self.item_rect[0], self.item_rect.y, self.item_rect[2], self.item_rect.y + 25*r]
        self.pin_pos_dict = {
            "0": (self.item_rect.center[0] + 16*r*(-1)**(rotation/20), self.item_rect.center[1] - 8*r),
            "GND": (self.item_rect.center[0] + 16*r*(-1)**(rotation/20), self.item_rect.center[1] - int(5*r)),
            "VCC": (self.item_rect.center[0] + 16*r*(-1)**(rotation/20), self.item_rect.center[1] - int(1*r))
        }
        


    def draw(self):
        self.screen.blit(self.item_img, self.item_rect)
        