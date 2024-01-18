import common

class variables:
	counter=0

def recursive_back(sudoku):
	variables.counter = variables.counter + 1
	#if complete, return True
	complete = True
	for i in range(0, 9):
		for j in range(0,9):
			if(sudoku[i][j] == 0):
				complete = False

	if complete == True:
		return True
	#next = find next var to try
	
	for county in range(0,9):
		for countx in range(0,9):
			if (sudoku[county][countx] == 0):
				for z in range(1,10):
					if common.can_yx_be_z(sudoku, county, countx, z):
						sudoku[county][countx] = z
						
						if (recursive_back(sudoku) == True):
							
							return True
						sudoku[county][countx] = 0
				return False


	return False

def sudoku_backtracking(sudoku):
	variables.counter = 0
	recursive_back(sudoku)
	return variables.counter


def update_doms(sudoku):
	domain = []
	for y in range(0,9):
		temp = []
		for x in range(0,9):
			values = [0]
			if (sudoku[y][x] == 0):
				for z in range(1,10):
					if (common.can_yx_be_z(sudoku, y, x, z) == True):
						values.append(z)
			temp.append(values)
		domain.append(temp)
	return domain

def check_doms(sudoku, domain):
	for y in range(0,9):
		for x in range(0,9):
			if (sudoku[y][x] == 0):
				if domain[y][x] == [0]:
					return False
	return True

def recursive_forward(sudoku, domain):
	variables.counter = variables.counter + 1
	#if complete, return True
	complete = True
	for i in range(0, 9):
		for j in range(0,9):
			if(sudoku[i][j] == 0):
				complete = False

	if complete == True:
		
		return True
	#next = find next var to try

	for county in range(0,9):
		for countx in range(0,9):
			if (sudoku[county][countx] == 0):
				for z in range(1,10):
					if common.can_yx_be_z(sudoku, county, countx, z):
						sudoku[county][countx] = z
						
						#CHECK THIS ADDITION AGAINST DOMAINS
						# update domains
						doms = update_doms(sudoku)
						# remove z in same column domains , remove z in the same row domains, "" from 3 by 3 square
						
						# check the domains (if any are empty, go to next z)
						if check_doms(sudoku, doms) == True:			
							if (recursive_forward(sudoku, doms) == True):
								
								return True

						sudoku[county][countx] = 0
						doms = update_doms(sudoku)
						
						#revert domain after changing it

				return False
	return False

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	domain = update_doms(sudoku)
	recursive_forward(sudoku, domain)

	return variables.counter
