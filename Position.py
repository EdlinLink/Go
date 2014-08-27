class Position:

	def __init__(self, pos_msg, id):
		self.pos_msg = pos_msg
		if id=="Black":
			self.id = "1"
		elif id=="White":
			self.id = "3"

	def getMsg(self):
		return self.pos_msg

	def setID(self, id):
		self.id = id
		
	def to_str(self):
		msg = self.id + ";" + self.pos_msg
		return msg

	
