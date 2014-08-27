class State:


	def __init__(self, state_msg):
		self.Name = ""
		self.Board = ""
		self.Turn = ""
		self.Name, self.Board, self.Turn = state_msg.split(";")
		tmp, self.Name = self.Name.split(":")
		tmp, self.Board = self.Board.split(":")
		self.Board = self.Board.split(",")
		tmp, self.Turn = self.Turn.split(":")

	def setName(self, name):
		self.Name = name

	def setBoard(self, board):
		self.Board = board

	def setTurn(self, turn):
		self.Turn = turn

	def print_board(self):
		#board = self.Board.split(",")
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

		
	def to_str(self):
		msg = "Name:" + self.Name + ";Board:" + ",".join(self.Board) + ";Turn:" + self.Turn
		return msg
