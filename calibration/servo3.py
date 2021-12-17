# servo3.py

from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
channels = [1,2,3,8,6,9,11] # adapt to your wiring
a = 7.7 # adapt to your servo
b = 2.9  # adapt to your servo

dict_motors = {1: [7.3,2.9], 2: [7.0,3.4], 3: [7.1,3.1], 4: [7.7,1.6], 5: [7.4,2.6], 6: [7.1,3.0], 7: [8.1,1.6], 8: [7.3,2.6], 9: [8.1,1.6], 10: [8.1,1.5], 11: [7.7,2.9$


def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(direction):
    for i in channels:
        duty = dict_motors[i][0] / 180 * direction + dict_motors[i][1]
        pwm.setDuty(i,duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(0.4) # allow to settle

def serialDirection(direction,motorid):
    duty = dict_motors[motorid][0] / 180 * direction + dict_motors[motorid][1]
    pwm.setDuty(motorid,duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(0.4) # allow to settle

def topLink():
    for direction in range(90,44,-5):
        setDirection(direction)
    for direction in range(45,91,5):
        setDirection(direction)

def wholeRange():
    for direction in range(90,181,10):
        setDirection(direction)
    for direction in range(180,-1,-10):
        setDirection(direction)
    for direction in range(0,91,10):
        setDirection(direction)

print "starting"
setup()



print "Moving first joint"
channels = [1,4,7,10]
setDirection(90)
topLink()
time.sleep(2)
print "Moving second joint"
channels = [2,5,8,11]
wholeRange()
time.sleep(2)
print "Moving third joint"
channels = [3,6,9,12]
wholeRange()
time.sleep(2)
print "Done"

