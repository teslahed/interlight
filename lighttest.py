
import time
from light import interlight
import os

# Create the pi thing.
pi_light = interlight()



temp = pi_light.measure_temp()
print(temp())
time.sleep(1)

