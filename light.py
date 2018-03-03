#Chris Telford christophertelford@yahoo.co.uk 11/02/2018
#This is the 'light' code for controlling the LED channels via PWMing the raspberry pi's GPIO pins.
#this works along side the main.py flask server code and the index.html website code.
#This is dodgy code hacked together by someone that doesn't know what they are doing based on an example found on youtube;
# https://www.youtube.com/watch?v=L55QYFnnrgo  Full credit to original creator of the code I am basing mine on. Thanks Adafruit Industries!


#I am using the pigpio library to handle PWMing the rapsberry pi GPIO pins. 
#It works better than other libraries I've tried for flicker free results.
#see abyz.me.uk/rpi/pigpio for details.

import pigpio       #import pigpio library.
pi = pigpio.pi()    #set 'pi' to access local pi pins. pigpio setup.
import os           #for temp sensor stuff
import time         #for temp sensor stuff

#set the pins for the colour channels going to the LED controller hardware from the pi. Ground connection also required.
redled = 23
greenled = 22
blueled = 25


#interlight object;
class interlight(object):
    """Raspberry Pi RGB LED controller. Chris Telford."""


    def __int__(self):
        """RGB Controller"""
        

    def set_redbright(self, value):
        pi.set_PWM_dutycycle(redled, (value))
        
    def set_greenbright(self, value):
        pi.set_PWM_dutycycle(greenled, (value))

    def set_bluebright(self, value):
        pi.set_PWM_dutycycle(blueled, (value))
