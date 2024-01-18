import common

#returns zero if board is full, else, 1
def check_board(board):
	for z in range(0, len(board)):
		if board[z] == 0:
			return 1
	return 0

def minimizer(temp, orig):
	if orig == 2:
		orig = -1
	if temp == 2:
		temp = -1
	return temp < orig

def maximizer(temp, orig):
	if orig == 2:
		orig = -1
	if temp == 2:
		temp = -1
	return temp > orig
		

def mmprune(board, turn):
	
	#check game over
	board_val = common.game_status(board)
	if board_val != 0:
		return board_val
	if check_board(board) == 0:
		#board is full (tie)
		return 0

	#make board copy
	temp_board = []
	for x in range(0,len(board)):
		temp_board.append(board[x])

	#max part
	if turn == 1:
		v = -5
		for i in range(0, len(temp_board)):
			if temp_board[i] == 0:
				temp_board[i] = turn
				temp_val = mmprune(temp_board, 2)

				#if temp_val > v:
				if maximizer(temp_val, v):
					v = temp_val
				temp_board[i] = 0
		return v
	#else (min part)
	if turn == 2:		
		v = 5
		for z in range(0, len(temp_board)):
			if temp_board[z] == 0:
				temp_board[z] = turn
				temp_val = mmprune(temp_board, 1)

				#if temp_val < v: #chooses x over draw 
				if minimizer(temp_val, v):
					v = temp_val
				temp_board[z] = 0
		return v


def minmax_tictactoe(board, turn):
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

	return mmprune(board, turn)
	#return max_value(board, turn)

	#return common.constants.NONE

def prune(board, turn, alp, bet):
	
	#check game over
	board_val = common.game_status(board)
	
	if board_val != 0:
		return board_val
	
	if check_board(board) == 0:
		#board is full (tie)
		return 0

	#make board copy
	temp_board = []
	for x in range(0,len(board)):
		temp_board.append(board[x])

	
	#max part
	if turn == 1:
		v = -5
		for i in range(0, len(temp_board)):
			if temp_board[i] == 0:
				temp_board[i] = turn
				temp_val = prune(temp_board, 2, alp, bet)

				#if temp_val > v:
				if maximizer(temp_val, v):
					v = temp_val
				#if v >= bet:
				if v == bet or maximizer(v, bet):
					return v
				#if v > alp:
				if maximizer(v, alp):
					alp = v
				temp_board[i] = 0
		return v
	#else (min part)
	if turn == 2:		
		v = 5
		for z in range(0, len(temp_board)):
			if temp_board[z] == 0:
				temp_board[z] = turn
				temp_val = prune(temp_board, 1, alp, bet)

				#if temp_val < v:
				if minimizer(temp_val, v):
					v = temp_val
				#if v <= alp:
				if v == alp or minimizer(v, alp):
					return v
				#if v < bet:
				if minimizer(v, bet):
					bet = v
				temp_board[z] = 0
		return v
		
def abprun_tictactoe(board, turn):
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return prune(board, turn, -5, 5)

