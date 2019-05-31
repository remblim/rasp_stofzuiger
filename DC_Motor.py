import RPi.GPIO as GPIO
import time


class dc_motor():
	def __init__(self):
		self.GPIO_output = [14,15,18,23]
		GPIO.setup(self.GPIO_output,GPIO.OUT)

	def forward_right(self,speed):
		GPIO.output(14,1)
		GPIO.output(15,0)

	def backward_right(self,speed):
		GPIO.output(14,0)
		GPIO.output(15,1)
		print('1 backward')
	def stop_right(self):
		GPIO.output(14,0)
		GPIO.output(15,0)

	def forward_left(self,speed):
		GPIO.output(18,0)
		GPIO.output(23,1)

	def backward_left(self,speed):
		GPIO.output(18,1)
		GPIO.output(23,0)
		print('2 backward')

	def stop_left(self):
		GPIO.output(18,0)
		GPIO.output(23,0)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()
	motor = dc_motor()
	print('rechts vooruit')
	motor.forward_right(1)
	motor.stop_right()
	time.sleep(10)
	print('rechts stop')
	motor.stop_right()
	time.sleep(1)
	print('rechts achteruit')
	motor.backward_right(1)
	time.sleep(10)
	print('rechts stop')
	motor.stop_right()
	time.sleep(1)
	print('links vooruit')
	motor.forward_left(1)
	motor.stop_left()
	time.sleep(10)
	print('links stop')
	motor.stop_left()
	time.sleep(1)
	print('links achteruit')
	motor.backward_left(1)
	time.sleep(10)
	GPIO.cleanup()
	print('einde')
