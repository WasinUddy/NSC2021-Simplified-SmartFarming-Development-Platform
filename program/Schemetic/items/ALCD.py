from frontend.setting import *

class ALCD:
    def __init__(self, screen, x, y,r, rotation = 360):
        self.r = r
        self.item_img = pg.transform.scale(pg.transform.rotate(pg.image.load("Schemetic/items/ALCD.png"), rotation),(int(55*r),int(55*r)))
        self.item_rect = self.item_img.get_rect()
        self.item_rect.midtop = (int(x), int(y))
        self.screen = screen
        self.item = [self.item_rect[0], self.item_rect.y, self.item_rect[2], self.item_rect.y + 42*r]
        self.pin_pos_dict = {
            "SDA": (self.item_rect.center[0] + 20*r*(-1)**(rotation/20), self.item_rect.center[1] +19*r),
            "SCL": (self.item_rect.center[0] + 20*r*(-1)**(rotation/20), self.item_rect.center[1] +int(21.5*r)),
            "GND": (self.item_rect.center[0] + 20*r*(-1)**(rotation/20), self.item_rect.center[1] + 14*r),
            "VCC": (self.item_rect.center[0] + 20*r*(-1)**(rotation/20), self.item_rect.center[1] + int(16.5*r))
        }
        


    def draw(self):
        self.screen.blit(self.item_img, self.item_rect)
        