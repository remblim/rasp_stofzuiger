import RPi.GPIO as GPIO
import time

class ultrasonic_sensor():
	def __init__(self):
		self.GPIO_TRIGGER = 18
		self.GPIO_ECHO = 24

		GPIO.setup(self.GPIO_TRIGGER,GPIO.OUT)
		GPIO.setup(self.GPIO_ECHO,GPIO.IN)

	def measure_distance(self):
		GPIO.output(self.GPIO_TRIGGER, True)

		time.sleep(0.0001)
		GPIO.output(self.GPIO_TRIGGER, False)

		StartTime = time.time()
		StopTime = time.time()

		while GPIO.input(self.GPIO_ECHO) == 0:
			StartTime = time.time()

		while GPIO.input(self.GPIO_ECHO) == 1:
			StopTime = time.time()

		TimeElapsed = StopTime - StartTime

		distance = (TimeElapsed * 34300) / 2

		return distance

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	ultra = ultrasonic_sensor()
	distance = ultra.measure_distance()
	print(distance)
	GPIO.cleanup()
