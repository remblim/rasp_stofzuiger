import RPi.GPIO as GPIO
import time 


class dc_motor():
	def __init__(self):
		self.GPIO_output = [12,16,20,21]
		GPIO.setup(self.GPIO_output,GPIO.OUT)
	
	def forward_1(self,speed):
		GPIO.output(self.GPIO_output[0],1)

	def backward_1(self,speed):
		GPIO.output(self.GPIO_output[0],0)	

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	motor = dcmotor()
	motor.forward_1(1)
	time.sleep(1)
	motor.backward_1(1)
	GPIO.cleanup()
	print('einde')