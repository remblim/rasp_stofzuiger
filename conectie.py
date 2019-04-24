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
			print('server error')
		print("socket bind complete")
				
	def setupConnection(self):
		self.s.listen(1)
		self.conn, address = self.s.accept()
		
	def dataTransfer(self):
		command = self.conn.recv(1024)
		command = command.decode('utf-8')
		return command
	
	def send(self,data):
		self.s.send(str.encode(data,'utf-8'))
		
if __name__ == "__main__":
	server = Server()
	server.setupConnection()
	server.dataTransfer()