import numpy as np
import random
import cv2

def pitching_zone(strike):
    img = cv2.imread('process/pitching_zone.png')

    if strike == True:
        strike_height = random.randint(259,346)
        strike_width = random.randint(238,325)
        cv2.circle(img,(strike_width,strike_height),10,(255,255,255),-1,cv2.LINE_AA)

        cv2.imshow('pitching_zone',img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    else:
        pass