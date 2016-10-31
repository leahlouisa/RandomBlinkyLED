import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
First_LED = 5

timer_max_1 = randrange(4, 11)
timer_count_1 = 0

GPIO.output(First_LED, False)
first_led_state = 0

while True:
    if (timer_count_1>=timer_max_1):
        if (first_led_state==0):
            first_led_state=1
        else:
            first_lef_state=0
        timer_count_1=0
    timer_count_1+=1
    timer_max_1 = randrange(4, 11)
    time.sleep(0.2)
