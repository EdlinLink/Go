import socket
from Position import Position
from State import State
from Handle import handle

def Init(name):
	msg = ""
	msg += "Name:" + name
	msg += ";Board:"
	board = "5,"*21 + ("5," + "0,"*19 + "5,")*19 + "5,"*20 + "5"
	msg += board
	msg += ";Turn:Black"
	return msg
	





SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(('192.168.1.2', 8001)) 
sock.bind(('localhost', 8001)) 
sock.listen(5)

connection1, address1 = sock.accept()
state_msg = Init("Black")
connection1.send(state_msg)

state = State(state_msg)

connection2, address2 = sock.accept()
state_msg = Init("White")
connection2.send(state_msg)


while True:

	if state.Turn == "Black":
		connect = connection1
	else:
		connect = connection2

	pos_msg_id = connect.recv(SIZE)
	id, pos_msg = pos_msg_id.split(";")

	pos = Position(pos_msg, state.Turn)
	
	state = handle(state.Board, pos)

	connection1.send(state.to_str())
	connection2.send(state.to_str())
