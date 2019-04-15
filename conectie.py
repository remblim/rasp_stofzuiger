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

		while True:
			try:
				print('try')
				self.conn = self.setupConnection()
				print('hi')
				self.dataTransfer()
				print('hey')
			except:
				break
				
	def setupConnection(self):
		self.s.listen(1)
		self.conn, address = self.s.accept()
		print('hello')
		return conn
		
	def Get(self):
		reply = stored_Value
		return reply
		
	def REPEAT(self,dataMessage):
		reply = dataMessage[1]
		return reply

	def dataTransfer(self):
		print('transfer data')
		while True:
			data = self.conn.recv(1024)
			data = data.decode('utf-8')
			dataMessage = data.split(' ',1)
			command = dataMessage[0]
			if command == 'GET':
				reply = Get()
			elif command == 'REPEAT':
				reply = REPEAT(dataMessage)
			elif command == 'EXIT':
				print('afsluiten')
				break
			elif command == 'KILL':
				print('shutdown')
				self.s.close()
				break
			else:
				reply = 'unknown command'
				
			self.conn.sendall(str.encode(reply))
			print('data has been sent')
		self.conn.close()
	

if __name__ == "__main__":
	server = Server()