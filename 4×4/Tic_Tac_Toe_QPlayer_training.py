import numpy as np
import tkinter as tk
import copy
import _pickle as cpickle
from Q_Learning_Tic_Tac_Toe import Game, QPlayer     # Classes used for Tic Tac Toe

root = tk.Tk()
epsilon = 0.9
player1 = QPlayer(mark="X",epsilon = epsilon)
player2 = QPlayer(mark="O",epsilon = epsilon)
game = Game(root, player1, player2)

N_episodes = 20
for episodes in range(N_episodes):
    game.play()
    game.reset()

Q = game.Q

filename = "Q-value{}.p".format(N_episodes)
cpickle.dump(Q, open(filename, "wb"),True)