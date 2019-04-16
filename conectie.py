import socket

class Server():
	def __init__(self):
		self.port = 50562
		self.host = ''
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		print('socket is gemaakt')
		try:
			self.s.bind((self.host, self.port))
		except socket.error as msg:
			print(msg)
			print('error')
		print("socket bind complete")
				
	def setupConnection(self):
		try:
			print('starting setup connection')
			self.s.listen(1)
			print('finished listening')
			self.conn, address = self.s.accept()
			print('connection setup')
		except:
			break
		
	def dataTransfer(self):
		print('transfer data')

		command = self.conn.recv(1024)
		print('data recieved')
		command = command.decode('utf-8')
		print(command)
		return command
		
if __name__ == "__main__":
	server = Server()
	server.setupConnection()
	server.dataTransfer()