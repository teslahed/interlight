
import time
from light import interlight


# Create the pi thing.
pi_light = interlight()

# Print the current switch state.
red = pi_light.read_redbright(redled)
print('Redbright status: {0}'.format(red))

temp + pi_light.tempread
print(measure_temp())
time.sleep(1)

#blink LED forever
print('Blinking LED control-C to stop')
while True:
    pi_light.set_bright(0.5)
    time.sleep(0.5)
    pi_light.set_bright(1)
    time.sleep(0.5)

