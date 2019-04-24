from conectie import Server
from DC_Motor import dc_motor
import RPi.GPIO as GPIO

#initialisatie code
GPIO.setmode(GPIO.BOARD) #board setten
run = True

Connecting = Server()
Motor = dc_motor()

server = Server()
server.setupConnection()

mode = 0

while run:
	command = server.dataTransfer()
	if mode == 0: #drive manual
		if command == 'a':
			Motor.forward_1(1)
			Motor.stop_2()
			print('left')
		elif command == 's':
			Motor.backward_1(1)
			Motor.backward_2(1)
			print('backward')
		elif command == 'd':
			Motor.stop_1()
			Motor.forward_2(1)
			print('right')
		elif command == 'w':
			Motor.forward_1(1)
			Motor.forward_2(1)
			print('forward')
		elif command == 'stop':
			Motor.stop_1()
			Motor.stop_2()		
		elif command == 'esc':
			Motor.stop_1()
			Motor.stop_2()
			break
		else:
			Motor.stop_1()
			Motor.stop_2()
	elif mode == 1:
		print('automatic navigation')
	else:
		print('mode not availlable')
		print(mode)
		
	if command == 'mode 0':
		mode = 0
		print(mode)
	elif command == 'mode 1':
		mode = 1
		print(mode)
	elif command == 'mode 2':
		mode = 2
		print(mode)
	elif command == 'mode 3':
		mode = 3
		print(mode)
	elif command == 'mode 4':
		mode = 4
		print(mode)
	

	server.send(str(mode))