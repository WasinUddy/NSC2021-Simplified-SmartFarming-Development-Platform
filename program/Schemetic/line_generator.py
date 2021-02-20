from setting import *

def line_generator(screen, pos1, pos2, color, board, item, ratio):
    b_left_pins = 0
    b_right_pins = 0
    i_left_pins = 0
    i_right_pins = 0
    Y_top = 0
    Y_bottom = 0
    for index, start in enumerate(pos1):
        case = [0,0]
        end = pos2[index]
        start = (start[0], start[1] + ratio)
        start_finish = ()
        # side for starting position
        # right
        if start[0] > board.board_rect.center[0]:
            b_right_pins += 1
            start = (start[0] + 2*ratio, start[1]) 
            x1 = start[0] + b_right_pins*2*ratio
            case[0] = 0
        #left
        elif start[0] <= board.board_rect.center[0]:
            b_left_pins += 1
            x1 = start[0] - b_left_pins*2*ratio
            case[0] = 1 
        # side for ending position
        # right
        if end[0] > item.center[0]:
            i_right_pins += 1
            x2 = end[0] + i_right_pins*2*ratio
            case[1] = 0
        # left
        elif end[0] <= item.center[0]:
            i_left_pins += 1
            x2 = end[0] - i_left_pins*2*ratio
            case[1] = 1
        
        # y axis
        # item left side
        if item.center[0] < board.board_rect.center[0]:
            # facing each other
            if case == [1, 0]:
                y1 = start[1]
            # right board to left item or left board to right item
            elif case == [0, 1] or case == [1, 0]:
                if item.center[1] < board.board_rect.center[1]:
                    Y_top += 1
                    y1 = min(board.board[1] , item[1]) - Y_top*2*ratio
                else:
                    Y_bottom += 1
                    y1 = max(board.board[3], item[3]) + Y_bottom*2*ratio
            else:
                if item.center[1] < board.board_rect.center[1]:
                    if end[1] < board.board_rect.center[1]:
                        y1 = end[1]
                    elif end[1] >= board.board_rect.center[1]:
                        Y_top += 1
                        y1 = board.board[1] - Y_top*2*ratio
                else:
                    if end[1] < board.board_rect.center[1]:
                        y1 = end[1]                         
                    elif end[1] >= board.board_rect.center[1]:
                        Y_bottom += 1
                        y1 = board.board[3] + Y_bottom*2*ratio
        # item right side
        else:
            y1 = start[1]

        start_finish += (start,)
        start_finish += ((x1, start[1]),)
        start_finish += ((x1, y1),)
        start_finish += ((x2, y1),)
        start_finish += ((x2, end[1]),)
        start_finish += (end,)
        
        
        pg.draw.lines(screen, color, False, start_finish, ratio)
    


