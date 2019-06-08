import RPi.GPIO as GPIO
import time


class dc_motor():
	def __init__(self):
		self.GPIO_output = [8,10,12,16]
		GPIO.setup(self.GPIO_output,GPIO.OUT)
		self.one = GPIO.PWM(8,10000)
		self.two = GPIO.PWM(10,10000)
		self.three = GPIO.PWM(12,10000)
		self.forr = GPIO.PWM(16,10000)
		
		self.one.start(0)
		self.two.start(0)
		self.three.start(0)
		self.forr.start(0)
		
		self.accelerate_time = 1
		self.decelerate_time = 1
		self.max_speed = 1
		self.min_speed = 0.3
		self.r_speed = 0
		self.l_speed = 0
		self.l_target_speed = 0
		self.r_target_speed = 0
		
		self.tijd = time.time()
	
	def step(self):
		print(self.accelerate_time,self.decelerate_time)
		print(self.max_speed)
		acceleration = (self.max_speed - self.min_speed)/self.accelerate_time
		deceleration = -(self.max_speed - self.min_speed)/self.decelerate_time
		delta_tijd = time.time() - self.tijd
		
		if self.r_speed < self.r_target_speed: #versnelling
			self.r_speed = self.r_speed + acceleration * delta_tijd
			if self.r_speed > self.max_speed-self.min_speed:
				self.r_speed = self.max_speed-self.min_speed
			if self.r_speed < -self.max_speed+self.min_speed:
				self.r_speed = -self.max_speed+self.min_speed
		elif self.r_speed > self.r_target_speed: #vertraging
			self.r_speed = self.r_speed + deceleration * delta_tijd
			if self.r_speed > self.max_speed-self.min_speed:
				self.r_speed = self.max_speed-self.min_speed
			if self.r_speed < -self.max_speed+self.min_speed:
				self.r_speed = -self.max_speed+self.min_speed
		
		if self.l_speed < self.l_target_speed: #versnelling
			self.l_speed = self.l_speed + acceleration * delta_tijd
			if self.l_speed > self.max_speed-self.min_speed:
				self.l_speed = self.max_speed-self.min_speed
			if self.l_speed < -self.max_speed+self.min_speed:
				self.l_speed = -self.max_speed+self.min_speed
		elif self.l_speed > self.l_target_speed: #vertraging
			self.l_speed = self.l_speed + deceleration * delta_tijd
			if self.l_speed > self.max_speed-self.min_speed:
				self.l_speed = self.max_speed-self.min_speed
			if self.l_speed < -self.max_speed+self.min_speed:
				self.l_speed = -self.max_speed+self.min_speed
		
		if self.r_speed < 0.1 and self.r_target_speed == 0 and self.r_speed > -0.1:
			self.r_speed = 0
			
		if self.l_speed < 0.1 and self.l_target_speed == 0 and self.l_speed > -0.1:
			self.l_speed = 0

		if self.r_speed < 0:
			self.speed_one = 0
			self.speed_two = -self.r_speed + self.min_speed
		elif self.r_speed > 0:
			self.speed_two = 0
			self.speed_one = self.r_speed + self.min_speed
		else:
			self.speed_one = 0
			self.speed_two = 0
			
			
		if self.l_speed < 0:
			self.speed_forr = 0
			self.speed_three = -self.l_speed + self.min_speed
		elif self.l_speed > 0:
			self.speed_three = 0
			self.speed_forr = self.l_speed + self.min_speed
		else:
			self.speed_three = 0
			self.speed_forr = 0
		
		self.one.ChangeDutyCycle(self.speed_one*100)
		self.two.ChangeDutyCycle(self.speed_two*100)
		self.three.ChangeDutyCycle(self.speed_three*100)
		self.forr.ChangeDutyCycle(self.speed_forr*100)
		self.tijd = time.time()

	def forward_right(self,speed):
		self.r_target_speed = speed
		
	def backward_right(self,speed):
		self.r_target_speed = -speed
		
	def stop_right(self):
		self.r_target_speed = 0

	def forward_left(self,speed):
		self.l_target_speed = speed

	def backward_left(self,speed):
		self.l_target_speed = -speed

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
