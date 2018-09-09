#! usr/bin/env python
#-*- coding:utf-8 -*-

# Inteligencia Artificial
# Gilberto Carlos Domìnguez Aguilar

import copy


class Board:
    global x,y 
    #global y 
    x, y = 1, 1
    def __init__(self, state):
        self.state = copy.deepcopy(state)
        #self.state_current_0 = self.get_index_of_0()

    def state_expand(self):
        list_of_children = []
        #s = self.state
        possible_states = self.evaluate_moves(self.get_index_of_0())
        #print possible_states
        for state in possible_states:
            child = Board(state)
            list_of_children.append(child)
        
        return list_of_children
         
       
    def evaluate_moves(self, index):
        if isinstance(index, str):
            return index
        else:
         #   current_state = self.state
            current_x, current_y = index[0], index[1]
            move_up = (current_x - x, current_y)
            move_down = (current_x + x, current_y)
            move_left = (current_x, current_y - y)
            move_right = (current_x, current_y + y)
            moves = [move_up, move_down, move_left, move_right]    
            valid_moves = self.is_valid(moves)
  #          print()
 #           print(current_state)
#            print()
            states = self.gen_state(valid_moves, index)
            #print states
            #print(current_state)
            
            return states

    def gen_state(self, moves, current_index):
        
        def make_board( move, index):
            s = copy.deepcopy(self.state)
            #print s
            curr_x, curr_y = index[0], index[1]
            new_x, new_y = move[0], move[1]
            aux = s[new_x][new_y]
            #print (aux)
            s[curr_x][curr_y] = aux
            s[new_x][new_y] = 0
            #print (state)
            #print(s)
            #print s
            return s
        
        states = []
        #state = current_state
        for move in moves:
            #print(current_state)
            child_state = make_board(move, current_index)
            #print(child_state)
            states.append(child_state)
            #state = current_state
            #print state
        return states
        
    def is_valid(self, list_of_moves):
        valid_moves = []
        for move in list_of_moves:
            x, y = move[0], move[1]
            if x not in [0,1,2,3]:
                continue
            elif y not in [0,1,2,3]:
                continue
            else:
                valid_moves.append(move)
        return valid_moves
        
    def get_index_of_0(self):
        i = 0
        for row in self.state:        
            if 0 in row:
                return (i,row.index(0)) 
            i += 1
        return("ningun 0 indexado")   
        
    def print_board(self):
        pared = "|"
        for row in self.state:
            print
            for n in row:
                #s = "| {} |".join(n)
                print "| " + str(n) + " |",


init_state = [[5,1,3,2], [6,13,7,8], [9,0,11,12],[4,10,15,14]]
goal_state = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,0]]

O = Board(init_state)
L = O.state_expand()

