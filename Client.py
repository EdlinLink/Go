import thread
import threading
import time
import socket
from State import State
from Position import Position
from Handle import is_valid


class Client:

	def __init__(self):

		self.SIZE=1024
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "[Enter Server IP]:"
		self.ip = raw_input()
		self.sock.connect((ip, 11270))
		#sock.connect(("192.168.1.5", 19281))


		# Initial the board and the name (black/white).
		msg = self.sock.recv(self.SIZE) 
		self.state = State(msg)
		self.Name = self.state.Name
		self.update_flag = True

		thread.start_new_thread(self.recv_station, ())

	def get_board(self):
		return self.state.Board

	def send_station(self, x, y):
		if self.Name == self.state.Turn:	

			input = str(x)+","+str(y)
			pos = Position(input, self.Name)

			if is_valid(self.state.Board, pos) == False:
				print "[Position Error, Enter Again]"
			else:
				print "[Client 40]"
				print pos
				self.sock.send(pos.to_str())


	def recv_station(self):
		while True:
			self.state = State(self.sock.recv(self.SIZE))
			self.state.print_board()
			self.update_flag = True



if __name__ == "__main__":
	c = Client()
	while True:
		c.get_state()


