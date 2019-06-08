import time
import Adafruit_ADS1x15

class battery():
	def __init__(self):
		self.adc = Adafruit_ADS1x15.ADS1115()
		self.gain = 2/3
		self.battery = [0]*4
	
	def step(self):
		for i in range(4):
			self.battery[i] = (self.adc.read_adc(i, gain=self.gain)/32767)*6.144
	
	def status(self):
		self.status_battery = ((self.battery[3]-6.0)/(8.4/6))*100
		return self.status_battery