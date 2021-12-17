# servo2.py

from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
channels = [0] # adapt to your wiring
a = 8.1  # adapt to your servo
b = 1.6  # adapt to your servo

def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(direction):
    duty = a / 180 * direction + b
    for i in channels:
        pwm.setDuty(i,duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(0.4) # allow to settle

print "starting"
setup()
#for direction in range(0, 181, 10):
#    setDirection(direction)
#direction = 0
setDirection(0)
print "should be on 180"
time.sleep(1)
setDirection(90)
time.sleep(1)
print "should end on 90"
#setDirection(180)
print "done"
