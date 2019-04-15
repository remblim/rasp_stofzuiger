from conectie import Server
from DC_Motor import dc_motor

run = True
Connecting = Server()
Motor = dc_motor()

server = Server()
server.setupConnection()

#initialisatie code
GPIO.setmode(GPIO.BOARD) #board setten


while run:
	command = server.dataTransfer()
	if command == 'a':
		Motor.forward_1(1)
		Motor.stop_2()
		print('left')
	elif command == 's':
		Motor.stop_1()
		Motor.stop_2()
		print('backward')
	elif command == 'd':
		Motor.stop_1()
		Motor.forward_2(1)
		print('right')
	elif command == 'w':
		Motor.forward_1(1)
		Motor.forward_2(1)
		print('forward')
	elif command == 'esc':
		Motor.stop_1()
		Motor.stop_2()	
		break
	else:
		Motor.stop_1()
		Motor.stop_2()	