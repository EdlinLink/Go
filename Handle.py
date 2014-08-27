from Position import Position
from State import State

def is_valid(board, pos):
	pos_msg = pos.getMsg()
	x, y = pos_msg.split(",")
	x = int(x)
	y = int(y)

	if board[x*21 + y]=="0":
		return True
	else:
		return False

def is_neighbor(board, x, y, tag):
	if board[x*21 + y+1]==tag or board[x*21 + y-1]==tag or board[(x+1)*21 + y]==tag or board[(x-1)*21 + y]==tag :
		return True
	else:
		return False



def is_dead(board, x, y, tag):

	test_board = list(board)

	cluster = {}
	cluster[(x,y)] = True


	keys = cluster.keys()
	while len(keys)!=0:
		for i in keys:
			if is_neighbor(test_board, i[0], i[1], "0"):
				return False

			if test_board[i[0]*21 + i[1]+1]==tag:
				cluster[(i[0], i[1]+1)] = True
			if test_board[i[0]*21 + i[1]-1]==tag:
				cluster[(i[0], i[1]-1)] = True
			if test_board[(i[0]+1)*21 + i[1]]==tag:
				cluster[(i[0]+1, i[1])] = True
			if test_board[(i[0]-1)*21 + i[1]]==tag:
				cluster[(i[0]-1, i[1])] = True

			test_board[i[0]*21 +i[1]] = "-1"
			cluster.pop(i)
		keys = cluster.keys()

	return True

	
	

def neighbor_change(board, x, y, tag1, tag2):
	cluster = {}
	cluster[(x,y)] = True
	board[x*21 + y] = tag2

	keys = cluster.keys()
	while len(keys)!=0:
		for i in keys:
			if board[i[0]*21 + i[1]+1]==tag1:
				board[i[0]*21 + i[1]+1] = tag2
				cluster[(i[0], i[1]+1)] = True
			if board[i[0]*21 + i[1]-1]==tag1:
				board[i[0]*21 + i[1]-1] = tag2
				cluster[(i[0], i[1]-1)] = True
			if board[(i[0]+1)*21 + i[1]]==tag1:
				board[(i[0]+1)*21 + i[1]] = tag2
				cluster[(i[0]+1, i[1])] = True
			if board[(i[0]-1)*21 + i[1]]==tag1:
				board[(i[0]-1)*21 + i[1]] = tag2
				cluster[(i[0]-1, i[1])] = True

			cluster.pop(i)
		keys = cluster.keys()



def neighbor_isdead_handle(board, x, y, tag):
	if board[x*21 + (y+1)]==tag and is_dead(board, x, y+1, tag):
		neighbor_change(board, x, y+1, tag, "0")
	if board[x*21 + (y-1)]==tag and is_dead(board, x, y-1, tag):
		neighbor_change(board, x, y-1, tag, "0")
	if board[(x+1)*21 + y]==tag and is_dead(board, x+1, y, tag):
		neighbor_change(board, x+1, y, tag, "0")
	if board[(x-1)*21 + y]==tag and is_dead(board, x-1, y, tag):
		neighbor_change(board, x-1, y, tag, "0")



def handle(board, pos):
	state_msg = ""
	state_msg += "Name:" 
	if pos.id == "1":
		state_msg += "Black;"
	elif pos.id == "3":
		state_msg += "White;"

	state_msg +="Board:"
	#----------------------

	x, y = pos.pos_msg.split(",")
	x = int(x)
	y = int(y)


	# determine whether (x,y) neighbors are null.
	# if there is at least one neighbor is null, everything goes well 
	# or, we should determine whether (x,y) is_dead

	PositionError = False

	'''
	print "[TAG 1]"
	if is_neighbor(board, x, y, "0"):
		print "[TAG 2.1]"
		board[x*21 + y] = pos.id 
	else:
		print "[TAG 2.2]"
	'''


	board[x*21 + y] = pos.id



	## Black
	if pos.id == "1":	

		#============================
		
		neighbor_isdead_handle(board, x, y, "3")

		#============================
		
		print "TAG 2.2.1"
		if is_dead(board, x, y, pos.id):
			print "TAG 2.2.1.1"
			board[x*21 + y] = "4"	# White_tmp
			if is_dead(board, x, y, "4"):
				print "TAG 2.2.1.1.1"
				neighbor_change(board, x, y,"3", "0")	# White -> Null
				board[x*21 + y] = "1"			# White_tmp -> Black
			else:
				print "TAG 2.2.1.1.2"
				print "[Position Error]"
				board[x*21 + y] = "0"
				PositionError = True
		else:
			print "TAG 2.2.1.2"
			print "###", board[x*21 + (y-1)], is_dead(board, x, y-1, "3"), "###"

			neighbor_isdead_handle(board, x, y, "3")


				


	## White
	else:

		
		neighbor_isdead_handle(board, x, y, "1")


		print "TAG 2.2.2"
		if is_dead(board, x, y, pos.id):
			board[x*21 + y] = "2"	# Black_tmp
			if is_dead(board, x, y, "2"):
				neighbor_change(board, x, y,"1", "0")	# Black -> Null
				board[x*21 + y] = "3"			# Black_tmp -> White
			else:
				print "[Position Error]"
				board[x*21 + y] = "0"
				PositionError = True
		else:

			neighbor_isdead_handle(board, x, y, "1")



	

	#-----------------------
	board = ",".join(board)
	state_msg +=board

	state_msg += ";Turn:"

	if PositionError == False:
		if pos.id == "1":
			state_msg += "White"
		elif pos.id == "3":
			state_msg += "Black"
	else:
		if pos.id == "1":
			state_msg += "Black"
		elif pos.id == "3":
			state_msg += "White"
		

	return State(state_msg)



