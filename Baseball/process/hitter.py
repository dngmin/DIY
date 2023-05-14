import numpy as np

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