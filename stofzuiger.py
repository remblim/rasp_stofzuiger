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
	command_give = []
	command_got = server.dataTransfer()
	command_give.append('battery '+str(Battery.status()))
	for items in command_got:
		if mode == 0: #drive manual
			if items == 'a':
				Motor.forward_right(robots.speed)
				Motor.stop_left()
				print('left')
			elif items == 's':
				Motor.backward_right(robots.speed)
				Motor.backward_left(robots.speed)
				print('backwards')
			elif items == 'd':
				Motor.stop_right()
				Motor.forward_left(robots.speed)
				print('right')
			elif items == 'w':
				Motor.forward_right(robots.speed)
				Motor.forward_left(robots.speed)
				print(Motor.l_target_speed,Motor.r_target_speed)
				print('forwards')
			elif items == 'stop':
				Motor.stop_right()
				Motor.stop_left()	
				print('stop')
			elif items == 'esc':
				Motor.stop_right()
				Motor.stop_left()
				print('escape')
			print(Motor.l_target_speed,Motor.r_target_speed)
		elif mode == 1:
			print('settings')
			if items.split(' ')[0] == 'max_speed':
				Motor.max_speed = float(items.split()[1])
				print('robots speed',Motor.max_speed)
			elif items.split(' ')[0] == 'min_speed':
				Motor.min_speed = float(items.split()[1])
				print('robots speed',Motor.min_speed)
			elif items.split(' ')[0] == 'accelerate_time':
				Motor.accelerate_time = float(items.split()[1])
				print('accelerate_time',Motor.accelerate_time)
			elif items.split(' ')[0] == 'decelerate_time':
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
	command_give.append('mode '+str(mode))
	server.send(command_give)
	Motor.step()
	Battery.step()
