import time
from light import measure_temp


while True:

    print(measure_temp())
    time.sleep(1)
