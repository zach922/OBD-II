
#The Diagnostics object is designed to hold vehicle diagnostic data obtained by reading from the OBD-II port. 

class Diagnostics:
    MAX_SPEED = 120.0
    MAX_RPM = 9000.0
    MAX_OILTEMP = 100.0
    MIN_OILTEMP = -20

    def __init__(self, speed=0.0, tack=0.0, oilTemp=70.0, engineLight=False, gasLight=False):
        self.speed = speed
        self.tack = tack
        self.oilTemp = oilTemp
        self.engineLight = engineLight
        self.gasLight = gasLight

        
    def __str__(self):
        return "speed: " + str(self.speed)


