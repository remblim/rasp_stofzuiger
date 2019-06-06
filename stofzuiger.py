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
	for items in command:
		if mode == 0: #drive manual
			if command == 'a':
				Motor.forward_right(robots.speed)
				Motor.stop_left()
				print('left')
			elif command == 's':
				Motor.backward_right(robots.speed)
				Motor.backward_left(robots.speed)
				print('backward')
			elif command == 'd':
				Motor.stop_right()
				Motor.forward_left(robots.speed)
				print('right')
			elif command == 'w':
				Motor.forward_right(robots.speed)
				Motor.forward_left(robots.speed)
				print('forward')
			elif command == 'stop':
				Motor.stop_right()
				Motor.stop_left()		
			elif command == 'esc':
				Motor.stop_right()
				Motor.stop_left()
			else:
				Motor.stop_right()
				Motor.stop_left()
		elif mode == 1:
			if command.split()[0] == 'speed':
				robots.speed = float(command.split()[1])
			elif command.split()[0] == 'accelerate_time':
				Motor.accelerate_time = float(command.split()[1])
				print('accelerate_time',Motor.accelerate_time)
			elif command.split()[0] == 'decelerate_time':
				Motor.decelerate_time = float(command.split()[1])
				print('decelerate_time',Motor.decelerate_time)
			print('settings')
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
			print(mode)
			
		if command == 'mode 0':
			mode = 0
		elif command == 'mode 1':
			mode = 1
		elif command == 'mode 2':
			mode = 2
			print(mode)
		elif command == 'mode 3':
			mode = 3
			print(mode)
		elif command == 'mode 4':
			mode = 4
			print(mode)
		elif command == 'mode 9':
			mode = 999
			print(mode)
		elif command == 'esc':
			print('ending')
			break
	
	server.send(str(mode))
	Motor.step()