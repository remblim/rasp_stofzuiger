import RPi.GPIO as GPIO
import time


class dc_motor():
	def __init__(self):
		self.GPIO_output = [8,10,12,16]
		GPIO.setup(self.GPIO_output,GPIO.OUT)
		self.one = GPIO.PWM(8,1000).start(0)
		self.two = GPIO.PWM(10,1000).start(0)
		self.three = GPIO.PWM(12,1000).start(0)
		self.forr = GPIO.PWM(16,1000).start(0)
		
	def forward_right(self,speed):
		self.one.ChangeDutyCycle(speed*100)
		self.two.ChangeDutyCycle(0)

	def backward_right(self,speed):
		self.one.ChangeDutyCycle(0)
		self.two.ChangeDutyCycle(speed*100)
		
	def stop_right(self):
		self.one.ChangeDutyCycle(0)
		self.two.ChangeDutyCycle(0)

	def forward_left(self,speed):
		self.three.ChangeDutyCycle(0)
		self.forr.ChangeDutyCycle(speed*100)

	def backward_left(self,speed):
		self.three.ChangeDutyCycle(0)
		self.forr.ChangeDutyCycle(speed*100)

	def stop_left(self):
		self.three.ChangeDutyCycle(0)
		self.forr.ChangeDutyCycle(0)

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.cleanup()
	motor = dc_motor()
	motor.stop_left()
	motor.stop_right()
	print('rechts vooruit')
	motor.forward_right(1)
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
	time.sleep(10)
	print('links stop')
	motor.stop_left()
	time.sleep(1)
	print('links achteruit')
	motor.backward_left(1)
	time.sleep(10)
	motor.stop_left()
	GPIO.cleanup()
	print('einde')
