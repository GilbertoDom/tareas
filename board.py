#! usr/bin/env python
#-*- coding:utf-8 -*-

# Inteligencia Artificial
# Gilberto Carlos Domìnguez Aguilar

import copy


class Board:
    def __init__(self, state):
        self.state = copy.deepcopy(state)
        self.x = 1
        self.y = 1
        self.state_current_0 = self.get_index_of_0()

    def state_expand(self):
        s = self.state
        self.evaluate_moves(self.get_index_of_0())
    def evaluate_moves(self, index):
        if isinstance(index, str):
            return None
        else:
            current_x, current_y = index[0], index[1]
            move_up = (current_x - self.x, current_y)
            move_down = (current_x + self.x, current_y)
            move_right = (current_x, current_y + self.y)
            move_left = (current_x, current_y - self.y)
            print(move_up, move_down, move_right, move_left)      
        
    def get_index_of_0(self):
        i = 0
        for row in self.state:        
            if 0 in row:
                return (i,row.index(0)) 
            i += 1
        return("ningun 0 indexado")     


init_state = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,0]]

O = Board(init_state)
O.state_expand()

