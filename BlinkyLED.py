mport time
import RPi.GPIO as GPIO
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
First_LED = 5
Second_LED = 13

timer_max_1 = random.randrange(4, 11)
timer_count_1 = 0
timer_max_2 = random.randrange(4,11)
timer_count_2 = 0


GPIO.setup(First_LED, GPIO.OUT)
GPIO.output(First_LED, False)
first_led_state = 0

GPIO.setup(Second_LED, GPIO.OUT)
GPIO.output(Second_LED, False)
second_led_state = 0

while True:
    timer_count_1 = timer_count_1 + 1
    timer_count_2 = timer_count_2 + 1
    if (timer_count_1>=timer_max_1):
        if (first_led_state==0):
            first_led_state=1
            GPIO.output(First_LED, True)
        else:
            first_led_state=0
            GPIO.output(First_LED, False)
        timer_count_1=0
        timer_max_1 = random.randrange(4, 11)
    if (timer_count_2>=timer_max_2):
        if (second_led_state==0):
            second_led_state=1
            GPIO.output(Second_LED, True)
        else:
            second_led_state=0
            GPIO.output(Second_LED, False)
        timer_count_2=0
        timer_max_2 = random.randrange(4,11)
    time.sleep(0.2)

