# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 07:58:37 2022

@author: Felix
"""

from Algorithm import Algorithm

class Negamax(Algorithm):
    def __init__(self,player,prof):
        super().__init__(player,prof);
        self.compteur = 0;
        
        def negamax(self,s,d):
            if d == 0 or s.isOver():
                return s.getScore(self.player)
            else:
                m = None
                for i in s.getMoves(self.player):
                    m = max(m, -self.negamax(s.play(i), d-1));
                return m

        def getBestMove(self,State):#Move
            bestaction = None;
            bestvalue = None;
            for act in State.getMoves(self.player):
                nextstate = State.play(act);
                value = self.negamax(nextstate,self.prof);
                if bestvalue==None or value > bestvalue:
                    bestvalue = value;
                    bestaction = act;
            return bestaction