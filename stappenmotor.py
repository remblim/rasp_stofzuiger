import RPi.GPIO as GPIO
import time 


class stappenmotor():
	def __init__(self):
		self.GPIO_output = [2,3,4,17]
		GPIO.setup(self.GPIO_output,GPIO.OUT)
		self.gedane_stappen = 0

	def cw(self,stappen):
		i = 0
		while i < stappen:
			print(i)
			GPIO.output(self.GPIO_output[self.gedane_stappen%4],1)
			GPIO_low = self.GPIO_output.copy()
			GPIO_low.pop((self.gedane_stappen%4))
			GPIO.output(GPIO_low,0)
			time.sleep(0.1)
			i += 1
			self.gedane_stappen += 1

	def ccw(self,steppen):
		i = 0
		while i < stappen:
			print(i)
			GPIO.output(self.GPIO_output[self.gedane_stappen%4],1)
			GPIO_low = self.GPIO_output.copy()
			GPIO_low.pop((self.gedane_stappen%4))
			GPIO.output(GPIO_low,0)
			time.sleep(0.1)
			i += 1
			self.gedane_stappen -= 1

if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)
	stapper = stappenmotor()
	stappen = int(input('Hoeveel stappen?  '))
	stapper.cw(stappen)
	stapper.ccw(stappen)
	GPIO.cleanup()
	print('einde')
