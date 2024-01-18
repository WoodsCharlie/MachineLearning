QUEENS = 10


#check to make sure position is in bounds
def checkRange(y,x):
	if(y<0) or (y>9):
		return False
	if(x<0) or (x>9):
		return False
	return True

def findNumAttacks(board): 
	#check current state (number of attacks)
	numAttacks = 0

	for x in range(0,QUEENS-1):	#for each queen but the last
		queenSpot = 0
		#find the queen in the collumn 
		for y in range(0, 10):
			if board[y][x] == 1:
				queenSpot = y
		
		#check how many attacks that queen has (only looking right)
		 
		for remaining in range(x+1, QUEENS):
			#check the horizontal
			if board[queenSpot][remaining] == 1:
				numAttacks = numAttacks + 1

		#check the diagonals
		currx = x
		curry = queenSpot 

		#check decending diagonal 
		while checkRange(curry+1, currx+1):
			if board[curry+1][currx+1] == 1:
				numAttacks = numAttacks+1
			curry = curry + 1
			currx = currx + 1
		
		#check ascending diagonal 
		currx = x
		curry = queenSpot
		
		while checkRange(curry-1, currx+1):
			if board[curry-1][currx+1] == 1:
				numAttacks = numAttacks+1
			curry = curry - 1
			currx = currx + 1
	
	return numAttacks


def gradient_search(board):

	solved = False 

	prev_attacks = 90
	#get current number of attacks 
	curr_attacks = findNumAttacks(board)

	while curr_attacks < prev_attacks: #until min is found
		#make new boards and compare to current attacks
		prev_attacks = curr_attacks
		temp_result = 65 

		#make temp board 
		temp_board = [[0 for x in range(0,10)] for x in range(0,10)]
		for y in range(0,10):
			for x in range(0,10):
				temp_board[y][x] = board[y][x]

		for x in range(0, QUEENS):
			
			queenY = 15

			#remove queen from the x column
			for y in range(0, QUEENS):
				if temp_board[y][x] == 1:
					queenY = y
					temp_board[y][x] = 0

			#no queens in specific x 
			for y in range(0,QUEENS):
				temp_board[y][x] = 1
				temp_result = findNumAttacks(temp_board)
				if temp_result < curr_attacks:
					curr_attacks = temp_result

					for z in range(0,10):
						for xx in range(0,10):
							board[z][xx] = temp_board[z][xx]
					
				temp_board[y][x] = 0
			#put queeen back 
			temp_board[queenY][x] = 1
		

	if curr_attacks == 0:
			solved = True

	return solved