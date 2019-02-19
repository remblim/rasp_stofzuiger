import RPi.GPIO as GPIO

class encoder():
	def init(self,self.GPIO_CONNECT):
		GPIO.setup(self.GPIO_CONNECT, GPIO.IN)
		GPIO.add_event_detect(self.GPIO_CONNECT, GPIO.BOTH,callback=count bouncetime = 10)
		self.count = 0
	
	def count(self)
		self.count += 1
		
if __name__ == "__main__":
	import time
	GPIO.setmode(GPIO.BCM)
	encoder = encoder(8)
	while True:
		time.sleep(0.5)
		print(encoder.count)		
	GPIO.cleanup()