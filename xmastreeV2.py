## version 1 with defaults from pihut script
## version 1a with longer pause.. using time.sleep(()
## and V2 controlling leds directly with numbers
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import random
import time

## tree = LEDBoard(*range(2,28),pwm=True)
lights = LEDBoard(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25) 
while True:
    i = int(random.uniform(1,25))
    lights.leds[i].toggle()
    time.sleep(0.10)
pause()
##
##
##
##
