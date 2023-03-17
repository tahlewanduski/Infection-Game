#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:46:26 2022

@author: 22003660@campus
"""

import sys
#import random
from Data import Data
from Decision import State
from MinMax import MinMax
from AlphaBeta import AlphaBeta

def create(lin, col, init):
    #Retourne une liste de 'lin' listes de 'col' avec des valeurs 'init'
    return [[init] * col for _ in range(lin)]

def line_str(tab, i):
    #affiche proprement la ligne ``i`` de ``tab``."""
    return '|\t' + '\t'.join(str(val) for val in tab[i]) + '\t|'

def to_str(tab):
    #affiche proprement la grille de jeu
    res = ''
    for i in range(len(tab)):
        res += '\n' + line_str(tab, i)
    return res


A={"R":[(6,0),(0,6)],"B":[(0,0),(6,6)]}; #le board intiale pour la grille de 7 par 7


def init_TAB(board):
    """initialise tab pour une grille de jeu de 7*7
       remplie de point '.' sauf la ou se trouve les pions
       qui sont représentés par 'R' ou 'B' selon la couleur.
    """
    Tab = create(7,7,".")
    for i in range(len(board["R"])):
        x,y= board["R"][i]
        Tab[x][y] = "R"
    for i in range(len(board["B"])):
        x,y= board["B"][i]
        Tab[x][y] = "B"
    return Tab

def main(profB, profR, isalphaB):
    #main pour une grille de jeu de 7*7
    
    if not isinstance(profB, int) and profB < 1 and not isinstance(profR,int) and profR < 1:
        print("Error 1st or 2nd value not int");
        sys.exit();
    elif isalphaB == True:
        blue = AlphaBeta("B",profB);
    elif isalphaB == False:
        blue = MinMax("B",profB);
    else:
        print(isalphaB);
        print("Error 3rd entry not ok");
        sys.exit()

    S = State(A,"B",0,len(A["R"]),len(A["B"]),0);
    data = Data(0,0,0);
    print("....../ Tour n° ",S.turn ,"/......");
    print(S.board);
    print(to_str(init_TAB(S.board)));
    print("blue ",S.nBlue, "| Red ",S.nRed);

    red = MinMax("R",profR);
    while not S.isOver():
        p= S.player;
    #    Allmove = S.getMoves(p);
    #    nbMove = len(Allmove);
    #    print(S.player, " " ,nbMove);
        if p =="R":
            m= red.getBestMove(S);
        else:
            m = blue.getBestMove(S);
      #  m = random.randint(0,nbMove-1);
        S = S.play(m);

        print("....../ Tour n° ",S.turn ,"/......");
        print(S.board);
        print(to_str(init_TAB(S.board)));
        print("blue ",S.nBlue,"| Red ",S.nRed);
        data.Turn = S.turn;
        data.CmptBlue = blue.compteur;
        data.CmptRed = red.compteur;
        data.miseAJourRes();
        if S.isOver():
            print("FIN");
            data.traitement();
       # if (S in h): (code si coup deja joué arrivé trop souvent)
        #    print("deja joué");
         #   data.traitement();
          #  sys.exit();
          
if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Erreur d'usage : seulement 3 argument demandé {profondeur bleu} {profondeur rouge} {alphabeta}");
    
    main(int(sys.argv[0]),int(sys.argv[1]), bool(sys.argv[2]));
    print("Terminer");
