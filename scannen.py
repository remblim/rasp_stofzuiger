import time
import RPi.GPIO as GPIO
from stappenmotor import *
from ultrasoonsensor import *

class scanner():
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		self.ultra_sensor = ultrasonic_sensor()
		self.stepper = stappenmotor()
		self.steps_per_round = 520
		
	def scannen(self):
		i = 0
		distance = []
		while i < self.steps_per_round:
			distance.extend(self.ultra_sensor.measure_distance())
			self.stepper.cw(1)
			i += 1
		
		self.stepper.ccw(self.steps_per_round)
		
if __name__ == "__main__":
	scan = scanner()
	scan.scannen()
	GPIO.cleanup()
	print('einde')
