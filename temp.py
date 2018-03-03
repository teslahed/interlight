import os
import time


def measure_temp( ):
            temp = os.popen("vcgencmd measure_temp").readline()
            return (temp.replace("temp=",""))
#            return (("temp=",""))

while True:
       print(measure_temp())
       time.sleep(1)
