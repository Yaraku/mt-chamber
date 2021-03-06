class Command:

	InputSize = 2
	OutputSize = 1
	MultiThreadable = True
	ShareResources = True

	def __init__(self, threads, encode=None):
		self.encode = encode

	def routine(self, thread_id, instream):
		conn = instream[0]
		data = instream[1]
		if self.encode:
			data = data.encode(self.encode)
		conn.sendall(data)
		return (conn,)
