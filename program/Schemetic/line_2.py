from frontend.setting import *


b_left_pins = 0 
b_right_pins =0 
i_left_pins = 0
i_right_pins = 0
pin_wires_top = 0
pin_wires_bottom = 0
same_pos = []
no_dup = []

def line_generator(screen, pos1, pos2, color, board, item, ratio ):
    if type(color) != list:
       color = list(eval("color" +',color'*(len(pos1)- 1)))
    #color = lambda selected_color : selected_color if type(selected_color) == list else [selected_color for i in range(len(pos1))]
    global b_left_pins 
    global b_right_pins 
    global i_left_pins 
    global i_right_pins 
    global pin_wires_top 
    global pin_wires_bottom 
    global same_pos
    global no_dup

    for index, start in enumerate(pos1):
        case = [0,0]
        end = pos2[index]
        start = (start[0], start[1] + ratio/2)
        start_finish = ()
        # side for starting position
        # right
        if start[0] > board.board_rect.center[0]:
            b_right_pins += 1
            start = (start[0] + ratio, start[1]) 
            x1 = start[0] + b_right_pins*ratio*2
            case[0] = 0
        #left
        elif start[0] <= board.board_rect.center[0]:
            same_pos.append(start)
            [no_dup.append(item) for item in same_pos if item not in no_dup]
            b_left_pins = no_dup.index(start)
            x1 = start[0] - (b_left_pins + 1)*ratio*2 
            case[0] = 1 
        # side for ending position
        # right
        if end[0] > item.item_rect.center[0]:
            i_right_pins += 1
            x2 = end[0] + i_right_pins*ratio/2
            case[1] = 0
        # left
        elif end[0] <= item.item_rect.center[0]:
            i_left_pins += 1
            x2 = end[0] - i_left_pins*ratio/2
            case[1] = 1
        
        # y axis
        # item left side
        if item.item_rect.center[0] < board.board_rect.center[0]:
            # facing each other
            if case == [1, 0]:
                y1 = end[1]
            # right board to left item or left board to right item
            elif case == [0, 1] or case == [1, 0]:
                if item.item_rect.center[1] <= board.board_rect.center[1]:
                    pin_wires_top += 1
                    y1 = min(board.board[1] , item.item[1]) - pin_wires_top*2*ratio
                else:
                    pin_wires_bottom += 1
                    y1 = max(board.board[3], item.item[3]) + pin_wires_bottom*2*ratio
            # right board to right item
            else:
                if case == [1, 1]:
                    x1 = x2
                if item.item_rect.center[1] < board.board_rect.center[1]:
                    #if end[1] < board.board_rect.center[1]:
                    pin_wires_top += 1
                    if end[1] < board.board[1] - pin_wires_top*2*ratio:
                        y1 = end[1]
                    else:
                        y1 = board.board[1] - pin_wires_top*2*ratio
                else:
                    pin_wires_bottom += 1                         
                    if end[1] > board.board[3] - pin_wires_bottom*2*ratio:
                        y1 = end[1]
                    else:
                        y1 = max(board.board[3], item.item[3]) + pin_wires_bottom*2*ratio
        # item right side
        else:
            # facing each other
            if case == [0, 1]:
                y1 = start[1]
            # right board to left item or left board to right item
            elif case == [0, 1] or case == [1, 0]:
                if item.item_rect.center[1] < board.board_rect.center[1]:
                    pin_wires_top += 1
                    y1 = min(board.board[1] , item.item[1]) - pin_wires_top*2*ratio
                else:
                    pin_wires_bottom += 1
                    y1 = max(board.board[3], item.item[3]) + pin_wires_bottom*2*ratio
            else:
                if case == [0, 0]:
                    x1 = x2
                if item.item_rect.center[1] < board.board_rect.center[1]:
                    #if end[1] < board.board_rect.center[1]:
                    pin_wires_top += 1
                    if end[1] < board.board[1] - pin_wires_top*2*ratio:
                        y1 = end[1]
                    else:
                        y1 = board.board[1] - pin_wires_top*2*ratio
                else:
                    pin_wires_bottom += 1                         
                    if end[1] > board.board[3] - pin_wires_bottom*2*ratio:
                        y1 = end[1]
                    else:
                        y1 = max(board.board[3], item.item[3]) + pin_wires_bottom*2*ratio
        
        
        start_finish += (start,)
        start_finish += ((x1, start[1]),)
        start_finish += ((x1, y1),)
        start_finish += ((x2, y1),)
        start_finish += ((x2, end[1]),)
        start_finish += (end,)
        
        
        pg.draw.lines(screen, color[index], False, start_finish, int(ratio/2))
