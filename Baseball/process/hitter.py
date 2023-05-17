import numpy as np
import random

class Hitter():
    def __init__(self,batting_eye,contact,power):
        self.batting_eye = batting_eye  
        self.contact = contact
        self.power = power
    
    def hitter_ability(self):
        batting_eye_p = (5 + (1 / (1 + np.exp(-self.batting_eye/50)) * 210 - 100)*0.9) / 100
        contact_p = (5 + (1 / (1 + np.exp(-self.contact/50)) * 210 - 100)*0.9) / 100
        # power_ability = # 추후 추가

        return batting_eye_p, contact_p, self.power

def hitting(hitter_ability,ball_speed,ball_or_strike,ball,strike,caught,wild_pitching):
    hitted = False
    contact_p = hitter_ability[1] - (100**(ball_speed*0.005) - 25) / 100 # 구속 vs 컨택 관계
    batting_eye_rate = random.random()
    contact_rate = random.random()
    foul_rate = random.random()

    if not caught and wild_pitching:
        print('볼 뒤로 빠집니다')
        ball+=1
    else:
        if ball_or_strike == True: # 스트라이크
            if hitter_ability[0] >= batting_eye_rate: # 선구 성공
                if contact_p >= contact_rate:
                    if foul_rate > 0.2: # 파울 여부
                        hitted = True
                    else:
                        print('빗맞으며 파울')
                        if strike == 2:
                            pass
                        else:
                            strike+=1
                else:
                    print('헛스윙 스트라이크')
                    strike+=1
            else:
                print('룩킹 스트라이크')
                strike+=1
        else:
            if hitter_ability[0] >= batting_eye_rate:
                print('볼')
                ball+=1
            else:
                if contact_p/2 >= contact_rate:
                    print('걷어냅니다. 파울')
                    if strike == 2:
                        pass
                    else:
                        strike+=1
                else:
                    print('헛스윙 스트라이크')
                    strike+=1
    
    return ball, strike,hitted