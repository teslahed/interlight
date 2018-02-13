import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input = GPIO.input(16)

try:

    while True:
        if (GPIO.input(16) == 0):
            print("Button Pressed!")
        else:
            print("NOT pressed")

        time.sleep(0.14)

except KeyboardInterrupt:
        GPIO.cleanup()
