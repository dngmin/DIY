import numpy as np

class Pitcher():
    def __init__(self,control,velocity):
        self.control = control
        self.velocity = velocity
    
    def pitcher_ability(self):
        control_p = ((1 / (1 + np.exp(-self.control/40)) * 200 -90)) / 100
        velocity = ((1 / (1 + np.exp(-self.velocity/50)) * 280 - 76))

        return control_p, velocity