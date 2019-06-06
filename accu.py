import time
import Adafruit_ADS1x15

class battery():
	def __init__(self):
		self.adc = Adafruit_ADS1x15.ADS1115()
		self.gain = 2/3
	
	def step(self):
		values = [0]*4
		for i in range(4):
			values[i] = (self.adc.read_adc(i, gain=self.gain)/32767)*6.144
		return values