#python 3 test
from time import sleep
import sys

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(22, GPIO.OUT)

#prec = float(sys.argv[1])
#type = float(sys.argv[2])
#height = float(sys.argv[3])
typeDict = {0: "line", 1: "circle", 2: "square"}
print("argv[1]: " + sys.argv[1])
print("argv[2]: " + sys.argv[2])
print("argv[2]: " + typeDict[int(sys.argv[2])])
print("argv[3]: " + sys.argv[3])