from setting import *

def line_generator(screen, pos1, pos2, color, board_rect, item_rect, ratio):
    for index, start in enumerate(pos1):
        end = pos2[index]
        start_finish = ()
        if start[0] < board_rect[0] + board_rect[2]/2:
            start = (start[0],start[1] + 5)
            current_x = start[0] - 2*ratio*(len(pos1) - index)
            if start[1] > board_rect[1] + board_rect[3]/2:
                current_y = board_rect[1] + board_rect[3] + 2*ratio*(len(pos1) - index) - 30
            else:
                current_y = board_rect[1] - ratio*(len(pos1) - index) + 30
        elif start[0] > board_rect[0] + board_rect[2]/2:
            start = (start[0] + 10,start[1] + 5)
            current_x = start[0] + 2*ratio*(len(pos1) - index)
            if start[1] > board_rect[1] + board_rect[3]/2:
                current_y = board_rect[1] + board_rect[3] + ratio*(len(pos1) - index) - 30
            else:
                current_y = board_rect[1] - ratio*(len(pos1) - index) + 30
        if end[0] < item_rect[0] + item_rect[2]:
            target_x = end[0] - 5
        else:
            target_x = end[0] + 5

        start_finish += (start,)
        start_finish += ((current_x, start[1]),)
        start_finish += ((current_x, current_y),)
        start_finish += ((target_x, current_y),)
        start_finish += ((target_x, end[1]),)
        start_finish += (end,)
        
        
        pg.draw.lines(screen, color, False, start_finish, ratio)
    


