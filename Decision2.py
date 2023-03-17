#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:33:33 2022

@author: 22003660@campus
"""

import copy

def makeCloneMask(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]

def makeDepMask(x,y):
    return [(x+2,y),(x+2,y+2),(x+2,y-2),(x,y+2),(x,y-2),(x-2,y),(x-2,y+2),(x-2,y-2)]

class State:
    def __init__(self,board,player,turn,nRed,nBlue,hasPassed):
        self.board= board
        self.player= player
        self.turn= turn
        self.nRed= nRed
        self.nBlue= nBlue
        self.hasPassed = hasPassed;
        self.memory = []
    
    def getScore(self,player):
        if player == "R":
            diff = self.nRed - self.nBlue
        else:
            diff = self.nBlue - self.nRed
        return diff
        
    def isOver(self):
        if self.nRed == 0:
            return True
        elif self.nBlue == 0 :
            return True
        elif self.hasPassed == 2:
            return True
        elif self in self.memory:
            return True
        else:
            return False
        

        
    def getMoves(self,player): #set Move
        if self.player == "R":
           nextcolor="B"
        else:
            nextcolor="R"
        allMove = []
        for i in range(len(self.board[player])):
            x,y= self.board[player][i]
            cloneMasque = makeCloneMask(x,y)
            depMasque = makeDepMask(x,y)
            for c in range(len(cloneMasque)):
                j,k=cloneMasque[c]
                if j >=0 and k >=0 and j <= 4 and k <= 4 and (j,k) not in self.board[nextcolor] and (j,k) not in self.board[self.player]:
                    Mv = Move(x,y,j,k,True)
                    allMove.append(Mv)
            for m in range(len(depMasque)):
                j,k=depMasque[m]
                if j >=0 and k >=0 and j <= 4 and k <= 4 and (j,k) not in self.board[nextcolor] and (j,k) not in self.board[self.player]:
                    Mv = Move(x,y,j,k,False)
                    allMove.append(Mv)
        if len(allMove) == 0:
            Mnull = Move(None,None,None,None,False);
            allMove.append(Mnull);
        return allMove
        
    def play(self, Move): #State
        if self.player == "R":
           nextcolor="B"
        else:
            nextcolor="R"
        if Move.pos_i_x == None and  Move.pos_i_x == None and Move.pos_a_x == None and Move.pos_a_x == None:
             New_StateB = State(self.board,nextcolor,self.turn+1,self.nRed,self.nBlue,self.hasPassed+1);
             return New_StateB
        else:
             Masque = makeCloneMask(Move.pos_a_x,Move.pos_a_y)
             Pion=[]
             newboard = {}
             cooNotPlay = []
             for i in range(len(self.board[nextcolor])):
                x,y= self.board[nextcolor][i]
                if (x,y) in Masque:
                    Pion.append((x,y));
                else:
                    if x >=0 and y >=0 and x <= 4 and y <= 4 and (x,y) not in cooNotPlay:
                        cooNotPlay.append((x,y));
             if Move.isClone:
                 if self.player == "R":                     
                    cooRed = list(self.board["R"])+ Pion
                    cooRed.append((Move.pos_a_x,Move.pos_a_y));
                    cooBlue = cooNotPlay
                 else :
                    cooBlue = list(self.board["B"])+ Pion
                    cooBlue.append((Move.pos_a_x,Move.pos_a_y));
                    cooRed = cooNotPlay
                   
             else:
                 
                 if self.player == "R":   
                    cooRed = list(self.board["R"])+ Pion
                    cooRed.append((Move.pos_a_x,Move.pos_a_y));
                    cooRed.remove((Move.pos_i_x,Move.pos_i_y));
                    cooBlue = cooNotPlay
                 else :
                    cooBlue = list(self.board["B"])+ Pion
                    cooBlue.append((Move.pos_a_x,Move.pos_a_y));
                    cooBlue.remove((Move.pos_i_x,Move.pos_i_y));
                    cooRed = cooNotPlay
            
             self.memory.append(self);
             
             newnBlue = len(cooBlue);
             newnRed = len(cooRed);
             newboard = {"R":cooRed,"B":cooBlue};
             New_State = State(newboard,nextcolor,self.turn+1,newnRed,newnBlue,0)
             New_State.memory = copy.deepcopy(self.memory)
             return New_State
    
    def __eq__(self,state):
        if len(self.board)== len(state.board) and self.player == state.player and self.hasPassed != state.hasPassed:
            for i in state.board.items():
                for j in self.board.items():
                    if i == j:
                        return True
        return False

class Move:
    def __init__(self,pos_i_x,pos_i_y,pos_a_x,pos_a_y,isClone):
        self.pos_i_x= pos_i_x
        self.pos_i_y= pos_i_y
        self.pos_a_x= pos_a_x
        self.pos_a_y= pos_a_y
        self.isClone= isClone
        