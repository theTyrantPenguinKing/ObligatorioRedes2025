import sys
import socket
import threading
import time
import json

import definiciones

class P2PNode:
	def __init__(self, port, username):
		self.host = '127.0.0.1'
		self.port = port
		self.username = username
		self.running = False
		self.hosts_connected = []
	
	def start():
		self.server = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
		self.server.bind(self.host, self.port)
		self.listen(5)
		self.running = True
		
		accept_conn_thread = threading.Thread(self.accept_connection)
		accept_conn_thread.start()
		
		user_interface_thread = threading.Thread(self.user_interface)
		user_interface_thread.start()

	def accept_connection():
		while self.running:
			try:
				conn, addr = self.server.accept()
				self.hosts_connected.append(addr[0])
				self.running = True
				threading.Thread(self.handle_connection(conn, addr)).start()
			except:
				if self.running:
					print('Error al aceptar la conexión')
	
	def handle_conenection(self, conn, addr):
		while self.running:
			try:
				data_json = conn.recv(definiciones.MAX_LARGO_BUFFER)
				
				data = json.loads(data_json)
				
				msg = data['content']
				user = data['user']
				now = time.strftime('[%Y.%m.%d %H:%M]')
				print(now + addr[0] + user + " dice: " + msg)				
			except json.JSONDecodeError:
				print(f"Datos inválidos recibidos de {addr}")
			except Exception as e:
				print(f'Error: {e}')
				
				self.hosts_connected.remove(addr[0])
				conn.close()
				break
		
		if len(self.hosts_connected) == 0:
			self.running = False
		else:
			self.running = True
	
	def user_interface():
		while True:
			line = input('>>> ')
			
