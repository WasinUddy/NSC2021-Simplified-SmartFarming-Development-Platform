from frontend.setting import *



def generate_schemetics(BOARD='UNO', SENSOR=['DHT11_0', 'DHT11_1']):
    from PIL import Image
    from Schemetic.line_2 import line_generator
    exec(f'from Schemetic.board.{BOARD} import {BOARD}')    
    size = width, height = (3000, 4000)
    screen = pg.Surface(size)
    board = eval(f"{BOARD}(screen, width, height, 20)")
    #screen.fill((0,255,0))
    screen.fill((255,255,255))
    board.draw()
    H_list = []
    color_list = [darkpurple, grey2, donecolor, green, yellow]
    for index, item_ID in enumerate(SENSOR):
        item_name = item_ID.split('_')[0].upper()
        exec(f'from Schemetic.items.{item_name} import {item_name}')
        width, height = Image.open(f'Schemetic/items/{item_name}.png').size
        H_list.append(height)
        if index <= 4:
            sen = eval(f"{item_name}(screen, board.board_rect.center[0] - 1000, (sum(H_list)/10)*(board.r), board.r/2)")
        elif index > 4:
            sen = eval(f"{item_name}(screen, board.board_rect.center[0] + 1000, (index-4)*(height/10)*(board.r)/2, board.r/2, 180)")
        sen.draw()
        font = pg.font.SysFont(None, 100)
        txt = font.render(item_name, True, black)
        screen.blit(txt, (board.board_rect.center[0] - 1000, (sen.item_rect.center[1] - sen.item[1]) + (sum(H_list)/10)*(board.r)))
        if item_name == "ALCD":
            line_generator(screen,[board.pin_pos_dict[str(18)],board.pin_pos_dict[str(19)],board.power_pos_dict["GND1"], board.power_pos_dict["5V"]],
                                    [sen.pin_pos_dict['0'], sen.pin_pos_dict["1"], sen.pin_pos_dict["2"], sen.pin_pos_dict["3"]],[whiteblue, purple, black, red], board,sen, board.r)
        elif item_name == "SOILMOISTURE":
            line_generator(screen,[board.pin_pos_dict[str(14)],board.power_pos_dict["GND1"], board.power_pos_dict["5V"]],
                                    [sen.pin_pos_dict['0'], sen.pin_pos_dict["1"], sen.pin_pos_dict["2"]],[blue, black, red], board, sen, board.r)

        else:
            line_generator(screen,[board.pin_pos_dict[str(index + 1)],board.power_pos_dict["GND1"], board.power_pos_dict["5V"]],
                                    [sen.pin_pos_dict['0'], sen.pin_pos_dict["1"], sen.pin_pos_dict["2"]],[color_list[index], black, red], board, sen, board.r)
            
    pg.image.save(screen,"test_subject.png")



#generate_schematics('NANO')