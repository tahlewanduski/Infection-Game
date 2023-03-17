
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 08:56:13 2022

@author: Felix
"""
import matplotlib.pyplot as plt
#from main3 import main_bis

class Data():
    def __init__(self,CmptBlue, CmptRed, Turn):
        self.CmptBlue = CmptBlue;
        self.CmptRed = CmptRed;
        self.Turn = Turn;
        self.resultats =  [];
        
    def miseAJourRes(self):
        self.resultats.append((self.CmptBlue,self.CmptRed));
        
        
    def traitement(self):
        
        plt.figure();
        plt.plot([i for i in range(self.Turn)],
                 [ b for b, n in self.resultats], color='b', label="Bleu Alphabeta");
        plt.plot([i for i in range(self.Turn)],
                 [ n for b, n in self.resultats], color='r', label="Rouge MinMAx");
        plt.grid();
        plt.legend();
        plt.title("Nombre de noeuds visités par AlphaBeta et MinMAx");
        plt.ylabel("Nombre de Noeuds");
        plt.xlabel("tours");
        plt.savefig("Graphe3AB.png");
        
        """ 
         #graph pour MinMax 
         plt.figure();
         plt.plot([i for i in range(self.Turn)],[
             b for b, n in self.resultats], color='b', label="Bleu");
         plt.plot([i for i in range(self.Turn)],[
             n for b, n in self.resultats], color='r', label="Rouge");
         plt.grid();
         plt.legend();
         plt.title("Nombre de noeuds visités par MinMax");
         plt.ylabel("Nombre de Noeuds");
         plt.xlabel("tours");
         plt.savefig("Graphe2AB.png");
         """