from frontend.setting import *
import json


def generate_schemetics(BOARD, SENSOR):
    from PIL import Image
    from Schemetic.line_2 import line_generator
    board_name = BOARD.split(' ')[1].upper()
    exec(f'from Schemetic.board.{board_name} import {board_name}')    
    size = width, height = (3000, 4000)
    with open(f"resources/Boards/{BOARD}.json") as json_file:
            I2C_pin = json.load(json_file)["Communication_pins"]
    screen = pg.Surface(size)
    board = eval(f"{board_name}(screen, width, height, 20)")
    #screen.fill((0,255,0))
    screen.fill((255,255,255))
    board.draw()
    H_list = []
    color_list = [black, red, blue, donecolor, green, yellow, whiteblue, blue, donecolor, green, yellow, whiteblue]
    for index, item_ID in enumerate(SENSOR["NAME"]):
        item_name = item_ID.split('_')[0].upper()
        exec(f'from Schemetic.items.{item_name} import {item_name}')
        #width, height = Image.open(f'Schemetic/items/{item_name}.png').size
        # sensor name
        font = pg.font.SysFont(None, 100)
        txt = font.render(item_name, True, black)
        if index <= 5:
            sen = eval(f"{item_name}(screen, board.board_rect.center[0] - 1000, 20*board.r + 1.5*sum(H_list), board.r/2)")
             # draw name
            screen.blit(txt, (sen.item_rect.left - sen.item_rect.w/4, 20*board.r + 1.5*sum(H_list) - 4*board.r))
        elif index > 5:
            sen = eval(f"{item_name}(screen, board.board_rect.center[0] + 1000, 20*board.r + 1.5*sum(H_list[6:]), board.r/2, True)")
             # draw name
            screen.blit(txt, (sen.item_rect.left + sen.item_rect.w/4, 20*board.r + 1.5*sum(H_list[6:]) - 4*board.r))
        sen.draw()
        height = sen.item_img.get_height()
        H_list.append(height)
       
        # draw line
        b_pin, s_pin = [], []
        if len(SENSOR["PIN"][index]) > 1:
            for p in SENSOR["PIN"][index]:
                b_pin.append(board.pin_pos_dict[str(I2C_pin[p][0])])
                s_pin.append(sen.pin_pos_dict[p])
        else:
            b_pin.append(board.pin_pos_dict[str(SENSOR["PIN"][index][0])])
            s_pin.append(sen.pin_pos_dict['0'])
        # get board pin
        board_pin_position = [board.power_pos_dict["GND1"], board.power_pos_dict["5V"]] + b_pin
        # get sensor pin
        sensor_pin_position = [sen.pin_pos_dict["GND"], sen.pin_pos_dict["VCC"]] + s_pin
        line_generator(screen, board_pin_position, sensor_pin_position, color_list[:2] + color_list[2+index:], board, sen, board.r)
    pg.image.save(screen,"Schemetic.png")



#generate_schematics('NANO')