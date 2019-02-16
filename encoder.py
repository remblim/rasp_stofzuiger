import RPi.GPIO as GPIO

class encoder():
	def init(self,self.GPIO_CONNECT):
		GPIO.setup(self.GPIO_CONNECT, GPIO.IN)
		GPIO.add_event_detect(self.GPIO_CONNECT, GPIO.BOTH,callback=count bouncetime = 10)
		self.count = 0
	
	def count(self)
		self.count += 1