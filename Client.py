#########################################################################	
#	Title	:	Client.py												#
#	Author	:	Edlin (LIN Junhao)										#
#	Date	:	Sept. 17, 2014											#
#########################################################################

import thread
import threading
import time
import socket
from State import State
from Position import Position
from Handle import is_valid


##	Client:	The logical part of the players.
##
##	If you want to start the player, you should run the "UI.py" instead of "Client.py"
##

class Client:

	##	__init__(): Connect to the server and initial the players' state through the returning msg from server.
	##	
	##	1. Prompt the player to enter the server ip address;
	##	2. Receive the initial msg from the server and initial the client state;
	##	3. Launch a new thread to receive message from server for updating state.
	##	
	##	SIZE	:	Message length.
	##	PORT	:	Server ip address port number. Must be the same as the Server.py.
	##	sock	:	The socket to connect to server.
	##	ip		:	Server ip address. Entered by the user.
	##	state	:	The state of the player.
	##	update_flag	:	Decide whether to update the UI.

	def __init__(self):
		self.SIZE = 1024
		self.PORT = 11270
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "[Enter Server IP]:"
		self.ip = raw_input()
		self.sock.connect((self.ip, self.PORT))


		msg = self.sock.recv(self.SIZE) 
		self.state = State(msg)
		self.Name = self.state.Name
		self.update_flag = True


		thread.start_new_thread(self.recv_station, ())


	##	get_board(): Get the board state of the game.

	def get_board(self):
		return self.state.Board


	##	send_station(): Send the position of movement to the server.

	def send_station(self, x, y):
		if self.Name == self.state.Turn:	

			input = str(x)+","+str(y)
			pos = Position(input, self.Name)

			if is_valid(self.state.Board, pos) == False:
				print "[Position Invalid, Enter Again]"
			else:
				self.sock.send(pos.to_str())


	##	recv_station(): Receive the update msg from the server.

	def recv_station(self):
		while True:
			self.state = State(self.sock.recv(self.SIZE))
			self.state.print_board()
			self.update_flag = True


if __name__ == "__main__":
	c = Client()
	while True:
		c.get_state()
