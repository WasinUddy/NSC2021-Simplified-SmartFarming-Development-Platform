from frontend.setting import *

class DHT11:
    def __init__(self, screen, x, y,r, rotation = 360):
        self.r = r
        self.item_img = pg.transform.scale(pg.transform.rotate(pg.image.load("Schemetic/items/DHT11.png"), rotation),(int(55*r),int(55*r)))
        self.item_rect = self.item_img.get_rect()
        self.item_rect.center = (int(x), int(y))
        self.screen = screen
        self.item = [self.item_rect[0], self.item_rect.center[1] - 8*r , self.item_rect[2], self.item_rect.y + 42*r]
        self.pin_pos_dict = {
            "0": (self.item_rect.center[0] + 17*r*(-1)**(rotation/20), self.item_rect.center[1] - 2*r),
            "1": (self.item_rect.center[0] + 17*r*(-1)**(rotation/20), self.item_rect.center[1]),
            "2": (self.item_rect.center[0] + 17*r*(-1)**(rotation/20), self.item_rect.center[1] + 2*r)
        }
        


    def draw(self):
        self.screen.blit(self.item_img, self.item_rect)
        