import sys
import pygame
import numpy as np
"""a_dic = {}
L = []
b = [True,False]
for num in range(len(b)):
    a_dic["key%s"%num] = "abc%s"%num
    L.append(a_dic["key%s"%num])

print(max(L))
"""
'''
import pygame as pygame

screen = pygame.display.set_mode((500, 500))
run = True
drop = Choice(screen,(255,255,255),20,100,100,25,"select",['hi','hi2'])
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    drop.draw()
    pygame.display.flip()
'''
table_header = (52,41,69)
grey2 = (150,150,150)
FONTNAME = 'arial'
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
        self.top, self.bottom = 0, a
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
        font = pygame.font.SysFont(FONTNAME, min(15, self.height * 3 // 5))
        for word in range(len(self.default)):
            text = font.render(self.default[word], 1, self.text_color)
            if outline:
                pygame.draw.rect(self.surface, outline,
                             (self.x - 2 + sum(self.box_width[:word]) + sum(self.gap[:word]), self.y - 2,
                              self.box_width[word] + 4,
                              self.height + 4))
            pygame.draw.rect(self.surface, self.color,
                         (self.x + sum(self.gap[:word]) + sum(self.box_width[:word]),
                          self.y, self.box_width[word], self.height), 0)

            s = pygame.Surface((self.box_width[word], self.height))
            s.set_alpha(255)
            s.fill(table_header)
            self.surface.blit(s, (self.x + sum(self.gap[:word]) + sum(self.box_width[:word]), self.y))
            self.surface.blit(text, (self.x + sum(self.gap[:word]) +
                                     (self.box_width[word] - text.get_width()) / 2 + sum(self.box_width[:word]),
                                     self.y + (self.height - text.get_height()) / 2))
        self.scrollbar(outline)
        if len(self.table['items']) > 0:
            self.word_list(outline)

    # value table
    def word_list(self, outline):
        self.list = []
        font = pygame.font.SysFont(FONTNAME, min(15, self.height * 3 // 5))
        for item in self.table:
            self.list.append(self.table[item])
        self.list = np.transpose(np.array(self.list[:len(self.default)])).tolist()
        self.use_list = self.list[self.top:self.bottom]
        for row in range(len(self.use_list)):
            for col in range(len(self.use_list[row])):
                text = font.render(str(self.use_list[row][col]), 1, self.text_color)
                if outline:
                    pygame.draw.rect(self.surface, outline,
                                 (self.x + sum(self.box_width[:col]) - 2 + sum(self.gap[:col]),
                                  self.y + self.height * (row + 1) - 2, self.box_width[col] + 4,
                                  self.height + 4))
                pygame.draw.rect(self.surface, self.color,
                             (self.x + sum(self.box_width[:col]) + sum(self.gap[:col]),
                              self.y + self.height * (row + 1),
                              self.box_width[col], self.height))
                self.surface.blit(text,
                                      (self.x + sum(self.gap[:col]) + (
                                    self.box_width[col] - text.get_width()) / 2 + sum(self.box_width[:col]),
                                    self.y + self.height * (row + 1) + 2))


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

    # analyze pygame event
    def handle_event(self, e):
        total_width = sum(self.box_width)
        total_gap = sum(self.gap)
        pos = pygame.mouse.get_pos()
        if self.x < pos[0] < self.x + total_gap + total_width + 20:
            if self.y < pos[1] < self.y + self.height * (1 + min(len(self.table['items']), self.bottom - self.top + 1)):
                if e.type == pygame.MOUSEBUTTONDOWN:
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
        if outline:
            pygame.draw.rect(self.surface, outline,
                             (self.x + total_width + total_gap-2, self.y-2, 14,
                              4 + self.height * min(1 + len(self.table['items']), self.bottom - self.top + 1)))
        pygame.draw.rect(self.surface, table_header,
                     (self.x + total_width + total_gap, self.y, 10,
                      self.height * min(1 + len(self.table['items']), self.bottom - self.top + 1)))
        if len(self.table['items']) <= self.bottom - self.top:
            pygame.draw.rect(self.surface, grey2,
                         (self.x + total_width + total_gap,
                          self.y, 10, self.height * (1 + len(self.table['items']))))
        else:
            pygame.draw.rect(self.surface, grey2,
                         (self.x + total_width + total_gap, self.y + self.height *
                          ((self.bottom - self.top + 1) / (len(self.table['items']) - self.bottom + self.top + 1))
                          * self.top, 10, 0.5 + self.height *
                          ((self.bottom - self.top + 1) / (len(self.table['items']) - self.bottom + self.top + 1))))



pygame.init()
# Create the window, saving it to a variable.
held = False
surface = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Example resizable window")
table = Table(surface, (255,0,0), 50, 100, 50, 50, ['1','2','3','4'],(0, 0, 0),[10,50,100],[100,50,40,20])
while True:
    click = pygame.mouse.get_pressed()
    clicked = False
    if click[0]:
        if not held:
            clicked = True
        held = True
    else:
        held = False
    surface.fill((69, 69, 69))
    if clicked:
        table.add_data_2((['1','2'],['3','4'],['5','6'],['7','8']))
    # Draw a red rectangle that resizes with the window.
    table.draw((0,0,0))
    print(table.box_width)
    pygame.display.update()
    for event in pygame.event.get():
        table.handle_event(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)

