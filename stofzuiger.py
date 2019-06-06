from conectie import Server
from DC_Motor import dc_motor
from accu import battery
import RPi.GPIO as GPIO

class robot():
	def __init__(self):
		self.speed = 1

#initialisatie code
GPIO.setmode(GPIO.BOARD) #board setten
run = True

robots = robot()

Connecting = Server()
Motor = dc_motor()
Battery = battery()

server = Server()
server.setupConnection()

mode = 0

while run:
	command = server.dataTransfer()
	print(command)
	print(mode)
	for items in command:
		if mode == 0: #drive manual
			if items == 'a':
				Motor.forward_right(robots.speed)
				Motor.stop_left()
				print('left')
			elif items == 's':
				Motor.backward_right(robots.speed)
				Motor.backward_left(robots.speed)
				print('backward')
			elif items == 'd':
				Motor.stop_right()
				Motor.forward_left(robots.speed)
				print('right')
			elif items == 'w':
				Motor.forward_right(robots.speed)
				Motor.forward_left(robots.speed)
				print('forward')
			elif items == 'stop':
				Motor.stop_right()
				Motor.stop_left()		
			elif items == 'esc':
				Motor.stop_right()
				Motor.stop_left()
			else:
				Motor.stop_right()
				Motor.stop_left()
		elif mode == 1:
			print('settings')
			if items.split()[0] == 'speed':
				robots.speed = float(items.split()[1])
			elif items.split()[0] == 'accelerate_time':
				Motor.accelerate_time = float(items.split()[1])
				print('accelerate_time',Motor.accelerate_time)
			elif items.split()[0] == 'decelerate_time':
				Motor.decelerate_time = float(items.split()[1])
				print('decelerate_time',Motor.decelerate_time)
		elif mode == 2:
			print('mode 2')
		elif mode == 3:
			print('mode 3')
		elif mode == 4:
			print('mode 4')
		elif mode == 999:
			print('no mode selected')
		else:
			print('mode not availlable')
			
		if items == 'mode 0':
			mode = 0
		elif items == 'mode 1':
			mode = 1
		elif items == 'mode 2':
			mode = 2
			print(mode)
		elif items == 'mode 3':
			mode = 3
			print(mode)
		elif items == 'mode 4':
			mode = 4
			print(mode)
		elif items == 'mode 9':
			mode = 999
			print(mode)
		elif items == 'esc':
			print('ending')
			break
	
	server.send(str(mode))
	Motor.step()
	print('step')