
#The Diagnostics object is designed to hold vehicle diagnostic data obtained by reading from the OBD-II port. 

import obd

class Diagnostics:
    MAX_SPEED = 120.0
    MAX_RPM = 9000.0
    MAX_OILTEMP = 100.0
    MIN_OILTEMP = -20
    connection = obd.OBD()

    def __init__(self, speed=0.0, RPM=0.0, oilTemp=70.0, fuelLevel=0.0, engineLight=False):
        self.speed = speed
        self.RPM = RPM
        self.oilTemp = oilTemp
        self.engineLight = engineLight
        self.fuelLevel = fuelLevel

        
    def __str__(self):
        return "speed: " + str(self.speed)

    def CANUpdate():
        return

    def speedFetch(self):
        cmd = obd.commands.SPEED
        response = connection.query(cmd)
        self.speed = response.value.to("mph") 

    def RPMFetch(self):
        cmd = obd.commands.RPM
        response = connection.query(cmd)
        self.RPM = response.value

    def oilTempFetch(self):
        cmd = obd.commands.OIL_TEMP
        response = connection.query(cmd)
        self.oilTemp = response.value

    def engineLightFetch(self):
        return

    def fuelLevelFetch(self):
        cmd = obd.commands.query(cmd)
        response = connection.query(cmd)
        self.fuelLevel = response.value

