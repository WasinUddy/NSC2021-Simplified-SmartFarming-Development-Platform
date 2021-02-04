# All functioning object
from frontend.setting import *
from backend.quick_sort import quick_sort
from frontend.banana import Banana


logger = Banana()
logger.type_color = {
        "Error": 'Red',
        "Warning": 'Yellow',
        "Assert": 'Magenta',
        "Success": 'Green'
        }
logger.datetime_format = 'format_3'

# Button Class
class Button:

    def __init__(self, surface, color, x, y, width, height, text='', textcol=(0, 0, 0), outline=None,
                 text_size=20):
        # defined surface to draw on
        self.surface = surface

        # defined button color
        self.color = color

        # defined button position and size (rect)
        self.x = x
        self.y = y
        self.width, self.height = width, height
        
        # defined text to be shown on button
        self.text = text
        self.text_size = text_size
        self.text_color = textcol

        # set default hovering status to False
        self.over = False
        
        # draw outline aka border color set None for no outline
        self.Outline = outline


    def draw(self, clicked=False):
        # check for outline color
        if self.Outline:
            # draw outline
            pg.draw.rect(self.surface, self.Outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        # draw the button color
        pg.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height), 0)
        # check if the mouse is on the button
        if self.over and not clicked:
            # draw shade
            self.Draw_shade()
        # have text
        if self.text:
            font = pg.font.SysFont(FONTNAME, self.text_size)
            text = font.render(self.text, 1, self.text_color)
        # draw text
        self.surface.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    # check if mouse is on the button
    def isOver(self, pos):
        self.over = False
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                self.over = True
                return True
        return False

    # function draw shade
    def Draw_shade(self):
        shade = pg.Surface((self.width, self.height))
        shade.set_alpha(128)
        shade.fill((255, 255, 255))
        self.surface.blit(shade, (self.x, self.y))

# drop down menu
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
                        self.temp_mouse_hover.append(self.current_item_mouse_hover)
                        if len(self.temp_mouse_hover) >= 1:
                            if self.temp_mouse_hover[-1] == self.temp_mouse_hover[-2]:
                                self.temp_mouse_hover.append(self.current_item_mouse_hover)
                                if len(self.temp_mouse_hover) == self.waiting_time_n_var:
                                    "Draw Description"
                                    
                            else:
                                self.temp_mouse_hover = []
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

# text box
class Textbox:
    def __init__(self, x, y, w, h, text=''):
        # font
        font = pg.font.SysFont(FONTNAME, 30)
        # box 's position and size
        self.rect = pg.Rect(x, y, w, h)
        # text color
        self.color = COLOR_INACTIVE
        # word
        self.text = text
        self.txt_surface = font.render(text, 1, self.color)
        # default text
        self.ftxt = font.render('insert', 1, self.color)
        self.active, self.First = False, True
        self.result = ''

    def handle_event(self, event):
        
        # click
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.First = True
            else:
                self.active = False
                
        # Typing
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.active = False
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:

                    # limit word lenght
                    if self.txt_surface.get_width() < self.rect.width - 20:
                        self.text += event.unicode

    def update(self):

        # get font
        font = pg.font.SysFont(FONTNAME, 35)

        # check width
        width = self.rect.width

        # color when the object is selected
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        self.rect.w = width
        self.txt_surface = font.render(self.text, True, self.color)
        self.result = self.text
        if not self.active and self.text == '':
            self.First = False

    # draw object on screen
    def draw(self, screen):
        pg.draw.rect(screen, table_body, self.rect, 0)
        if not self.First:
            screen.blit(self.ftxt, (self.rect.x + 5, self.rect.y + (self.rect.h - self.ftxt.get_height())/2))
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + (self.rect.h - self.ftxt.get_height())/2))
        #pg.draw.rect(screen, self.color, self.rect, 2)

# counter
class Counter:
    def __init__(self, x, y, w, h, text='0',positive=False):
        font = pg.font.SysFont(FONTNAME, 32)

        # main counter position and size
        self.rect = pg.Rect(x, y, w, h)

        # blackground rect
        self.bg = pg.Rect(x, y, w + h / 2, h)

        # increase and decrease button
        self.rect_up = pg.Rect(x + w - 0.5, y, w/2 + 2, h // 2)
        self.rect_down = pg.Rect(x + w - 0.5, y + h / 2, w/2 + 2, h / 2)

        # increase or decrease status boolean
        self.increase = False
        self.decrease = False

    
        self.color = black
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.result = 0
        self.positive = positive
        
        # load arrow image
        self.down = pg.transform.scale(HEAD, (self.rect.h // 2, self.rect.h // 2))
        self.up = pg.transform.rotate(self.down, 180)


    # analyze pg event for counter object
    def handle_event(self, event):
        
        # when perform left click
        if event.type == pg.MOUSEBUTTONDOWN:
            if not self.text.isnumeric()  and len(str(self.text)) <= 1:
                    self.text = '0'
            # click on increase arrow button
            if self.rect_up.collidepoint(event.pos):
                
                # increase number
                self.text = str(int(self.text) + 1)

                # set increase status
                self.increase = True
            
            # click on decrease arrow button
            if self.rect_down.collidepoint(event.pos):

                # anti negative integers processor LOL cool name uh?
                if int(self.text) >= 1 or self.positive:
                    # decrease number 
                    self.text = str(int(self.text) - 1)
                
                # set decrese status
                self.decrease = True

            # click on rect for typing
            if self.rect.collidepoint(event.pos):

                # toggle use or not
                self.active = not self.active
            else:
                self.active = False
                if len(self.text) <= 1 and not self.text.isnumeric():
                    self.text = '0'

        # if pressed keyboard number
        if event.type == pg.KEYDOWN:
            if self.active:

                # enter
                if event.key == pg.K_RETURN:
                    self.active = False

                # backspace            
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if self.text.isnumeric() and int(self.text) == 0:
                        self.text = '0'
                    
                    # if input is number and less than 4 digits
                    if (len(self.text) < 4 and event.unicode.isnumeric()) or (len(self.text) < 1 and event.unicode == '-' and self.positive):
                        if len(self.text) == 1 and self.text == '0' and event.unicode.isnumeric():
                            self.text = ''
                        self.text += event.unicode


    # update
    def update(self):
        font = pg.font.SysFont(FONTNAME, 32)
        self.txt_surface = font.render(str(self.text), True, self.color)
        width = max(self.rect.w, self.txt_surface.get_width() + 10)
        self.rect.w = width
        self.bg.w = self.rect.w + self.rect.h / 2
        self.rect_up.x = self.rect.w + self.rect.x - 0.5
        self.rect_down.x = self.rect.w + self.rect.x - 0.5
        self.color = COLOR_ACTIVE if self.active else black
        if len(self.text) == 1 and self.text == '-':
            self.result = 0
        elif len(self.text) > 0:
            self.result = int(self.text)
        else:
            self.result = 0



    # draw counter on screen
    def draw(self, screen):
        pg.draw.rect(screen, table_header, self.bg, 0)
        pg.draw.rect(screen, butgreen, (self.rect_up.x, self.rect_up.y, self.rect_up.w, self.rect.h), 0)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + (self.rect.h - self.txt_surface.get_height())/2))
        screen.blit(self.up, (self.rect_up.x + (self.rect_up.w - self.up.get_width())/2 + 1, self.rect.y))
        screen.blit(self.down, (self.rect_down.x + (self.rect_down.w - self.down.get_width())/2, self.rect.y + self.rect.h // 2))
       
        if self.increase:
            self.draw_shade(screen, self.rect.y)
            self.increase = False
        if self.decrease:
            self.draw_shade(screen, self.rect.y + self.rect.h // 2 + 1)
            self.decrease = False

    # draw shade 
    def draw_shade(self, screen, y):
        s = pg.Surface((self.rect_up.w, self.rect_up.h))
        s.set_alpha(100)
        s.fill((0, 0, 0))
        screen.blit(s, (self.rect_up.x, y))


# class table
class Table:
    def __init__(self, surface, color, x, y, width, height, header, text_col=(0, 0, 0), gap=None, w=None, a=3):
        self.table = {'items': [], 'amount': [], 'used_digital_pins': [], 'used_analog_pins': []}
        self.default = header
        self.surface = surface
        self.color = color
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text_color = text_col
        self.list = []
        self.a = a
        self.top, self.bottom = 0, self.a
        self.use_list = []
        if gap is None:
            gap = []
            for _ in header:
                gap.append(0)
        self.gap = gap
        if w is None:
            w = []
            for _ in header:
                w.append(width)
        self.box_width = w

    # draw
    def draw(self, outline=None):
        font = pg.font.SysFont(FONTNAME, min(25, self.height * 4 // 5))
        for word in range(len(self.default)):
            text = font.render(self.default[word], 1, self.text_color)
            if outline:
                pg.draw.rect(self.surface, outline,
                             (self.x - 2 + sum(self.box_width[:word]) + sum(self.gap[:word]), self.y - 2,
                              self.box_width[word] + 4,
                              self.height + 4))
            pg.draw.rect(self.surface, self.color,
                         (self.x + sum(self.gap[:word]) + sum(self.box_width[:word]),
                          self.y, self.box_width[word], self.height), 0)

            s = pg.Surface((self.box_width[word], self.height))
            s.set_alpha(255)
            s.fill(table_header)
            self.surface.blit(s, (self.x + sum(self.gap[:word]) + sum(self.box_width[:word]), self.y))
            self.surface.blit(text, (self.x + sum(self.gap[:word]) +
                                     (self.box_width[word] - text.get_width()) / 2 + sum(self.box_width[:word]),
                                     self.y + (self.height - text.get_height()) / 2))
        if len(self.table['items']) > 0:
            self.word_list(outline)
        self.scrollbar(outline)
    # value table
    def word_list(self, outline):
        self.list = []
        font = pg.font.SysFont(FONTNAME, min(25, self.height * 4 // 5))
        for item in self.table:
            self.list.append(self.table[item])
        self.list = np.transpose(np.array(self.list[:len(self.default)])).tolist()
        self.use_list = self.list[self.top:self.bottom]
        for row in range(len(self.use_list)):
            if sum(self.gap) is not 0:
                pg.draw.rect(self.surface, butgreen, (
                self.x, self.y + self.height * (row + 1), sum(self.gap) + sum(self.box_width), self.height))
            for col in range(len(self.use_list[row])):
                text = font.render(str(self.use_list[row][col]), 1, self.text_color)
                if outline:
                    pg.draw.rect(self.surface, outline,
                                 (self.x + sum(self.box_width[:col]) - 2 + sum(self.gap[:col]),
                                  self.y + self.height * (row + 1) - 2, self.box_width[col] + 4,
                                  self.height + 4))
                pg.draw.rect(self.surface, self.color,
                             (self.x + sum(self.box_width[:col]) + sum(self.gap[:col]),
                              self.y + self.height * (row + 1),
                              self.box_width[col], self.height))
                self.surface.blit(text,
                                      (self.x + sum(self.gap[:col]) + (
                                    self.box_width[col] - text.get_width()) / 2 + sum(self.box_width[:col]),
                                    self.y + self.height * (row + 1) + (self.height - text.get_height()) / 2))


    # add data for first table
    def add_data_1(self, added_data):
        item, quantity = added_data
        if item in self.table['items']:
            item_index = self.table['items'].index(item)
            self.table['amount'][item_index] += quantity
            item_json_filename = f'resources/items/{item}.json'
            with open(item_json_filename) as json_file:
                item_dict = json.load(json_file)
            if item_dict["PIN"]["Digital"] != 0:
                if self.table['used_digital_pins'][item_index] + item_dict["PIN"]["Digital"] * quantity >= 0:
                    self.table['used_digital_pins'][item_index] += item_dict["PIN"]["Digital"] * quantity
                    self.table['used_analog_pins'][item_index] += 0
                else:
                    self.clear(item_index)
            if item_dict["PIN"]["Analog"] != 0:
                self.table['used_analog_pins'][item_index] += item_dict["PIN"]["Analog"] * quantity
                self.table['used_digital_pins'][item_index] += 0
        elif quantity > 0:
            item_json_filename = f'resources/items/{item}.json'
            with open(item_json_filename) as json_file:
                item_dict = json.load(json_file)
            self.table['items'].append(item)
            self.table['amount'].append(quantity)
            self.table['used_digital_pins'].append(item_dict["PIN"]["Digital"] * quantity)
            self.table['used_analog_pins'].append(item_dict["PIN"]["Analog"] * quantity)

    # add data for second table
    def add_data_2(self, added_data):
        Output, Input, Condition, Value = added_data
        if Condition == '=':
            Condition = '=='
        self.table['items'].append(str(Output))
        self.table['amount'].append(str(Input))
        self.table['used_digital_pins'].append(str(Condition))
        self.table['used_analog_pins'].append(str(Value))

    # clear table
    def clear(self, index=-1):
        if len(self.table['items']) > 0:
            self.table['items'].pop(index)
            self.table['amount'].pop(index)
            self.table['used_digital_pins'].pop(index)
            self.table['used_analog_pins'].pop(index)

    # analyze pg event
    def handle_event(self, e):
        total_width = sum(self.box_width)
        total_gap = sum(self.gap)
        pos = pg.mouse.get_pos()
        if self.x < pos[0] < self.x + total_gap + total_width + 20:
            if self.y < pos[1] < self.y + self.height * (1 + min(len(self.table['items']), self.bottom - self.top + 1)):
                if e.type == pg.MOUSEBUTTONDOWN:
                    if e.button == 4:
                        if self.top > 0:
                            self.top -= 1
                            self.bottom -= 1
                    elif e.button == 5:
                        if self.bottom < len(self.table['items']):
                            self.top += 1
                            self.bottom += 1
                            

    # create scrollbar on table
    def scrollbar(self, outline):
        total_width = sum(self.box_width)
        total_gap = sum(self.gap)
        if self.bottom > len(self.table['items']) and self.bottom > self.a: 
            self.bottom = len(self.table['items'])
            self.top = len(self.table['items']) - self.a
        if outline:
            pg.draw.rect(self.surface, outline,
                             (self.x + total_width + total_gap-2, self.y-2, 14,
                              4 + self.height * min(1 + len(self.table['items']), self.bottom - self.top + 1)))
        pg.draw.rect(self.surface, table_header,
                     (self.x + total_width + total_gap, self.y, 10,
                      self.height * min(1 + len(self.table['items']), self.bottom - self.top + 1)))
        if len(self.table['items']) == 0:
            None
        elif len(self.table['items']) <= self.bottom - self.top and len(self.table['items']) > 0:
            pg.draw.rect(self.surface, grey2,
                         (self.x + total_width + total_gap,
                          self.y + self.height, 10, self.height * (len(self.table['items']))))
        else:
            pg.draw.rect(self.surface, grey2,
                         (self.x + total_width + total_gap, self.y + self.height +  self.height *
                          ((self.bottom - self.top) / (len(self.table['items']) - self.bottom + self.top + 1))
                          * self.top, 10, 0.5 + self.height *
                          ((self.bottom - self.top) / (len(self.table['items']) - self.bottom + self.top + 1))))


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
                