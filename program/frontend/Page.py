from frontend.sprite import *
import os
from backend.pin_management import pin_management
from backend.arduino_code_generator import generate_and_upload
from backend.get_list import get_board_list, get_item_list
from backend.input_output_seperator import input_output_seperator
from Schemetic.main import *
import tkinter.filedialog
import time
from Schemetic.get_connection import get_connection

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
        self.logo = pg.transform.scale(LOGO, (200, 200))
        # next button
        self.next = Button(self.surface, table_header, WIDTH/2 + 10, HEIGHT*9/10, 120, 40,
                           "next", txtbrown, None, 30)
        # back
        self.back = Button(self.surface, table_header, WIDTH/2 - 130, self.height*9/10, 120, 40,
                           "back", txtbrown, None, 30)
        # add data to page 1 table, page 2
        self.add = Button(self.surface, table_header, 0, 250, 75, 40,
                          "เพิ่ม", txtbrown, None, 30)
        # remove data from page 1 table, page 2
        self.remove = Button(self.surface, table_header, 0, 275, 75, 40,
                             "ลบ", txtbrown, None, 30)
        # upload buttom
        self.upload = Button(self.surface, table_header, WIDTH/2 + 10, self.height*9/10, 120, 40,
                             "ลงโปรเเกรม", txtbrown, None, 35)
        # arduino board dropdown menu
        self.board = Choice(self.surface, table_header, WIDTH - 420, 90, 320, 40, get_board_list()[0],
                            get_board_list()[1:], txtbrown, 6)
        # arduino sensor drop down menu page 1
        self.sensor = Choice(self.surface, table_header, WIDTH - 400, 220, 125, 40, get_item_list()[0],
                             get_item_list()[1:], txtbrown, 3,True)
        # arduino sensor drop down menu page 3
        self.Sensor3 = Choice(self.surface, table_header, 30, 115, 120, 30, None,
                              None, txtbrown, 3, True)
        self.page3_object = Choice(self.surface, table_header, 105, 115, 250, 30, None,
                            None, txtbrown, 3, True)
        self.relay = Choice(self.surface, table_header, -20, 115, 100, 30, None,
                            None, txtbrown, 3, True)
        self.Sensor2 = Choice(self.surface, table_header, 130, 115, 250, 30, None,
                              None, txtbrown, 3, True)
        self.operator = Choice(self.surface, table_header, 525, 115, 55, 30, '>',
                               ['<', '='], txtbrown)
        self.table = Table(self.surface, table_body, WIDTH*1/10, HEIGHT*330/600, 150, 40, PAGE1, txtbrown, None, None, 4)
        self.table_page_2 = Table(self.surface, table_body, 10, 250, 80, 40, PAGE2, txtbrown, (75, 30,30),
                            (140, 264, 60, 67),6)
        self.table_page_3 = Table(self.surface, table_body, 10, 250, 120, 40, PAGE3, txtbrown, (60,20,50), (85, 204, 204, 40), 7)
        self.sensor_amount = Counter(self.width - 197, 190, 100, 40)
        self.number = Counter(610, 115, 50, 30,'0',True)
        self.row = Counter(610, 115, 50, 30)
        self.insert = Textbox(10, 115, 100, 30)
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
                    self.click = False
                    logger.log("excuting update function, collecting data from current page and progressing to the next page", "Success")
                else:
                    self.page = self.total
        elif self.back.isOver(pos) and click and self.page > 1:
            self.page -= 1
            logger.log("excuting update function, saving current page and returning to previous page", "Success")


    def page1(self, drawtext, pos):
        self.surface.blit(BOARD_CONTROLLER, (50,50))
        self.surface.blit(SENSOR, (50 ,190))
        self.add.x, self.add.y = self.width *502/WIDTH, self.height*270/HEIGHT
        self.remove.x, self.remove.y = self.width *580/WIDTH, self.height*270/HEIGHT
        self.sensor.x, self.board.x = self.width*265/WIDTH, self.width*185/500
        self.sensor.y, self.board.y = self.height*190/HEIGHT, self.height*50/HEIGHT
        self.table.x, self.table.y = 45, self.height*330/600
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
        pg.draw.rect(self.surface, butgreen, (55, self.height - 60, 200, 10), 5)
        pg.draw.rect(self.surface, butgreen, (55, self.height - 60, 200, 10))
        pg.draw.rect(self.surface, grey, (55, self.height - 60,
                                         sum(self.table.table['used_digital_pins']) / digital_amount * 200, 10))
        pg.draw.rect(self.surface, butgreen, (55, self.height - 40, 200, 10), 5)
        pg.draw.rect(self.surface, butgreen, (55, self.height - 40, 200, 10))
        pg.draw.rect(self.surface, grey, (55, self.height - 40,
                                         sum(self.table.table['used_analog_pins']) / digital_amount * 200, 10))
        drawtext(str(sum(self.table.table['used_digital_pins'])), 20, white, 40, self.height - 55)
        drawtext(str(sum(self.table.table['used_analog_pins'])), 20, white, 40, self.height - 35)
        drawtext("ช่องอนาล็อก", 25, white, 300, self.height - 35)
        drawtext('ช่องดิจิตอล', 25, white, 300, self.height - 55)
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
                    logger.log("Sucessfully added data to the table", "Success")
        elif sum(self.table.table['used_digital_pins']) > digital_amount:
            self.table.clear()
            logger.log("Successfully remove data")
        if self.remove.isOver(pos) and self.click:
            if sum(self.table.table['used_digital_pins']) == int(self.sensor_amount.result):
                self.table.add_data_1((str(self.sensor.result), -int(self.sensor_amount.result) - 1))
            else:
                self.table.add_data_1((str(self.sensor.result), -int(self.sensor_amount.result)))


    def page2(self, drawtext, pos):
        self.surface.blit(OUTPUT_TAG, (250, 50))
        self.surface.blit(ARE, (535, 115))
        self.surface.blit(OPERATE, (125, 110))
        self.surface.blit(OPERATE, (155, 245))
        self.relay.x, self.Sensor2.x = 10,200
        self.choice = [self.relay, self.Sensor2, self.operator]
        self.amount = [self.number]
        self.tables = [self.table_page_2]
        self.text = []
        self.add.x, self.add.y = 610, 155
        self.remove.x, self.remove.y = 610, 198
        self.button = [self.next, self.back, self.add, self.remove]
        if self.table.table['items'] and self.click:
            self.relay.WORDS_LIST = input_output_seperator(self.page1_result)[1]
            self.Sensor2.WORDS_LIST = input_output_seperator(self.page1_result)[0]
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
        self.surface.blit(DISPLAY_OUTPUT_TAG, (250, 50))
        #self.surface.blit(DISPLAY, (150, 100))
        if self.table.table['items']:
            self.page3_object.WORDS_LIST = input_output_seperator(self.page1_result)[0]
            self.Sensor3.WORDS_LIST = input_output_seperator(self.page1_result)[2]
        self.page3_object.x, self.Sensor3.x = 130, 465
        '''drawtext("analog output", 25, white, 20, 125)
        drawtext("display", 20, white, 20, 160)
        drawtext("display", 20, white, 20, 400)
        drawtext("value", 20, white, 210, 160)
        drawtext("value", 20, white, 210, 400)'''
        self.choice = [self.page3_object, self.Sensor3]
        self.amount = [self.row]
        self.text = [self.insert]
        self.table.default = PAGE2
        self.tables = [self.table_page_3]
        self.button = [self.back, self.add, self.remove, self.upload]
        if self.add.isOver(pos) and self.click:
            self.table_page_3.add_data_2(
                (self.insert.result,self.page3_object.result, self.Sensor3.result, self.row.result))
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
            pin_pos = {'NAME':[],
                        'TYPE':[],
                        'PIN':[]}
            polymer = '''

            '''
            for key in item_dict_keys:
                pin_pos['NAME'].append(get_connection(key, item_dict)['NAME'])
                pin_pos['TYPE'].append(get_connection(key, item_dict)['TYPE'])
                pin_pos['PIN'].append(get_connection(key, item_dict)['PIN'])
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
            #file_path = tkinter.filedialog.asksaveasfile(defaultextension=".ino")
            # Create Folder
            #print(file_path)
            condition_dict = self.page2_result
            noncondition_dict = self.page3_result
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
            #if noncondition_dict["INPUT"][0] is 'None':
            if noncondition_dict["INPUT"] == 'None':
                noncondition_dict = None
            generate_and_upload(item_dict, condition_dict, noncondition_dict,self.official_name, "Test")
            
            generate_schemetics(self.board.result, pin_pos)
          
    def draw(self, drawtext, pos):
        #self.surface.blit(self.logo, (25, -50))
        drawtext(str(self.page), 20, white, self.width - 20, self.height - 26)
        if self.page == 1:
            self.page1(drawtext, pos)
        elif self.page == 2:
            self.page2(drawtext, pos)
        elif self.page == 3:
            self.page3(drawtext, pos)
