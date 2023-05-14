from process.pitching_zone import pitching_zone
from process.pitcher import Pitcher
from process.hitter import Hitter
import random
import numpy as np
import time
import cv2



def play(pitcher_ability,hitter_ability):
    pitched = 0
    strike = 0
    ball = 0
    hitted = False

    while True:
        print(f'__________________________________\
              \n제 {pitched +1} 구')
        time.sleep(1)
        pitched+=1

        ball_speed = random.uniform(pitcher_ability[1]-20,pitcher_ability[1]) # 구속 폭 조정
        control = pitcher_ability[0] + (pitcher_ability[1] -10 - ball_speed)/100 # 구속 vs 제구 관계
        contact_p = hitter_ability[1] - (100**(ball_speed*0.005) - 25) / 100 # 구속 vs 컨택 관계

        strike_ball_rate = random.random()
        if control >= strike_ball_rate: # 스트라이크

            batting_eye_rate = random.random()
            if hitter_ability[0] >= batting_eye_rate: # 선구 여부 확인

                contact_rate = random.random()
                if contact_p >= contact_rate: # 컨택 여부 확인

                    hit_foul_rate = random.random()
                    if hit_foul_rate > 0.2: # 파울 여부 확인  
                        print('\n안타\n')
                        hitted = True

                    else:
                        print('빗맞으며 파울')
                        if strike == 2:
                            pass

                        else:
                            strike+=1

                else:
                    pitching_zone(True)
                    print('헛스윙 스트라이크')
                    strike+=1

            else:
                pitching_zone(True)
                print('룩킹 스트라이크!')
                strike+=1
        
        else: # 볼
            batting_eye_rate = random.random()
            if hitter_ability[0] >= batting_eye_rate: # 선구 여부확인
                pitching_zone(False)
                print('볼')
                ball+=1

            else:
                contact_rate = random.random()
                if contact_p / 2 >= contact_rate: # 컨택 여부 확인
                    print('걷어냅니다 파울')
                    if strike == 2:
                        pass

                    else:
                        strike+=1

                else:
                    pitching_zone(False)
                    print('헛스윙 스트라이크')
                    strike+=1
        
        print(f'구속 : {ball_speed}km/h')
        if strike == 3:
            print('\n삼진아웃!\n')
            break
        elif ball == 4:
            print('\n볼넷으로 출루\n')
            break
        elif hitted == True:
            break
        else:
            print(f'ball : {ball}\tstrike : {strike}\n')
            time.sleep(1)

tusu = Pitcher(80,72) # (제구력, 구속)
taja = Hitter(50,80,50) # (선구안, 컨택능력, 파워) | 파워는 추후 추가

play(tusu.pitcher_ability(),taja.hitter_ability())