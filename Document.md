
## 1. Server.py 

**Introduction**: The server of the game. Give the initial state of the players and handle their movements.

**Constant**:

+ SIZE	:	Message length.
+ PORT	:	Port number of the server.

**Global Variable**:

+ state	:	The state of the current game saved in the server.

**Function**:

+ Init(str)		:	Return the initial msg to initial the State of both the players.
+ Connection()	:	Prompt the user enter the ip address and set up the server, waitting for two players and initial them.
+ handling()	:	Game start and handle the process of the two players.

## 2. Client.py

**Class**: Client

**Introduction**: The logic part of the player which contributes to the UI.py.

**Variable**:

+ SIZE	:	Message length.
+ PORT	:	Server ip address port number. Must be the same as the Server.py.
+ sock	:	The socket to connect to server.
+ ip	:	Server ip address. Entered by the user.                                                                            
+ state	:	The state of the player.
+ update_flag	:	Decide whether to update the UI.

**Function**:

+ \_\_init\_\_(self)	:	Connect to the server and initial the players' state through the returning msg from server.
+ get_board(self)	:	Get the board state of the game.
+ send_station(self, x, y)	:	Send the position of movement to the server.
	+ x	:	x of position (x,y) of the movement.	
	+ y	:	y of position (x,y) of the movement.

## 3. State.py

**Class**: State

**Variable**:

+ Name	:	The current player who send this "state" to the server. It can either be (Black/White).
+ Board	:	The board of the game. The board is a 21*21 matrix.
+ Turn	:	The next one who can move one step.

**Function**:

+ \_\_init\_\_(self, state_msg)	:	Initial the state including "Name", "Board" and "Turn".
	+ state\_mag	:	A string state message that can initial the state class.
+ print_board(self)	:	Print the board for checking whether there is a bug.
+ to_str(self)		: Make the state to be a string in order to send to server.
