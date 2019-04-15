import socket

class Server():
	def __init__(self):
		self.port = 5560
		while True:
			try:
				conn = setupConnection()
				dataTransfer(conn)
			except:
				break
			
	def setupServer():
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('socket is gemaakt')
		try:
			s.bind((host, port))
		except socket.error as msg:
			print(msg)
		print("socket bind complete")
		return s
		
	def setupConnection():
		s.listen(1)
		conn, address = s.accept()
		print('hello')
		return conn
		
	def Get():
		reply = stored_Value
		return reply
		
	def REPEAT(dataMessage):
		reply = dataMessage[1]
		return reply

	def dataTransfer(conn):
		while True:
			data = conn.recv(1024)
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
				s.close()
				break
			else:
				reply = 'unknown command'
				
			conn.sendall(str.encode(reply))
			print('data has been sent')
		conn.close()
	s = setupServer()

if __name__ == "__main__":
	server = Server()