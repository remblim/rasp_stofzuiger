import RPi.GPIO as GPIO

class encoder:
	def __init__(self,connect):
		print('initializing encoder channel ',connect)
		self.counter = 0
		self.GPIO_CONNECT = connect
		GPIO.setup(self.GPIO_CONNECT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(self.GPIO_CONNECT, GPIO.BOTH, callback=self.count ,bouncetime = 10)

	def count(self,channel):
		self.counter += 1

if __name__ == "__main__":
	import time
	GPIO.setmode(GPIO.BOARD)
	encod = encoder(8)
	try:
		while True:
			time.sleep(0.5)
			print(encod.counter)
	except KeyboardInterrupt:
		GPIO.cleanup()
		print('ended and cleaning up')
