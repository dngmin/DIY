from process.pitching_zone import pitching_zone
from process.pitcher import Pitcher,pitcher_ball_control
from process.hitter import Hitter,hitting
from process.catcher import Catcher,strike_ball_dicesion,catcher_catching
import random
import numpy as np
import time
import cv2



def play(pitcher_ability,hitter_ability,catcher_ability):
    pitched, ball ,strike = 0, 0, 0
    hitted = False

    while True:
        print(f'__________________________________\
              \n제 {pitched +1} 구')
        time.sleep(1)
        pitched+=1

        catcher_decision = strike_ball_dicesion(ball,strike)
        ball_or_strike, ball_speed, wild_pitching = pitcher_ball_control(pitcher_ability,catcher_decision)
        caught = catcher_catching(catcher_ability,ball_speed,wild_pitching)
        ball, strike, hitted = hitting(hitter_ability,ball_speed,ball_or_strike,ball,strike,caught,wild_pitching)

        if not hitted:
            print(f'구속 : {ball_speed}km/h')

        if strike == 3:
            print('\n삼진아웃!\n')
            break
        elif ball == 4:
            print('\n볼넷으로 출루\n')
            break
        elif hitted:
            print('안타')
            break
        else:
            print(f'ball : {ball}\tstrike : {strike}\n')
            time.sleep(1)

tusu = Pitcher(70,65) # (제구력, 구속)
taja = Hitter(50,80,50) # (선구안, 컨택능력, 파워) | 파워는 추후 추가
posu = Catcher(70)

play(tusu.pitcher_ability(),taja.hitter_ability(),posu.catcher_ability())