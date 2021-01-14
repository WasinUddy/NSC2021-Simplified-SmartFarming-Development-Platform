from frontend.sprite import *
import os
from backend.pin_management import pin_management
from backend.arduino_code_generator import generate_and_upload
from backend.get_list import get_board_list, get_item_list
from backend.input_output_seperator import input_output_seperator
import time

class Tutorial:
    def __init__(self, screen):
        self.page =1
        self.total = 1
        self.surface = screen
        self.logo = pg.transform.scale(LOGO, (113, 119))
        self.next = Button(self.surface, table_header, WIDTH - 102, 2, 100, 25,
                           "next", txtbrown, None, 20)
        self.back = Button(self.surface, table_header, WIDTH - 102, 27, 100, 25,
                           "back", txtbrown, None, 20)
        self.button = [self.next, self.back]

    def update(self, click, pos):
        if self.next.isOver(pos) and click:
            if self.page < self.total:
                self.page += 1
            else:
                self.page = self.total
        elif self.back.isOver(pos) and click:
            self.page -= 1

    def draw(self, drawtext):
        self.surface.fill(bgcolor)
        pg.draw.rect(self.surface, table_header, (0, 25, WIDTH, 25))
        self.surface.blit(self.logo, (10, 5))
        drawtext("Tutorial", 35, white, WIDTH * 2 / 5, 75)
        drawtext(str(self.page), 20, white, WIDTH - 20, HEIGHT - 26)


class Normal:
    def __init__(self, screen):
        self.page = 0
        self.total = 2
        self.surface = screen
        self.logo = pg.transform.scale(LOGO, (113, 119))
        self.next = Button(self.surface, table_header, WIDTH - 102, 2, 100, 25,
                           "next", txtbrown, None, 20)
        self.back = Button(self.surface, table_header, WIDTH - 102, 27, 100, 25,
                           "back", txtbrown, None, 20)
        self.button = [self.next, self.back]

    def update(self, click, pos):
        if self.next.isOver(pos) and click:
            if self.page < self.total:
                self.page += 1
            else:
                self.page = self.total
        elif self.back.isOver(pos) and click:
            self.page -= 1

    def draw(self, drawtext):
        self.surface.fill(bgcolor)
        pg.draw.rect(self.surface, table_header, (0, 25, WIDTH, 25))
        self.surface.blit(self.logo, (10, 5))
        drawtext("โหมดใช้งานง่าย", 35, white, WIDTH * 2 / 5, 75)
        drawtext(str(self.page), 20, white, WIDTH - 20, HEIGHT - 26)


class Advance:
    def __init__(self, screen):
        # set variables and object
        self.width, self.height = WIDTH, HEIGHT
        # current page
        self.page = 1
        # total page amount
        self.total = 3
        # surface to draw
        self.surface = screen
        # click check
        self.click = None
        # page 1 result
        self.page1_result = None
        # page 2 result
        self.page2_result = None
        # smart farming logo picture
        self.logo = pg.transform.scale(LOGO, (130, 130))
        # next button
        self.next = Button(self.surface, table_header, WIDTH/2 + 10, HEIGHT*9/10, 120, 30,
                           "next", txtbrown, None, 20)
        # back
        self.back = Button(self.surface, table_header, WIDTH/2 - 130, self.height*9/10, 120, 30,
                           "back", txtbrown, None, 20)
        # add data to page 1 table, page 2
        self.add = Button(self.surface, table_header, 0, 250, 50, 20,
                          "เพิ่ม", txtbrown, None, 20)
        # remove data from page 1 table, page 2
        self.remove = Button(self.surface, table_header, 0, 275, 50, 20,
                             "ลบ", txtbrown, None, 20)
        # upload buttom
        self.upload = Button(self.surface, table_header, 470, 250, 70, 20,
                             "ลงโปรดดกรม", txtbrown, None, 20)
        # arduino board dropdown menu
        self.board = Choice(self.surface, table_header, WIDTH - 250, 125, 200, 25, get_board_list()[0],
                            get_board_list()[1:], txtbrown)
        # arduino sensor drop down menu page 1
        self.sensor = Choice(self.surface, table_header, WIDTH - 400, 220, 125, 25, get_item_list()[0],
                             get_item_list()[1:], txtbrown)
        # arduino sensor drop down menu page 3
        self.Sensor3 = Choice(self.surface, table_header, 290, 165, 150, 25, None,
                              None, txtbrown)
        self.p3_thing = Choice(self.surface, table_header, 105, 165, 150, 25, None,
                            None, txtbrown)
        self.relay = Choice(self.surface, table_header, 10, 165, 85, 25, None,
                            None, txtbrown)
        self.Sensor2 = Choice(self.surface, table_header, 140, 165, 180, 25, None,
                              None, txtbrown)
        self.operator = Choice(self.surface, table_header, 435, 165, 50, 25, '>',
                               ['<', '='], txtbrown)
        self.table = Table(self.surface, table_body, WIDTH*1/10, HEIGHT*330/600, 100, 25, PAGE1, txtbrown)
        self.table_page_2 = Table(self.surface, table_body, 10, 270, 80, 35, PAGE2, txtbrown, (70, 25,10),
                            (100, 150, 90, 60),6)
        self.table_page_3 = Table(self.surface, table_body, 10, 280, 120, 35, PAGE3, txtbrown, (60,20,10), (85, 150, 150,40), 6)
        self.sensor_amount = Counter(self.width - 200, 220, 75, 25)
        self.number = Counter(485, 165, 30, 25,'0',True)
        self.row = Counter(480, 165, 50, 25)
        self.insert = Textbox(10, 165, 85, 25)
        self.official_name = None

        self.button = [self.next, self.back]
        self.amount = []
        self.choice = []
        self.tables = []
        self.text = []


    def update(self, click, pos, width, height):
        self.width, self.height = width, height
        self.click = click
        if self.next.isOver(pos):
            self.page1_result = pin_management(self.board.result, self.table.list)
            for c in self.choice:
                c.size_check()
            if click:
                if self.page < self.total:
                    self.page += 1
                else:
                    self.page = self.total
        elif self.back.isOver(pos) and click and self.page > 1:
            self.page -= 1

    def page1(self, drawtext, pos):
        self.surface.blit(BOARD_CONTROLLER, (120,110))
        self.surface.blit(SENSOR, (55,220))
        self.add.x, self.add.y = self.width *3/4 - 60, self.height*250/600
        self.remove.x, self.remove.y = self.width *3/4, self.height*250/600
        self.sensor.x, self.board.x = self.width *1/3, self.width*275/500
        self.sensor.y, self.board.y = self.height*220/600, self.height*110/600
        self.table.x, self.table.y = self.width*1/10, self.height*330/600
        self.choice = [self.sensor, self.board]
        self.amount = [self.sensor_amount]
        self.tables = [self.table]
        self.button = [self.add, self.remove, self.next]
        item = self.board.result
        item_json_path = f"resources/Boards/{item}.json"
        with open(item_json_path) as json_file:
            json_file_dict = json.load(json_file)
        digital_amount = len(json_file_dict['Digital_pins'])
        self.official_name = json_file_dict["official_name"]
        pg.draw.rect(self.surface, butgreen, (50, self.height - 125, 200, 10), 5)
        pg.draw.rect(self.surface, butgreen, (50, self.height - 125, 200, 10))
        pg.draw.rect(self.surface, grey, (50, self.height - 125,
                                         sum(self.table.table['used_digital_pins']) / digital_amount * 200, 10))
        pg.draw.rect(self.surface, butgreen, (50, self.height - 105, 200, 10), 5)
        pg.draw.rect(self.surface, butgreen, (50, self.height - 105, 200, 10))
        pg.draw.rect(self.surface, grey, (50, self.height - 105,
                                         sum(self.table.table['used_analog_pins']) / digital_amount * 200, 10))
        drawtext(str(sum(self.table.table['used_digital_pins'])), 20, white, 40, self.height - 120)
        drawtext(str(sum(self.table.table['used_analog_pins'])), 20, white, 40, self.height - 100)
        drawtext('analog pin', 20, white, 300, self.height - 100)
        drawtext('digital pin', 20, white, 300, self.height - 120)
        if sum(self.table.table['used_digital_pins']) + int(self.sensor_amount.result) <= digital_amount:
            if str(self.sensor.result) == '16x2_I2C_LCD':
                if int(self.sensor_amount.result) > 1:
                    self.sensor_amount.text = 1
                if '16x2_I2C_LCD' in self.table.table['items']:
                    if self.table.table['amount'][self.table.table['items'].index('16x2_I2C_LCD')] >= 1:
                        self.table.table['amount'][self.table.table['items'].index('16x2_I2C_LCD')] = 1
                else:
                    if self.add.isOver(pos) and self.click:
                        self.table.add_data_1((str(self.sensor.result), int(self.sensor_amount.result)))
            else:
                if self.add.isOver(pos) and self.click:
                    self.table.add_data_1((str(self.sensor.result), int(self.sensor_amount.result)))
        elif sum(self.table.table['used_digital_pins']) > digital_amount:
            self.table.clear()
        if self.remove.isOver(pos) and self.click:
            self.table.add_data_1((str(self.sensor.result), -int(self.sensor_amount.result)))


    def page2(self, drawtext, pos):
        self.surface.blit(OUTPUT_TAG, (150, 100))
        self.surface.blit(ARE, (400, 165))
        self.surface.blit(OPERATE, (110, 165))
        self.surface.blit(OPERATE, (110, 265))
        self.relay.x, self.Sensor2.x = 10, 180
        self.choice = [self.relay, self.Sensor2, self.operator]
        self.amount = [self.number]
        self.tables = [self.table_page_2]
        self.text = []
        self.add.x, self.add.y = 480, 205
        self.remove.x, self.remove.y = 480, 235
        self.button = [self.next, self.back, self.add, self.remove]
        if self.table.table['items'] and self.click:
            self.relay.WORDS_LIST = input_output_seperator(self.page1_result)[1]
            self.Sensor2.WORDS_LIST = input_output_seperator(self.page1_result)[0]
        '''drawtext("digital output", 25, white, 20, 125)
        drawtext("operate", 20, white, 100, 160)
        drawtext("operate", 20, white, 100, 310)
        drawtext("when", 20, white, 105, 330)
        drawtext("are", 20, white, 385, 160)'''
        if self.add.isOver(pos) and self.click:
            self.table_page_2.add_data_2(
                (self.relay.result, self.Sensor2.result, self.operator.result, self.number.result))
            self.page2_result = self.table_page_2.table.copy()
            self.page2_result['OUTPUT'] = self.page2_result.pop('items')
            self.page2_result['INPUT'] = self.page2_result.pop('amount')
            self.page2_result['CONDITION'] = self.page2_result.pop('used_digital_pins')
            self.page2_result['VALUE'] = self.page2_result.pop('used_analog_pins')
        if self.remove.isOver(pos) and self.click:
            self.table_page_2.clear()
            


    def page3(self, drawtext, pos):
        self.surface.blit(DISPLAY_OUTPUT_TAG, (150, 100))
        self.surface.blit(DISPLAY, (150, 100))
        if self.table.table['items']:
            self.p3_thing.WORDS_LIST = input_output_seperator(self.page1_result)[0]
            self.Sensor3.WORDS_LIST = input_output_seperator(self.page1_result)[2]
        self.relay.x, self.Sensor2.x = 110, 280
        self.add.x, self.add.y = 480, 200
        self.remove.x, self.remove.y = 480, 225
        '''drawtext("analog output", 25, white, 20, 125)
        drawtext("display", 20, white, 20, 160)
        drawtext("display", 20, white, 20, 400)
        drawtext("value", 20, white, 210, 160)
        drawtext("value", 20, white, 210, 400)'''
        self.choice = [self.p3_thing, self.Sensor3]
        self.amount = [self.row]
        self.text = [self.insert]
        self.table.default = PAGE2
        self.tables = [self.table_page_3]
        self.button = [self.next, self.back, self.add, self.remove, self.upload]
        if self.add.isOver(pos) and self.click:
            self.table_page_3.add_data_2(
                (self.insert.result,self.p3_thing.result, self.Sensor3.result, self.row.result))
        #self.table_page_3.table['used_analog_pins'] = [int(x) if int(x) <= 2 else 2 for x in self.table_page_3.table['used_analog_pins']]
        if self.remove.isOver(pos) and self.click:
            self.table_page_3.clear()
        if self.upload.isOver(pos) and self.click:
            self.page3_result = self.table_page_3.table.copy()
            self.page3_result['name'] = self.page3_result.pop('items')
            self.page3_result['INPUT'] = self.page3_result.pop('amount')
            self.page3_result['OUTPUT'] = self.page3_result.pop('used_digital_pins')
            self.page3_result['row'] = self.page3_result.pop('used_analog_pins')
            item_dict = self.page1_result
            item_dict_keys = item_dict.keys()
            polymer = '''

            '''
            for key in item_dict_keys:
                monomer = f'''
=======
{key}
I2C: {item_dict[key]['I2C']}
SPI: {item_dict[key]['SPI']}
Serial: {item_dict[key]['Serial']}
Digital_pins: {item_dict[key]['Digital_pins']}
Analog_pins: {item_dict[key]['Analog_pins']}
=======
                '''
                polymer += monomer
            with open(TXT_FILE, 'w') as f:
                f.write(polymer)
            condition_dict = self.page2_result

            # Fetal BUG
            print("=======================Fetal BUG Investigate===========================")
            print(item_dict)
            print("====================")
            print(condition_dict)
            print("=========================End of Investigation==========================")
            generate_and_upload(item_dict, condition_dict, self.official_name, "Test")


    def draw(self, drawtext, pos):
        pg.draw.rect(self.surface, butgreen, (0, 25, self.width, 25))
        self.surface.blit(self.logo, (10, 5))
        drawtext(str(self.page), 20, white, self.width - 20, self.height - 26)
        if self.page == 1:
            self.page1(drawtext, pos)
        elif self.page == 2:
            self.page2(drawtext, pos)
        elif self.page == 3:
            self.page3(drawtext, pos)
