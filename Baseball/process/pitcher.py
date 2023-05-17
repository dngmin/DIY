import numpy as np
import random

class Pitcher():
    def __init__(self,control,velocity):
        self.control = control
        self.velocity = velocity
    
    def pitcher_ability(self):
        control_p = ((1 / (1 + np.exp(-self.control/40)) * 200 -90)) / 100
        velocity = ((1 / (1 + np.exp(-self.velocity/50)) * 280 - 76))

        return control_p, velocity

def pitcher_ball_control(pitcher_ability,catcher_decision):
    wild_pitching = False
    wild_pitching_rate = random.random()
    ball_speed = random.uniform(pitcher_ability[1]-20,pitcher_ability[1]) # 구속 폭 조정
    control = pitcher_ability[0] + (pitcher_ability[1] -10 - ball_speed)/100 # 구속 vs 제구 관계
    control_rate = random.random()

    if catcher_decision == True:
        if control >= control_rate:
            return True , ball_speed, wild_pitching
        else:
            if 0.1 - control * 0.1 >= wild_pitching_rate:
                wild_pitching = True
            return False, ball_speed, wild_pitching
    else:
        if control <= control_rate:
            return True, ball_speed, wild_pitching
        else:
            if 0.1 - control * 0.1 >= wild_pitching_rate:
                wild_pitching = True
            return False, ball_speed, wild_pitching