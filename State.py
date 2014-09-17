#########################################################################
#	Title	:	State.py												#	
#	Author	:	Edlin													#
#	Date	:	Sept. 1, 2014											#
#########################################################################


##	State: It is a class that represents the state of the players that pass to the server. 
##

class State:

	##	__init__(): Initial the state including "Name", "Board" and "Turn".
	##
	##	"Name"	:	The current player who send this "state" to the server. It can either be (Black/White). 
	##	"Board"	:	The board of the game. The board is a 21*21 matrix.
	##	"Turn"  :   The next one who can move one step.
	##
	##	"state_msg"	:	A string state message that can initial the state class.

	def __init__(self, state_msg):
		self.Name = ""
		self.Board = ""
		self.Turn = ""
		self.Name, self.Board, self.Turn = state_msg.split(";")
		tmp, self.Name = self.Name.split(":")
		tmp, self.Board = self.Board.split(":")
		self.Board = self.Board.split(",")
		tmp, self.Turn = self.Turn.split(":")


	##	print_board(): Print the board for checking whether there is a bug.

	def print_board(self):
		i = 1
		while i<=19:
			j = 1
			while j<=19:
				char = self.Board[21*i + j]
				if char == "0":
					print "_",
				elif char == "1":
					print "B",
				elif char == "3":
					print "W",
				else: 
					print "E",
				j+=1
			i+=1
			print ""


	##	to_str(): Make the state to be a string in order to send to server.

	def to_str(self):
		msg = "Name:" + self.Name + ";Board:" + ",".join(self.Board) + ";Turn:" + self.Turn
		return msg
