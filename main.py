import numpy as np
import random

def Always_COO(p,i): # Player Always Choose Cooperate.
    # p : The Player Actions.
    p[i] = 0 # 0 Represents the Cooperate Action.
    return p[i] # Return The Next Action of the player.

def Always_DEF(p,i): # Player Always Choose Defect.
    # p : The Player Actions.
    p[i] = 1  # 1 Represents the Defect Action.
    return p[i] # Return The Next Action of the player.

def Tit_For_Tat(p1,p2,i): # Player Cooperate in the first round. Then in each subsequent round, play the opponent's action in the previous round.
    # p1 : The Player 1  Actions.
    # p2 : The Player 2  Actions.
    if(i == 0):
        p1[i] = 0 # Make the first round of the player Cooperate.
    else:
        p1[i] = p2[i-1] # The other rounds is the opponent's action in the previous round.
    return p1[i] # Return The Next Action of the player.


def Suspicious_TFT(p1,p2,i): # Player Defect in the first round. Then in each subsequent round, play the opponent's action in the previous round.
    # p1 : The Player 1  Actions.
    # p2 : The Player 2  Actions.
    if(i == 0):
        p1[i] = 1 # Make the first round of the player Defect.
    else:
        p1[i] = p2[i-1] # The other rounds is the opponent's action in the previous round.
    return p1[i] # Return The Next Action of the player.


def Reverse_TFT(p1,p2,i): # Defect in the first round, then plays the reverse of the opponent's action in the previous round.
    # p1 : The Player 1  Actions.
    # p2 : The Player 2  Actions.
    if(i == 0):
        p1[i] = 1 # Make the first round of the player Defect.
    else:
        p1[i] = 1 - p2[i-1] # The other rounds is the Reverse of the opponent's action in the previous round.
    return p1[i] # Return The Next Action of the player.


def Random(p,i): # In each round, cooperate or defect with equal probabilities.
    # p : The Player Actions.
    actions = [0,1] # The possible actions to be choosen.
    p[i] = random.choice(actions) # Make the action Cooperate or defect based on equal probabilities.
    return p[i] # Return The Next Action of the player.


def Naive_Prober(p1,p2,i): #Cooperate in the first round. Then in each subsequent round, play the opponent's action in the previous round, but sometimes defect in lieu of cooperation with some probability.
    # p1 : The Player 1  Actions.
    # p2 : The Player 2  Actions.
    if(i == 0):
        p1[i] = 0 # Make the first round of the player Defect.
    else:
        r = random.random() # Random Number to check the probability of make the next action to be defect
        if( 0 < r < 0.001):
            p1[i] = 1
        else:
            p1[i] = p2[i-1] # if not we will do same as we did in normal Tit For Tat
    return p1[i] # Return The Next Action of the player.


def calc_payoffs(p1,p2,payoff_matrix): # function to  calculate the payoffs
    fit1 = 0
    fit2 = 0
    for i in range(len(p1,)):
        fit1 += payoff_matrix[1-p1[i],1-p2[i]][0]
        fit2 += payoff_matrix[1-p1[i],1-p2[i]][1]
    return fit1,fit2


def IPDGame(Strategy1,Strategy2,p1,p2):
    for i in range(50):
        if(Strategy1 == 'Always Cooperate'):
            p1[i] = Always_COO(p1,i)
        if(Strategy1 == 'Always Defect'):
            p1[i] = Always_DEF(p1,i)
        if(Strategy1 == 'Tit For Tat'):
            p1[i] = Tit_For_Tat(p1,p2,i)
        if(Strategy1 == 'Suspicious Tit For Tat'):
            p1[i] = Suspicious_TFT(p1,p2,i)
        if(Strategy1 == 'Reverse Tit for Tat'):
            p1[i] = Reverse_TFT(p1,p2,i)
        if(Strategy1 == 'Random'):
            p1[i] = Random(p1,i)
        if(Strategy1 == 'Naive Prober'):
            p1[i] = Naive_Prober(p1,p2,i)
        if(Strategy2 == 'Always Cooperate'):
            p2[i] = Always_COO(p2,i)
        if(Strategy2 == 'Always Defect'):
            p2[i] = Always_DEF(p2,i)
        if(Strategy2 == 'Tit For Tat'):
            p2[i] = Tit_For_Tat(p2,p1,i)
        if(Strategy2 == 'Suspicious Tit For Tat'):
            p2[i] = Suspicious_TFT(p2,p1,i)
        if(Strategy2 == 'Reverse Tit for Tat'):
            p2[i] = Reverse_TFT(p2,p1,i)
        if(Strategy2 == 'Random'):
            p2[i] = Random(p2,i)
        if(Strategy2 == 'Naive Prober'):
            p2[i] = Naive_Prober(p2,p1,i)

    payoff_matrix = np.array([[(3, 3), (5, 0)], [(0, 5), (1,1)]], dtype=object)
    fit1,fit2 = calc_payoffs(p1,p2,payoff_matrix)
    if(fit1 > fit2):
        print("The Winning Strategy is : " + Strategy1 + " Which belongs to Player 1" )
    elif(fit2 > fit1):
        print("The Winning Strategy is : " + Strategy2 + " Which belongs to Player 2" )
    else:
        print("Draw Game, Meaning that The two strategies are equal")


p1 = np.zeros(50,dtype=int)
p2 = np.zeros(50,dtype=int)

IPDGame("Always Cooperate","Tit For Tat",p1,p2)
IPDGame("Always Defect","Tit For Tat",p1,p2)
IPDGame("Always Defect","Suspicious Tit For Tat",p1,p2)
IPDGame("Reverse Tit for Tat","Suspicious Tit For Tat",p1,p2)
print(".....................................")
for i in range(10):
    IPDGame("Always Cooperate","Random",p1,p2)
for i in range(10):
    IPDGame("Tit For Tat"," Random",p1,p2)
for i in range(10):
    IPDGame("Suspicious Tit For Tat","Naive Prober",p1,p2)
