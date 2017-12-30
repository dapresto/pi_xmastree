## version 1 with defaults from pihut script
## version 1a with longer pause.. using led.source_delay value in seconds
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import time
tree = LEDBoard(*range(2,28),pwm=True)
for led in tree:
    led.source_delay = 0.2
    led.source = random_values()
pause()
##
##
##
##
