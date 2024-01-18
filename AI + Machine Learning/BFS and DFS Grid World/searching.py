import common

#check to make sure position is in bounds
def checkRange(y, x):
	if(y<0) or (y>common.constants.MAP_HEIGHT-1):
		return False
	if(x<0) or (x>common.constants.MAP_WIDTH-1):
		return False
	return True

def df_search(map):
	found = False

	# access the map using "map[y][x]"

	frontier = []
	parent = []

	#Find starting tile: 
	for y in range(0, common.constants.MAP_HEIGHT):
		temp = []
		for x in range(0, common.constants.MAP_WIDTH):
			temp.append([])
			if (map[y][x] == 2):
				frontier.append([y,x])
				startx = x
				starty = y	
		parent.append(temp)

	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	#start DF search

	while frontier:
		
		#take out node
		
		curr_node = frontier.pop()
		curr_x = curr_node.pop()
		curr_y = curr_node.pop()

		#check if goal
			#if yes, found = true, return/break loop
		
		if ((map[curr_y][curr_x]) == 3):
			found = True
			break

		#mark node as visited (set value to 4)
		map[curr_y][curr_x] = 4

		#for each child
			#check if valid
			#put in frontier
			#mark og node as parent  to child ???
		
		#check child with LOWEST PRIO
		if checkRange(curr_y-1,curr_x) and (((map[curr_y-1][curr_x]) == 0) or ((map[curr_y-1][curr_x]) == 3)):
			frontier.append([curr_y-1,curr_x])
			
			#MARK IN PARENT ARR
			parent[curr_y-1][curr_x] = [curr_y,curr_x]
		
		#second lowest prio
		if checkRange(curr_y,curr_x-1) and (((map[curr_y][curr_x-1]) == 0) or ((map[curr_y][curr_x-1]) == 3)):
			frontier.append([curr_y,curr_x-1])
			
			#MARK IN PARENT ARR
			parent[curr_y][curr_x-1] = [curr_y,curr_x]

		#second highest prio
		if checkRange(curr_y+1,curr_x) and (((map[curr_y+1][curr_x]) == 0) or ((map[curr_y+1][curr_x]) == 3)):
			frontier.append([curr_y+1,curr_x])
			
			#MARK IN PARENT ARR
			parent[curr_y+1][curr_x] = [curr_y,curr_x]

		#highest prio
		if checkRange(curr_y,curr_x+1) and (((map[curr_y][curr_x+1]) == 0) or ((map[curr_y][curr_x+1]) == 3)):
			frontier.append([curr_y,curr_x+1])
			
			#MARK IN PARENT ARR
			parent[curr_y][curr_x+1] = [curr_y,curr_x]
		
	if found == True:
		#back through parent array marking nodes as 5 (the path)
		
		#set goal to found
		map[curr_y][curr_x] = 5

		while (curr_y != starty) or (curr_x != startx):
			temp_parent = parent[curr_y][curr_x]
			curr_x = temp_parent.pop()
			curr_y = temp_parent.pop()
			map[curr_y][curr_x] = 5

		#set starting node to 5
		#map[starty][startx] = 5

	return found

def bf_search(map):
	found = False

	# access the map using "map[y][x]"
	frontier = []
	parent = []

	#Find starting tile: 
	for y in range(0, common.constants.MAP_HEIGHT):
		temp = []
		for x in range(0, common.constants.MAP_WIDTH):
			temp.append([])
			if (map[y][x] == 2):
				frontier.append([y,x])
				startx = x
				starty = y	
		parent.append(temp)

	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	#start DF search

	while frontier:
		
		#take out node
		
		curr_node = frontier.pop(0)
		curr_x = curr_node.pop()
		curr_y = curr_node.pop()

		#check if goal
			#if yes, found = true, return/break loop
		
		if ((map[curr_y][curr_x]) == 3):
			found = True
			break

		#mark node as visited (set value to 4)
		map[curr_y][curr_x] = 4

		#for each child
			#check if valid
			#put in frontier
			#mark og node as parent  to child ???

		#new lowest prio
		if checkRange(curr_y,curr_x+1) and (((map[curr_y][curr_x+1]) == 0) or ((map[curr_y][curr_x+1]) == 3)):
			frontier.append([curr_y,curr_x+1])
			
			#MARK IN PARENT ARR
			parent[curr_y][curr_x+1] = [curr_y,curr_x]

		#second highest prio
		if checkRange(curr_y+1,curr_x) and (((map[curr_y+1][curr_x]) == 0) or ((map[curr_y+1][curr_x]) == 3)):
			frontier.append([curr_y+1,curr_x])
			
			#MARK IN PARENT ARR
			parent[curr_y+1][curr_x] = [curr_y,curr_x]
		
		#new highest prio
		if checkRange(curr_y,curr_x-1) and (((map[curr_y][curr_x-1]) == 0) or ((map[curr_y][curr_x-1]) == 3)):
			frontier.append([curr_y,curr_x-1])
			
			#MARK IN PARENT ARR
			parent[curr_y][curr_x-1] = [curr_y,curr_x]

		#check child with NEW HIGHEST PRIO
		if checkRange(curr_y-1,curr_x) and (((map[curr_y-1][curr_x]) == 0) or ((map[curr_y-1][curr_x]) == 3)):
			frontier.append([curr_y-1,curr_x])
			
			#MARK IN PARENT ARR
			parent[curr_y-1][curr_x] = [curr_y,curr_x]
		
	if found == True:
		#back through parent array marking nodes as 5 (the path)
		
		#set goal to found
		map[curr_y][curr_x] = 5

		while (curr_y != starty) or (curr_x != startx):
			temp_parent = parent[curr_y][curr_x]
			curr_x = temp_parent.pop()
			curr_y = temp_parent.pop()
			map[curr_y][curr_x] = 5

		#set starting node to 5
		#map[starty][startx] = 5

	return found
