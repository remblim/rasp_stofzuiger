import socket

class Server():
	def __init__(self):
		self.port = 5560
		self.host = ''
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('socket is gemaakt')
		try:
			self.s.bind((self.host, self.port))
		except socket.error as msg:
			print(msg)
		print("socket bind complete")

		
				
	def setupConnection(self):
		while True:
			try:
				print('setup connection')
				self.s.listen(1)
				self.conn, address = self.s.accept()
				self.dataTransfer()
			except:
				break
		
		
	def dataTransfer(self):
		print('transfer data')
		while True:
			data = self.conn.recv(1024)
			data = data.decode('utf-8')
			dataMessage = data.split(' ',1)
			command = dataMessage[0]
			if command == 'a':
				print('left')
			elif command == 'd':
				print('right')
			elif command == 'w':
				print('forward')
			elif command == 's':
				print('backward')
			elif command == 'esc':
				break
		self.conn.close()
	

if __name__ == "__main__":
	server = Server()
	server.setupConnection()
	server.dataTransfer()