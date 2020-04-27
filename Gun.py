import RPi.PGIO as GPIO

GPIO.setmode(GPIO.BCM)


switch = 24

GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.add_event_detect(switch, GPIO.RISING, callback = Lazer)

try:
    while True:
        print "0"

except KeyboardInterrupt:
    GPIO.cleanup()
