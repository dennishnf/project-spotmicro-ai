from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module

#dict_motors = {1: [7.3,2.9], 2: [7.0,3.4], 3: [7.1,3.1], 4: [7.7,1.6], 5: [7.4,2.6], 6: [7.1,3.0], 7: [8.1,1.6], 8: [7.3,2.6], 9: [8.1,1.6], 10: [8.1,1.5], 11: [7.7,2.$
dict_motors = {1: [7.3,3.2], 2: [7.0,4.0], 3: [7.1,3.8], 4: [7.7,1.6], 5: [7.4,2.8], 6: [7.1,3.4], 7: [8.1,2.4], 8: [7.3,2.6], 9: [8.1,2.4], 10: [8.1,1.5], 11: [7.7,2.2$

def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)
    for i in range(12):
        print "Seting link " + str(i+1) + " to 90"
        channels = [i + 1]
        setDirection(90, channels)
        time.sleep(0.2)

def setDirection(direction, channels):
    duty = 0.0
    for i in channels:
        if i == 7:
            direction = (direction - 90)*-1 + 90
        duty = dict_motors[i][0] / 180 * direction + dict_motors[i][1]
        pwm.setDuty(i,duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(0.1) # allow to settle

def topLink(channels):
    for direction in range(90,59,-5):
        setDirection(direction, channels)
    for direction in range(60,91,5):
        setDirection(direction, channels)

def otherLink(channels):
    for direction in range(90,120,5):
        setDirection(direction,channels)
    for direction in range(120,59,-5):
        setDirection(direction, channels)
    for direction in range(60,91,5):
        setDirection(direction, channels)

def lastLink(channels):
    for direction in range(90,150,5):
        setDirection(direction,channels)
    for direction in range(150,29,-5):
        setDirection(direction, channels)
    for direction in range(30,91,5):
        setDirection(direction, channels)

def moveLeg(leg):
    aux = 3*(leg -1) + 1
    channels = [aux]
    print "Moving first joint of leg " + str(leg)
    time.sleep(2)
    topLink(channels)
    channels = [aux + 1]
    print "Moving second joint of leg " + str(leg)
    time.sleep(2)
    otherLink(channels)
    channels = [aux + 2]
    print "Moving third joint of leg " + str(leg)
    time.sleep(2)
    otherLink(channels)
    print "Finished moving leg " + str(leg)

def moveTwoLegs(leg1, leg2):
    aux = 3*(leg1 -1) + 1
    aux2 = 3*(leg2 -1) + 1
    channels = [aux, aux2]
    print "Moving first joint of legs " + str(leg1) + " and " + str(leg2)
    time.sleep(2)
    topLink(channels)
    channels = [aux + 1, aux2 +1]
    print "Moving second joint of legs " + str(leg1) + " and " + str(leg2)
    time.sleep(2)
    otherLink(channels)
    channels = [aux + 2, aux2 + 2]
    print "Moving third joint of legs " + str(leg1) + " and " + str(leg2)
    time.sleep(2)
    lastLink(channels)
    print "Finished moving legs " + str(leg1) + " and " + str(leg2)

def walk(leg1, leg2):
    aux = 3*(leg1 -1) + 1
    aux2 = 3*(leg2 -1) + 1
    channels1 = [aux + 1, aux2 + 1]
    channels2 = [aux + 2, aux2 + 2]
    for direction1 in range(90,34,-5):
        setTwoDirections(direction1, channels1, (90 - direction1) + 90, channels2)
    for direction1 in range(35,91,5):
        setTwoDirections(direction1, channels1, (90 - direction1) + 90, channels2)


def setTwoDirections(direction1, channels1, direction2, channels2):
    duty = 0.0
    for i in channels1:
        duty = dict_motors[i][0] / 180 * direction1 + dict_motors[i][1]
        pwm.setDuty(i,duty)
    for i in channels2:
        duty = dict_motors[i][0] / 180 * direction2 + dict_motors[i][1]
        pwm.setDuty(i,duty)
    #print "direction =", direction, "-> duty =", duty
    time.sleep(0.1) # allow to settle


print "starting"
setup()

#for i in range(10):
#    walk(1,3)

print "Done"


