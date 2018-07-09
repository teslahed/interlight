# ChrisTelford christophertelford@yahoo.co.uk 11/02/2018
# This is the 'light' code for controlling the LED channels via PWMing the raspberry pi's GPIO pins.
# this works along side the main.py flask server code and the index.html website code.
# https://www.youtube.com/watch?v=L55QYFnnrgo  Full credit to original creator of the code I am basing mine on. Thanks Adafruit Industries!


# I am using the adafruit PCA9685 library and hardware because it works better for PWM than using the GPIO pins on the pi directly.
# see https://github.com/adafruit/Adafruit_Python_PCA9685 for more details.

from __future__ import division


import os           # for temp sensor stuff
import time         # for temp sensor stuff
import Adafruit_PCA9685	# for PWM hardware
 
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# set the pwm frequency for all pins. Valid between 40 and 1000 hertz.
pwm.set_pwm_freq(150)

# set the pins for the colour channels going to the LED controller hardware from the pi. Ground connection also required.
redled = 0
greenled = 1
blueled = 2

# interlight object;
class interlight(object):
    """Raspberry Pi RGB LED controller. Chris Telford."""


    def __int__(self):
        """RGB Controller"""
        
 
    def set_redbright(self, value):
        pwm.set_pwm(0, value, 4095)
	
        
    def set_greenbright(self, value):
        pwm.set_pwm(greenled, value, 4095)
        

    def set_bluebright(self, value):
        pwm.set_pwm(blueled, value, 4095)
