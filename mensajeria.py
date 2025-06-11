import sys
import socket
import hashlib
import signal

import definiciones

def handle_interruption(signum, frame):
	print('\r\nInterrupción detectada...')
	print('Cerrando sesión')

def get_authentication_message(auth_socket):
	msg_in = ''
	while not msg_in.endswith('\r\n'):
		msg_in += auth_socket.recv(definiciones.MAX_LARGO_BUFFER).decode('utf-8')
	msg_in = msg_in.strip()
	return msg_in

# verifica autenticacion del usuario
def authentication(ip_auth, port_auth):
	auth_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	auth_socket.connect((ip_auth, port_auth))
	
	msg_in = get_authentication_message(auth_socket)
	
	if msg_in != 'Redes 2025 - Laboratorio - Autenticacion de Usuarios':
		print('Protocolo Incorrecto')
		sys.exit()
	print(msg_in)
	
	user = input('Usuario: ')
	password = input('Clave: ')
	md5_password = hashlib.md5(password.encode('utf-8')).hexdigest()
	
	auth_socket.send((user + '-' + md5_password + '\r\n').encode('utf-8'))
	
	msg_in = get_authentication_message(auth_socket)
	
	if msg_in == 'NO':
		print(msg_in)
		sys.exit()
	
	msg_in = get_authentication_message(auth_socket)
	print(msg_in)
	
	auth_socket.close()
	
	return msg_in

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print('Uso: python mensajeria.py <port> <ipAuth> <portAuth>')
		sys.exit()
	
	signal.signal(signal.SIGINT, handle_interruption)
	
	port = int(sys.argv[1])
	ip_auth = sys.argv[2]
	port_auth = int(sys.argv[3])
	
	username = authentication(ip_auth, port_auth)
	
