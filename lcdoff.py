# import modules
import lcddriver as lcd
import os
import psutil as ps
from time import time
from time import sleep
from datetime import datetime

lcd = lcd.lcd()

# lcd.display_string("####################",1)
lcd.display_string("STOP LCD...",1)
lcd.display_string("SHUTDOWN...",2)
# lcd.display_string("####################",4)

sleep(5)

lcd.clear()
lcd.backlight_off()
