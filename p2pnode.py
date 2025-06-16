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
	
	def start():
		self.server = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
		self.server.bind(self.host, self.port)
		self.listen(5)
		
		accept_conn_thread = threading.Thread(self.accept_connection)
		accept_conn_thread.start()
		
		user_interface_thread = threading.Thread(self.user_interface)
		user_interface_thread.start()

	def accept_connection():
		while True:
			try:
				conn, addr = self.server.accept()
				threading.Thread(self.handle_connection(conn, addr)).start()
			except:
				print('Error al aceptar la conexión')
	
	def handle_conenection(self, conn, addr):
		try:
			data = ''
			while not data.endswith('\r\n'):
				data += conn.recv(definiciones.MAX_LARGO_BUFFER)
			self.display_message(data, addr)
		except json.JSONDecodeError:
			print(f"Datos inválidos recibidos de {addr[0]}")
		except Exception as e:
			print(f'Error: {e}')
		finally:
			conn.close()
	
	def display_message(data_json, addr):
		data = json.loads(data_json).decode('utf-8')
		msg = data['content']
		user = data['user']
		now = time.strftime('[%Y.%m.%d %H:%M]')
		print(now + " " + addr[0] + " " + user + " dice: " + msg)
	
	def send_messaje(ip_address, message):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
			s.connect((socket.gethostbyname(ip_address), self.port))
			
			msg_dict = {
				"user" : self.username,
				"content" : message
			}
			
			msg_json = json.dumps(msg_dict)
			msg_json += '\r\n'
			s.send(msg_json.encode('utf-8'))
		except Exception as e:
			print(f'Error: {e}')
	
	def user_interface():
		while True:
			line = input('>>> ')
			
			msg_list = line.split()
			
			if len(msg_list) >= 2:
				ip_address = msg_list[0]
				if(msg_list[1] != '&file'):
					msg = ''
					msg_list = msg_list[1 : len(msg_list)]
					for i in range(len(msg_list)):
						msg += msg_list[i]
					
					msg = msg[0 : definiciones.MAX_LARGO_MENSAJE]
					self.send_message(ip_address, msg)
