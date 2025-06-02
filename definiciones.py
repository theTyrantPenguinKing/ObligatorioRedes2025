MAX_LARGO_MENSAJE = 0xff
MAX_LARGO_BUFFER = 1 << 10

def is_valid_ipv4(text : str):
	ip_values = text.split('.')
	ip_values_size = len(ip_values)
	result = False
	
	if ip_values_size == 4:
		result = True
		
		try:
			for i in range(ip_values_size):
				val = int(ip_values[i])
				if(val < 0 or val > 255):
					result = False
		except ValueError:
			result = False
	
	return result
