SENECHAL FELIX 
22003660

# Jeu d'infection et algorithmes d'intelligence artificielle

1.Présentation
2.Librairies nécessaire
3.Utilisation
4.Organisation

## Présentation
C'est un jeu d'infection classique entre des pions de deux couleurs différentes
(ici Rouge et Bleu)
les pions peuvent :
	-se deplacer de 2 cases dans toutes les directions diagonales comprises
	-créer un double a 1 cases autour d'eux dans toutes les directions diagonales comprises
	-chaque action amène a l'infection des pions adverses environnants.

Le jeu se termine si il n'y a pu de place, si une couleur a disparu du plateau, si 
les deux joueurs passent leurs tours ou si un coup a déjà été réalisé.

Le second but était d'implémenter des algorithmes d'intelligence artificielle tels que minimax, alphabeta (negamax).

Ici on confronte les Algorithmes, le rouge utilise toujours Minmax avec la profondeur que souhaite l'utilisateur et le bleu utilise l'algorithme que choisi l'utilisateur. 

##Librairies nécessaire

Il faut Python 3 avec les libraires 'copy', 'matplotlib'

## Utilisation

commande bash:
'''
python3 jeu.py <profondeur Bleu> <profondeur Rouge> <Utilisation alphabeta>
'''

'<profondeur Bleu>' : profondeur de raisonnement du joueur Bleu (Nombre entier positif)
'<profondeur Rouge>' : profondeur de raisonnement du joueur Rouge (Nombre entier positif)
'<Utilisation alphabeta>' : utilisation de l'algorithme AlphaBeta pour Bleu (String "False", "True")

Si jamais ça ne marche pas vous pouvez lancer la fonction main en lui passant les arguments ci dessus (par exemple depuis un ide comme spyder)

##Organisation

'Decision.py' contient le code des classes State et Move pour une grille de 7*7
'main.py' contient le code du main pour une grille de 7*7
'Decision2.py' contient le code des classes State et Move pour une grille de 5*5
'main2.py' contient le code du main pour une grille de 5*5
'Data.py' contient le code pour réaliser les graphiques avec matplotlib
'Algorithm.py' super classe dont herite Minmax, Alphabeta et Negamax
'MinMax.py'  contient le code de l'algorithme d'intelligence artificielle MinMax
'Alphabeta.py' contient le code de l'algorithme d'intelligence artificielle AlphaBeta
'Negamax.py' contient le code de l'algorithme d'intelligence artificielle NegaMax