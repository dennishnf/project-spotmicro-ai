# Servo1.py

import RPi.GPIO as GPIO
import time
import sys

P_SERVO = 7 # adapt to your wiring
fPWM = 50  # Hz (not higher with software PWM)
a = 8.70 #10
b = 2.5 #2

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO, GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.ChangeDutyCycle(duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(1) # allow to settle

print "starting"
direction = int(sys.argv[1])
setup()
setDirection(direction)
for direction in range(0, 181, 10):
    setDirection(direction)
#direction = 0    
#setDirection(0)    
GPIO.cleanup() 
print "done"  
