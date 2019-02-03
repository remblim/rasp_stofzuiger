import time
import RPi.GPIO as GPIO
from stappenmotor import *
from ultrasoonsensor import *

class scanner():
	def __init__(self):
		GPIO.setmode(GPIO.BCM(
		

