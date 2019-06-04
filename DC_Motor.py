import RPi.GPIO as GPIO
import time


class dc_motor():
	def __init__(self):
		self.GPIO_output = [8,10,12,16]
		GPIO.setup(self.GPIO_output,GPIO.OUT)
		self.one = GPIO.PWM(8,1000)
		self.two = GPIO.PWM(10,1000)
		self.three = GPIO.PWM(12,1000)
		self.forr = GPIO.PWM(16,1000)
		
		self.one.start(0)
		self.two.start(0)
		self.three.start(0)
		self.forr.start(0)
		
		self.accelerate_time = 3
		self.decelerate_time = 3
		self.max_speed = 1
		self.min_speed = 0.3
		self.r_speed = 0
		self.l_speed = 0
		self.l_target_speed = 0
		self.r_target_speed = 0
		
		self.tijd = time.time()
	
	def step(self):
		acceleration = 0.001
		deceleration = -0.001
		delta_tijd = time.time() - self.tijd
		
		if self.r_speed < self.r_target_speed: #versnelling
			print('versnelling')
			self.r_speed = self.r_speed + acceleration * delta_tijd
			if self.r_speed > 1:
				self.r_speed = 1
			if self.r_speed < self.min_speed:
				self.r_speed = self.min_speed
		elif self.r_speed > self.r_target_speed: #vertraging
			print('vertraging')
			self.r_speed = self.r_speed + deceleration * delta_tijd
			if self.r_speed > 1:
				self.r_speed = 1
			if self.r_speed < self.min_speed:
				self.r_speed = 0
		
		if self.l_speed < self.l_target_speed: #versnelling
			print('versnelling')
			self.l_speed = self.l_speed + acceleration * delta_tijd
			if self.l_speed > 1:
				self.l_speed = 1
			if self.l_speed < self.min_speed:
				self.l_speed = self.min_speed
		elif self.l_speed > self.r_target_speed: #vertraging
			print('vertraging')
			self.l_speed = self.l_speed + deceleration * delta_tijd
			if self.l_speed > 1:
				self.l_speed = 1
			if self.l_speed < self.min_speed:
				self.l_speed = 0
		print(self.l_speed,self.r_speed)
		self.one.ChangeDutyCycle(self.l_speed*100)
		self.two.ChangeDutyCycle(0)
		self.three.ChangeDutyCycle(0)
		self.forr.ChangeDutyCycle(self.r_speed*100)

	def forward_right(self,speed):
		self.r_target_speed = speed

	def backward_right(self,speed):
		self.one.ChangeDutyCycle(0)
		self.two.ChangeDutyCycle(speed*100)
		
	def stop_right(self):
		self.r_target_speed = 0

	def forward_left(self,speed):
		self.l_target_speed = speed

	def backward_left(self,speed):
		self.three.ChangeDutyCycle(speed*100)
		self.forr.ChangeDutyCycle(0)

	def stop_left(self):
		self.l_target_speed = 0

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
