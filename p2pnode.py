import sys
import socket
import threading
import datetime

import definiciones

class P2PNode:
	def __init__(self, port, username):
		self.host = '127.0.0.1'
		self.port = port
		self.username = username
		# diccionario host-username
		self.known_peers = {}
		self.running = False
	
	def start():
		self.server = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
		self.server.bind(self.host, self.port)
		self.listen(5)
		
		self.running = True
		
		accept_conn_thread = threading.Thread(self.accept_connection)
		

	def accept_connection():
		while self.running:
			try:
				conn, addr = self.server.accept()
				threading.Thread(self.handle_connection(conn, addr)).start()
			except:
				if self.running:
					print('Error al aceptar la conexión')
	
	def handle_conenection():
		pass
	
	def receive_messages(self, conn, addr):
		mensaje = ''
		try:
			data = conn.recv(MAX_LARGO_BUFFER).decode('utf-8').strip()
			
			# obtiene el string desde la posición cero hasta la posición MAX_LARGO_MENSAJE - 1 inclusive
			data = data[0 : 0 + MAX_LARGO_MENSAJE]
			
			fecha = datetime.now().strftime('[%Y.%M.%D %H:%M]')
			mensaje = fecha + ' ' + addr[0] + 
