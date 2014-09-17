#########################################################################	
#	Title	:	Server.py												#
#	Author	:	Edlin (LIN Junhao)										#
#	Date	:	Sept. 17, 2014											#
#########################################################################

import socket
from Position import Position
from State import State
from Handle import handle

##	SIZE: Message length
SIZE = 1024	

##	PORT: The server port number.
PORT = 11270


##	Init(): Return the initial msg to initial the State of both the players.
##	The format of the msg is a no new line string:
##
##		Name:name;
##		Board:s,s,...,s;
##		Turn:name
##
##	"Name"	:	Initial the role of the player.
##	"Board"	:	The states of the board.
##	"Turn"	:	The next one who move one step.
##
##	"name"	:	"Black" or "White". 
##	"s"		:	"1", "2", "3", "4" or "5". Each number stands for different state of the grid:
##
##		1: Black on the grid;
##		2: Black on the grid temporarily (for calculate the state);
##		3: White on the grid;
##		4: White on the grid temporarily (for calculate the state);
##		5: Border of the board.
##	


def Init(name):
	msg = ""
	msg += "Name:" + name
	msg += ";Board:"
	board = "5,"*21 + ("5," + "0,"*19 + "5,")*19 + "5,"*20 + "5"
	msg += board
	msg += ";Turn:Black"
	return msg
	

##	Connection(): Prompt the user enter the ip address and set up the server, waitting for two players and initial them. 
##
##	The server can only serve "2" players.
##
##	state	:	The state of the current game saved in the server.	
##
##	The first one to connect server will be "Black" and the second one will be "White".
##


def Connection():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "[Enter Server IP]: "
	ip = raw_input()
	sock.bind((ip, PORT)) 
	sock.listen(2)

	connection1, address1 = sock.accept()
	connection2, address2 = sock.accept()

	state_msg = Init("Black")
	connection1.send(state_msg)

	global state
	state = State(state_msg)

	state_msg = Init("White")
	connection2.send(state_msg)


##	Handling(): Game start and handle the process of the two players.
##
##	According to the "state.Turn" to judge whose turn, 
##	handle the movement and update the state and tell players the new state.
## 

def Handling():
	while True:

		if state.Turn == "Black":
			connect = connection1
		else:
			connect = connection2

		pos_msg_id = connect.recv(SIZE)
		print "[Server]", pos_msg_id, "//"
		id, pos_msg = pos_msg_id.split(";")

		pos = Position(pos_msg, state.Turn)
		
		state = handle(state.Board, pos)

		connection1.send(state.to_str())
		connection2.send(state.to_str())


if __name__ == '__main__':
	Connection()
	Handling()
