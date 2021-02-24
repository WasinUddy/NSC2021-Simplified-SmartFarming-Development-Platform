from frontend.setting import *
def generate_schemetics(BOARD='UNO', SENSOR=['DHT11_0', 'DHT11_1']):
    from PIL import Image
    from Schemetic.line_generator import line_generator
    exec(f'from Schemetic.board.{BOARD} import {BOARD}')    
    size = width, height = (3000, 4000)
    screen = pg.Surface(size)
    board = eval(f"{BOARD}(screen, width, height, 20)")
    screen.fill((0,255,0))
    board.draw()
    
    for index, item_ID in enumerate(SENSOR):
        item_name = item_ID.split('_')[0]
        exec(f'from Schemetic.items.{item_name} import {item_name}')
        width, height = Image.open(f'Schemetic/items/{item_name}.png').size
        if index <= 6:
            sen = eval(f"{item_name}(screen, board.board_rect.center[0] - 1000, 100 + index*(height/10)*(board.r)/2, board.r/2)")
        elif index > 6:
            sen = eval(f"{item_name}(screen, board.board_rect.center[0] + 1000, (index-6)*(height/10)*(board.r)/2, board.r/2, 180)")
        sen.draw()
        line_generator(screen,[board.pin_pos_dict[str(index + 1)],board.power_pos_dict["GND1"], board.power_pos_dict["5V"]],
                                    [sen.pin_pos_dict['0'], sen.pin_pos_dict["1"], sen.pin_pos_dict["2"]],[blue, black, red], board,sen, board.r)
    pg.image.save(screen,"test_subject.png")



#generate_schematics('NANO')