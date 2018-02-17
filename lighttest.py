
import time
from light import interlight
import os

# Create the pi thing.
pi_light = interlight()



temp = pi_light.tempread
print(measure_temp())
time.sleep(1)

#blink LED forever
print('Blinking LED control-C to stop')
while True:
    pi_light.set_bright(0.5)
    time.sleep(0.5)
    pi_light.set_bright(1)
    time.sleep(0.5)

