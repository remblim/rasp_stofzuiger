import time
import Adafruit_ADS1x15

class battery():
	def __init__(self):
		self.adc = Adafruit_ADS1x15.ADS1115()
		self.gain = 2/3
		self.battery = 0
	
	def step(self):
		self.battery = (self.adc.read_adc(3, gain=self.gain)/32767)*6.144
		print('battery',self.battery)
	
	def status(self):
		self.status_battery = ((self.battery-6.0)/(8.4/6))*100
		return self.status_battery