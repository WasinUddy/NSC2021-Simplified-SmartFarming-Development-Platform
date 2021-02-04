import random
import pygame as pg
import string
FONTNAME = 'arial'

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

class Infobox:
    def __init__(self, x, y, w, h, text):
        # font
        font = pg.font.SysFont(FONTNAME, 30)
        # box 's position and size
        self.rect = pg.Rect(x, y, w, h)
        # text color
        self.color = black
        # word
        self.text = text
        self.use_list = []
        self.font_size = 20
        # default text
        self.active = True
        self.top, self.bottom = 0, (h-10)// self.font_size
        self.surface = None


    # draw object on screen
    def draw(self, screen):
        self.surface = screen
        if self.active:
            font = pg.font.SysFont(FONTNAME, self.font_size)
            self.use_list = self.text[self.top:self.bottom]
            pg.draw.rect(self.surface, grey,self.rect)
            for row in range(len(self.use_list)):
                text = font.render(str(self.use_list[row]), 1, self.color)
                self.surface.blit(text,(self.rect.x + (self.rect.w - text.get_width()) / 2,
                                        self.rect.y + 20 *row + (self.rect.h/self.bottom - text.get_height()) / 2))
            self.scrollbar(None)
            #pg.draw.rect(screen, self.color, self.rect, 2)

     # create scrollbar on table
    def scrollbar(self, outline):
        if outline:
            pg.draw.rect(self.surface, outline,
                             (self.x + total_width + total_gap-2, self.y-2, 14,
                              4 + self.rect.h * min(1 + len(self.table['items']), self.bottom - self.top + 1)))
        pg.draw.rect(self.surface, table_header, (self.rect.x + self.rect.w*13/10 - 29, self.rect.y, 10, self.rect.h ))
        pg.draw.rect(self.surface, grey2, (self.rect.x + self.rect.w*13/10 - 29, self.rect.y + 20 *
                                           (((self.bottom - self.top) / (
                                                   len(self.text) - self.bottom + self.top)) * self.top), 10,
                                           20 * ((self.bottom - self.top) / (
                                                   len(self.text) - self.bottom + self.top + 1))))
                                
    def handle_event(self, event):
        if self.active:
            # mouse function
            if event.type == pg.MOUSEBUTTONDOWN:
                # mouse wheel scroll down
                if event.button == 4:
                    if self.top > 0:
                        self.top -= 1
                        self.bottom -= 1
                # mouse wheel scroll up
                elif event.button == 5:
                    if self.bottom < len(self.text):
                        self.top += 1
                        self.bottom += 1
                


pg.init()
information = Infobox(100,50,100,100,['dsf','sdffsdfsdfsdf','dsf','sdffsdfsdfsdf','dsf','sdffsdfsdfsdf'])
screen = pg.display.set_mode((300, 300))
intermediate = pg.surface.Surface((300, 300))
i_a = intermediate.get_rect()
x1 = i_a[0]
x2 = x1 + i_a[2]
a, b = (255, 49, 255), (69, 21, 220)
y1 = i_a[1]
y2 = y1 + i_a[3]
h = y2 - y1
rate = (float((b[0] - a[0]) / h),
        (float(b[1] - a[1]) / h),
        (float(b[2] - a[2]) / h)
        )
for line in range(h):
    color = (min(max(a[0] + (rate[0] * line), 0), 255),
             min(max(a[1] + (rate[1] * line), 0), 255),
             min(max(a[2] + (rate[2] * line), 0), 255)
             )
    pg.draw.line(intermediate, color, (x1, line), (x2, line))

clock = pg.time.Clock()
quit = False

while not quit:
    information.active = True
    quit = pg.event.get(pg.QUIT)
    for e in pg.event.get():
        information.handle_event(e)

    screen.blit(intermediate, (0, 0))
    information.draw(screen)

    
    pg.display.flip()
    clock.tick(60)

'''def quick_sort(sequence, start=0):
    if start == '':
        start = 0
    number_list = [x for x in sequence if isinstance(x, int)]
    alphabets_list = [x for x in sequence if not isinstance(x, int)]
    num = [x for x in alphabets_list if x.isnumeric()]
    alphabets_list = [ele for ele in alphabets_list if ele not in num]
    number_list += [int(x) for x in num]
    special_alphabets = []
    secondary_special_alphabets = []

    for item in alphabets_list:
        if str(item)[:len(str(start))] == str(start)[:]:
            special_alphabets.append(item)
        elif str(item.lower())[:len(str(start))] == str(start)[:]:
            special_alphabets.append(item)
        elif str(start)[:] in str(item):
            secondary_special_alphabets.append(item)
        elif str(start)[:] in str(item.lower()):
            secondary_special_alphabets.append(item)
    alphabets_list = [ele for ele in alphabets_list if ele not in special_alphabets + secondary_special_alphabets]

    length = len(number_list)
    if length <= 1:
        return special_alphabets + secondary_special_alphabets + alphabets_list + number_list
    else:
        pivot = number_list.pop()

    special = []
    item_greater = []
    item_lower = []

    for item in number_list:
        if str(item)[:len(str(start))] == str(start)[:]:
            special.append(item)
        elif item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    if str(pivot)[:len(str(start))] == str(start)[:]:
        return [pivot] + alphabets_list + quick_sort(item_lower) + quick_sort(item_greater)

    return sorted(special_alphabets) + sorted(secondary_special_alphabets) + quick_sort(special) + alphabets_list + quick_sort(item_lower) + [pivot] + quick_sort(item_greater)


print(quick_sort(['text0','text1','text2','text3','text10','text20','text11']))

s = '12abcd405'
result = ''.join([i for i in s if not i.isdigit()])

list_name = ['text0','text1','text2','text3','text10','text20','text11']

#lambda x: float(x[4:]
def intinstr(L):
    for x in L:
        for i, c in enumerate(x):
            if c.isdigit():
                return [].append()



list_name.sort(key=intinstr)
print(list_name)

l = [1,2,3,4]
w = []
for amount in l:
    w.append(50)

print(w)'''