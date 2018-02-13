
import time
from light import interlight


# Create the pi thing.
pi_light = interlight()

# Print the current switch state.
switch = pi_light.read_switch()
print('Switch status: {0}'.format(switch))

