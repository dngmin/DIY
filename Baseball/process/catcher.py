import numpy as np
import random

class Catcher():
    def __init__(self,blocking):
        self.blocking = blocking
    
    def catcher_ability(self):
        blocking_p = (1 / (1 + np.exp(-self.blocking/70)) * 280 - 127) / 100
        
        return blocking_p,True

def strike_ball_dicesion(ball,strike):
    dicesion = random.random()

    if  (ball == 3 and strike == 0) or (ball == 3 and strike == 1) or (ball == 3 and strike == 2):
        strike_p = 0.9
    elif (ball == 0 and strike ==0) or (ball == 2 and strike == 0):
        strike_p = 0.7
    elif (ball == 1 and strike == 0) or (ball == 2 and strike == 1) or (ball == 2 and strike == 2):
        strike_p = 0.6
    elif (ball == 0 and strike == 1) or (ball == 1 and strike == 1):
        strike_p = 0.5
    elif (ball == 0 and strike == 2) or (ball == 1 and strike == 2):
        strike_p = 0.4
    
    if strike_p >= dicesion:
        return True
    else:
        return False

def catcher_catching(catcher_ability,ballspeed,wild_pitching):
    catch_rate = random.random()

    if wild_pitching:
        catch_p = catcher_ability[0] - 0.5
    else:
        catch_p = catcher_ability[0]

    if catch_p >= catch_rate:
        caught = True
    else:
        caught = False


    return caught