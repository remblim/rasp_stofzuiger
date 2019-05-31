import RPi.GPIO as GPIO
import time


class dc_motor():
	def __init__(self):
		self.GPIO_output = [8,22,12,16]
		GPIO.setup(self.GPIO_output,GPIO.OUT)

	def forward_1(self,speed):
		GPIO.output(8,1)
		GPIO.output(22,0)

	def backward_1(self,speed):
		GPIO.output(8,0)
		GPIO.output(22,1)
		print('1 backward')
	def stop_1(self):
		GPIO.output(8,0)
		GPIO.output(22,0)

	def forward_2(self,speed):
		GPIO.output(12,0)
		GPIO.output(16,1)

	def backward_2(self,speed):
		GPIO.output(12,1)
		GPIO.output(16,0)
		print('2 backward')

	def stop_2(self):
		GPIO.output(12,0)
		GPIO.output(16,0)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.cleanup()
	motor = dc_motor()
	print('rechts vooruit')
	motor.forward_1(1)
	motor.stop_2()
	time.sleep(10)
	print('rechts stop')
	motor.stop_1()
	time.sleep(1)
	print('rechts achteruit')
	motor.backward_1(1)
	time.sleep(10)
	motor.stop_1()
	time.sleep(1)
	print('links vooruit')
	motor.forward_2(1)
	motor.stop_1()
	time.sleep(10)
	print('links stop')
	motor.stop_2()
	time.sleep(1)
	print('links achteruit')
	motor.backward_2(1)
	time.sleep(10)
	GPIO.cleanup()
	print('einde')
