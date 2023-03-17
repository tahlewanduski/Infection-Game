# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:17:42 2022

@author: Felix
"""
from Algorithm import Algorithm

class MinMax(Algorithm):
    def __init__(self,player,prof):
        super().__init__(player,prof);
        self.compteur = 0;

    def minimax(self,s,d):
        if d==0 or s.isOver():
            return s.getScore(self.player)
        else:
            self.compteur +=1;
            if self.player == s.player :#noeud de max
                b=None
                for i in s.getMoves(self.player):
                    m = self.minimax(s.play(i),d-1);
                    if b == None or b < m:
                        b = m
            else:
                b = float("+inf")
                for y in s.getMoves(s.player):
                    m = self.minimax(s.play(y),d-1);
                    if b > m:
                        b = m
            return b

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
            value = self.minimax(nextstate,self.prof);
            if bestvalue==None or value > bestvalue:
                bestvalue = value;
                bestaction = act;
        return bestaction
