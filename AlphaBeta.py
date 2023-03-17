# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:18:48 2022

@author: Felix
"""

from Algorithm import Algorithm

class AlphaBeta(Algorithm):
    def __init__(self,player,prof):
        super().__init__(player,prof);
        self.compteur = 0;

# a score mini possible -49
#b score maxi possible 49

    def alphabeta(self,s, a, b, d):
        if d == 0 or s.isOver():
            return s.getScore(s.player)
        else:
            self.compteur += 1;
            if self.player == s.player:
                for i in s.getMoves(self.player):
                    a = max(a, self.alphabeta(s.play(i),a,b,d-1))
                    if a >= b :
                        return a
                return a
            else:
                for y in s.getMoves(s.player):
                    b = min(b, self.alphabeta(s.play(y),a,b,d-1))
                    if a >= b:
                        return b
                return b

    def getBestMove(self,State):#Move
        bestaction = None;
        bestvalue = None;
        for act in State.getMoves(self.player):
            nextstate = State.play(act);
            value = self.alphabeta(nextstate,-49,49,self.prof);
            if bestvalue==None or value > bestvalue:
                bestvalue = value;
                bestaction = act;
        return bestaction
