from conectie import Server
from DC_Motor import dc_motor
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

server = Server()
server.setupConnection()

mode = 0

while run:
	command = server.dataTransfer()
	print(command)
	if mode == 0: #drive manual
		if command == 'a':
			Motor.forward_right(1)
			Motor.stop_left()
			print('left')
		elif command == 's':
			Motor.backward_right(1)
			Motor.backward_left(1)
			print('backward')
		elif command == 'd':
			Motor.stop_right()
			Motor.forward_left(1)
			print('right')
		elif command == 'w':
			Motor.forward_right(1)
			Motor.forward_left(1)
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
			robots.speed = int(command.split()[1])
		print(robots.speed)
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