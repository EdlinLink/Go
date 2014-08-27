import socket
from State import State
from Position import Position
from Handle import is_valid
SIZE=1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8001))
#sock.connect(("192.168.1.5", 19281))


# Initial the board and the name (black/white).
msg = sock.recv(SIZE) 
state = State(msg)
Name = state.Name



while True:
	if Name == state.Turn:	
		pos = Position(raw_input(), Name)

		if is_valid(state.Board, pos) == False:
			print "[Position Error, Enter Again]"
			continue

		sock.send(pos.to_str())
		state = State(sock.recv(SIZE))
		print "[25]"
		state.print_board()
		print "[27]"
	
	while Name != state.Turn:
		state = State(sock.recv(SIZE))
		state.print_board()

sock.close()
