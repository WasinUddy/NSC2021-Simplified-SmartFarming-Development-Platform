import random
import pygame as pg
import string
from frontend.setting import *


class Choice:
    def __init__(self, Surface, color, x, y, width, height, default, text=None, textcol=(0, 0, 0), a=3):
        # check for word use in list
        if text is None:
            text = []
        elif not isinstance(text, list):
            text = list(text)
        self.WORDS_LIST = text
        # default text on the box
        self.default = default
        # result 
        self.result = default
        # add the default word in the WORD_LIST
        if self.default is not None:
            self.WORDS_LIST.append(self.default)
        # initial sort WORD_LIST 
        self.WORDS_LIST.sort()
        # screen surface in which will be drawn on
        self.surface = Surface
        # the box color
        self.color = color
        # the box position and size3
        self.x = x
        self.y = y
        self.width, self.height = width, height
        # click variable
        self.clicked = False
        # text color
        self.text_color = textcol
        # check if menu drop down or not
        self.toggle = False
        self.held = False
        # if the menu is not overlapp one another
        self.allow = True
        # arrow image
        self.image = pg.transform.scale(Down, (15, 15)) 
        self.top = 0
        # maximum word window and positon when scrolling
        self.boxes = min(a, len(self.WORDS_LIST))
        # word use to display for the menu
        self.display_text = self.WORDS_LIST[self.top:self.boxes]
        # word original size
        self.size = 30
        # change size if it is too big for the box when initialize
        if len(self.WORDS_LIST) is not 0:
            font = pg.font.SysFont(FONTNAME, 20)
            m = [len(str(x)) for a, x in enumerate(self.WORDS_LIST)]
            text = font.render(self.WORDS_LIST[m.index(max(m))], 1, self.text_color)
            if text.get_width() > self.width - 20:
                self.size = round(self.width * 4 / 5 / text.get_width() * 20)
        # search variable
        self.search = False
        # clear the display box to search
        self.clear = False


    def draw(self, outline=None):
        # draw box outline
        if outline:
            pg.draw.rect(self.surface, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        # draw box
        pg.draw.rect(self.surface, self.color, (self.x, self.y, self.width - 20, self.height), 0)
        pg.draw.rect(self.surface, butgreen, (self.x + self.width - 20, self.y, self.width*3/10, self.height), 0)
        # draw text on box
        text = pg.font.SysFont(FONTNAME, self.size).render(str(self.default), 1, self.text_color)
        self.surface.blit(text, (
            self.x + ((self.width - 20 - text.get_width()) / 2), self.y + (self.height / 2 - text.get_height() / 2)))
        # draw drop down button
        if outline:
            pg.draw.line(self.surface, outline, (self.x + self.width - 22, self.y),
                         (self.x + self.width - 22, self.y + self.height), 2)
        self.surface.blit(self.image, (self.x + self.width + (self.width*3/10 - self.image.get_width())/2 - 20,
                                       self.y + (self.height - self.image.get_height()) / 2))
        # if open drop down and there is text draw drop down
        if self.toggle and len(self.WORDS_LIST) is not 0:
            self.word_list(outline)


    def isOver(self, pos, clicked):
        # if mouse is on the box
        if self.y < pos[1] < self.y + self.height:
            if self.x < pos[0] < self.x + self.width - 20:
                if clicked:
                    self.search = True
                    if self.clear is not True:
                        self.default = ''
                        self.clear = True
                    self.toggle = False
                return True
            elif self.x + self.width - 20 < pos[0] < self.x + self.width*13/10 - 20:
                if clicked:
                    self.toggle = not self.toggle
                return True
        # if drop down
        if self.toggle:
            if self.x < pos[0] < self.x + self.width*13/10 - 30:
                for word in range(len(self.display_text) + 1):
                    if self.y + word * self.height - 1 < pos[1] < self.y + self.height + word * self.height + 1:
                        self.current_item_mouse_hover = self.display_text[word - 1]
                        self.Infobox(self.x + self.width, self.y + word * self.height, 100, 50,['dfsdfsdfsdssf'])
                        if word > 0 and clicked:
                            # get the result
                            self.default = self.display_text[word - 1]
                            self.result = self.display_text[word - 1]
                            self.toggle = False
                            logger.log("Selected " + str(self.result), "Success")
                        return True
        return False

    def word_list(self, outline):
        if outline:
            pg.draw.rect(self.surface, outline,
                         (self.x - 2, self.y - 2 + self.height, self.width + 4, self.height *
                          min(len(self.WORDS_LIST), len(self.display_text)) + 4))
        # drop down body
        pg.draw.rect(self.surface, table_body, (self.x, self.y + self.height, self.width*13/10 - 29, self.height *
                                                min(len(self.WORDS_LIST), len(self.display_text))))
        # scroll bar
        pg.draw.rect(self.surface, table_header, (self.x + self.width*13/10 - 29, self.y + self.height, 10, self.height *
                                                  min(len(self.WORDS_LIST), len(self.display_text))))
        pg.draw.rect(self.surface, grey2, (self.x + self.width*13/10 - 29, self.y + 0.5 + self.height *
                                           (((self.boxes - self.top) / (
                                                   len(self.WORDS_LIST) - self.boxes + self.top + 1)) * self.top + 1), 10,
                                           0.5 + self.height * ((self.boxes - self.top) / (
                                                   len(self.WORDS_LIST) - self.boxes + self.top + 1))))
        #display text
        for word in range(len(self.display_text)):
            if outline:
                pg.draw.line(self.surface, outline, (self.x + self.width - 22, self.y),
                             (self.x + self.width - 22, self.y + self.height * (word + 2)), 2)
                pg.draw.line(self.surface, outline, (self.x, self.y + self.height * (word + 2)),
                             (self.x + self.width - 22, self.y + self.height * (word + 2)), 2)
            text = pg.font.SysFont(FONTNAME, self.size).render(str(self.display_text[word]), 1, self.text_color)
            self.surface.blit(text, (
                self.x + ((self.width*13/10 - 30 - text.get_width()) / 2),
                self.y + self.height * (word + 1) + (self.height / 2 - text.get_height() / 2)))
            
        

    def update(self, clicked, pos):
        #drop down
        if self.toggle is not True:
            self.search = False
            self.clear = False
        # set drop down limit
        if self.boxes <= 3:
            self.boxes = min(3, len(self.WORDS_LIST))
        # if drop down is not overlap
        if self.allow:
            # mouse in side the box and clicked and has drop down box
            if self.isOver(pos, clicked) and self.toggle:
                self.toggle = True
            # mouse inside the box open dropdown and close
            elif self.isOver(pos, clicked) and clicked:
                self.toggle = not self.toggle
            # mouse is outside the box close the menu
            elif not self.isOver(pos, clicked) and clicked:
                self.toggle = False
        # search by name
        if self.search:
            self.display_text = quick_sort(self.WORDS_LIST, self.default)[self.top:self.boxes]
        # if not using search
        else:
            # display the top name in list
            self.display_text = self.WORDS_LIST[self.top:self.boxes]
            self.default = self.result

    def size_check(self):
        # get size for text
        if len(self.WORDS_LIST) is not 0:
            font = pg.font.SysFont(FONTNAME, 20)
            m = [len(str(x)) for a, x in enumerate(self.WORDS_LIST)]
            text = font.render(self.WORDS_LIST[m.index(max(m))], 1, self.text_color)
            if text.get_width() > self.width - 24:
                self.size = round(self.width * 4 / 5 / text.get_width() * 20)

    def handle_event(self, event):
        # keyboard and mouse function
        if self.toggle:
            if event.type == pg.MOUSEBUTTONDOWN:
                # mouse wheel scroll down
                if event.button == 4:
                    if self.top > 0:
                        self.top -= 1
                        self.boxes -= 1
                # mouse wheel scroll up
                elif event.button == 5:
                    if self.boxes < len(self.WORDS_LIST):
                        self.top += 1
                        self.boxes += 1
            elif event.type == pg.KEYDOWN:
                # typing
                if self.search:
                    # press enter to cancel
                    if event.key == pg.K_RETURN:
                        self.search = False
                        self.toggle = False
                    # backspace to delete
                    elif event.key == pg.K_BACKSPACE:
                        self.default = self.default[:-1]
                    else:
                        # keyboard letter
                        self.default += event.unicode
                        self.top = 0
                        self.boxes = min(3, len(self.WORDS_LIST))
    
    def Infobox(self,x,y,w,h,text):
        limit = (h-10)// 20
        top, bottom = 0, limit
        font = pg.font.SysFont(FONTNAME, 20)
        use_list = text[top:bottom]
        pg.draw.rect(self.surface, grey,(x,y,w,h))
        for row in range(len(use_list)):
            render_text = font.render(str(use_list[row]), 1, black)
            self.surface.blit(render_text,(x + (w - text.get_width()) / 2,
                                    y + 3 + row * (h/(bottom - top) + text.get_height())/2))
        if bottom > len(text) and bottom > limit: 
            bottom = len(text)
            top = 0
        pg.draw.rect(self.surface, table_header, (x + w*13/10 - 29, y, 10, h))
        pg.draw.rect(self.surface, grey2, (x + w*13/10 - 29, y + h/(len(text) - len(use_list) + 1)*top,
                                            10, h/(len(text) - len(use_list) + 1)))
          


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
        self.active = False
        self.a = (h-10)// self.font_size
        self.top, self.bottom = 0, self.a
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
                                        self.rect.y + 3 + row * (self.rect.h/(self.bottom - self.top) + text.get_height())/2))
            self.scrollbar(None)
            #pg.draw.rect(screen, self.color, self.rect, 2)

     # create scrollbar on table
    def scrollbar(self, outline):
        if self.bottom > len(self.text) and self.bottom > self.a: 
            self.bottom = len(self.text)
            self.top = 0
        pg.draw.rect(self.surface, table_header, (self.rect.x + self.rect.w*13/10 - 29, self.rect.y, 10, self.rect.h))
        pg.draw.rect(self.surface, grey2, (self.rect.x + self.rect.w*13/10 - 29, self.rect.y + self.rect.h/(len(self.text) - len(self.use_list) + 1)*self.top,
                                            10, self.rect.h/(len(self.text) - len(self.use_list) + 1)))
                                
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
#information = Infobox(100,50,100,100,['dsf','sdffsdfsdfsdf','dsf','sdffsdfsdfsdf','dsf','sdffsdfsdfsdf','55151','dfssd'])
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
choice = Choice(screen, blue, 50,50 ,100,20,'sd',['dssds','safasfaf'] )
while not quit:
    quit = pg.event.get(pg.QUIT)
    for e in pg.event.get():
        choice.handle_event(e)
    click = pg.mouse.get_pressed()[0]

    screen.blit(intermediate, (0, 0))
    choice.update(click)
    choice.draw()

    
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