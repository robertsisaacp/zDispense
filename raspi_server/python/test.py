from sys import argv
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

#prec = float(sys.argv[1])
#type = float(sys.argv[2])
#height = float(sys.argv[3])
print argv[1]
print argv[2]
print argv[3]

if prec > 0:
    for i in range(0, 10):
        print i
        GPIO.output(22, GPIO.HIGH)
        sleep(1)
        GPIO.output(22, GPIO.LOW)
        sleep(1)

GPIO.cleanup()

#print("it worked!")

#sys.stdout.flush()

