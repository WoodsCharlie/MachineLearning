import common

def checkRange(y, x):
	if(y<0) or (y>common.constants.MAP_HEIGHT-1):
		return False
	if(x<0) or (x>common.constants.MAP_WIDTH-1):
		return False
	return True

def findDistance(y1,x1,y2,x2):
	result = 0
	#compare y distance
	if(y1 < y2):
		result = y2 - y1
	if(y2 < y1):
		result = y1 - y2
	#compare x distance
	if(x1 < x2):
		return result + (x2-x1)
	
	return result + (x1 - x2)	

def astar_search(map):
	found = False
	
	frontier = []
	parent = []

	#init parent array
	for y in range(0, common.constants.MAP_HEIGHT):
		temp = []
		for x in range(0, common.constants.MAP_WIDTH):
			temp.append([])
		parent.append(temp)

	#find the start and end
	startY = 0
	startX = 0
	goalY = 0
	goalX = 0

	for y in range(0, common.constants.MAP_HEIGHT):
		for x in range(0, common.constants.MAP_WIDTH):
			if map[y][x] == 2:
				startY = y
				startX = x
				frontier.append([y,x, 0])
			if map[y][x] == 3:
				goalY = y
				goalX = x

	while frontier:
		
		#get x and y
		curr_node = frontier.pop(0) #taking from front of list
		curr_dis = curr_node.pop()
		curr_x = curr_node.pop()
		curr_y = curr_node.pop()

		if ((map[curr_y][curr_x]) == 3):
			found = True
			break
		
		#set to visited 
		map[curr_y][curr_x] = 4

		#calculate f(n) [steps from start + distance to end]

		distanceFromStart = 0

		#calculate distance from start 
		temp_y = curr_y
		temp_x = curr_x

		while (temp_y != startY) or (temp_x != startX):
				temp_parent = parent[temp_y][temp_x]
				temp_x = temp_parent[1]
				temp_y = temp_parent[0]
				distanceFromStart = distanceFromStart + 1
		
		#for each of the 4 directions 

		#check move left 
		if(checkRange(curr_y, curr_x-1)):
			#check not wall or invalid 
			if (((map[curr_y][curr_x-1]) == 0) or ((map[curr_y][curr_x-1]) == 3)):
				#check distance to end
				leftWeight = findDistance(curr_y, curr_x-1, goalY, goalX)
				leftWeight = leftWeight + distanceFromStart + 1
				
				#add to frontier in right spot

				#check to see if frontier is empty
				if (frontier == []):
					
					#add to frontier
					frontier.append([curr_y,curr_x-1, leftWeight])
					#MARK IN PARENT ARR
					parent[curr_y][curr_x-1] = [curr_y,curr_x]
				
				#if frontier not empty, put in right spot
				inserted = False
				for spot in range(0, len(frontier)): 
					if (leftWeight < frontier[spot][2]):
						frontier.insert(spot, [curr_y,curr_x-1, leftWeight])
						parent[curr_y][curr_x-1] = [curr_y,curr_x]
						inserted = True
						break
					
					#if they have same weight, check x
					elif (leftWeight == frontier[spot][2]):
						if ((curr_x-1) < frontier[spot][1]):
							frontier.insert(spot, [curr_y,curr_x-1, leftWeight])
							parent[curr_y][curr_x-1] = [curr_y,curr_x]
							inserted = True
							break

						#if they have same x, check y
						if ((curr_x-1) == frontier[spot][1]):
							if((curr_y) < frontier[spot][0]):
								frontier.insert(spot, [curr_y,curr_x-1, leftWeight])
								parent[curr_y][curr_x-1] = [curr_y,curr_x]
								inserted = True
								break

						elif(spot == len(frontier)-1):
							frontier.insert(spot+1, [curr_y,curr_x-1, leftWeight])
							parent[curr_y][curr_x-1] = [curr_y,curr_x]
							inserted = True
							break
				if (inserted == False):
					frontier.insert(len(frontier), [curr_y,curr_x-1, leftWeight])
					parent[curr_y][curr_x-1] = [curr_y,curr_x]

		#check move up
		if(checkRange(curr_y-1, curr_x)):
			#check not wall or invalid 
			if (((map[curr_y-1][curr_x]) == 0) or ((map[curr_y-1][curr_x]) == 3)):
				#check distance to end
				upWeight = findDistance(curr_y-1, curr_x, goalY, goalX)
				upWeight = upWeight + distanceFromStart + 1
			
				#add to frontier in right spot

				#check to see if frontier is empty
				if (frontier == []):
					#add to frontier
					frontier.append([curr_y-1,curr_x, upWeight])
					#MARK IN PARENT ARR
					parent[curr_y-1][curr_x] = [curr_y,curr_x]
				
				#if frontier not empty, put in right spot
				inserted = False
				for spot in range(0, len(frontier)): 
					if (upWeight < frontier[spot][2]):
						frontier.insert(spot, [curr_y-1,curr_x, upWeight])
						parent[curr_y-1][curr_x] = [curr_y,curr_x]
						inserted = True
						break

					#if they have same weight, check x
					elif (upWeight == frontier[spot][2]):
						if ((curr_x) < frontier[spot][1]):
							frontier.insert(spot, [curr_y-1,curr_x, upWeight])
							parent[curr_y-1][curr_x] = [curr_y,curr_x]
							inserted = True
							break

						#if they have same x, check y
						if ((curr_x) == frontier[spot][1]):
							if((curr_y-1) < frontier[spot][0]):
								frontier.insert(spot, [curr_y-1,curr_x, upWeight])
								parent[curr_y-1][curr_x] = [curr_y,curr_x]
								inserted = True
								break

						elif(spot == len(frontier)-1):
							frontier.insert(spot+1, [curr_y-1,curr_x, upWeight])
							parent[curr_y-1][curr_x] = [curr_y,curr_x]
							inserted = True
							break
				if (inserted == False):
					frontier.insert(len(frontier), [curr_y-1,curr_x, upWeight])
					parent[curr_y-1][curr_x] = [curr_y,curr_x]


		#check move down
		if(checkRange(curr_y+1, curr_x)):
			#check not wall or invalid 
			if (((map[curr_y+1][curr_x]) == 0) or ((map[curr_y+1][curr_x]) == 3)):
				#check distance to end
				downWeight = findDistance(curr_y+1, curr_x, goalY, goalX)
				downWeight = downWeight + distanceFromStart + 1

				#add to frontier in right spot

				#check to see if frontier is empty
				if (frontier == []):
					#add to frontier
					frontier.append([curr_y+1,curr_x, downWeight])
					#MARK IN PARENT ARR
					parent[curr_y+1][curr_x] = [curr_y,curr_x]

				#if frontier not empty, put in right spot
				inserted = False 
				for spot in range(0, len(frontier)): 
					if (downWeight < frontier[spot][2]):
						frontier.insert(spot, [curr_y+1,curr_x, downWeight])
						parent[curr_y+1][curr_x] = [curr_y,curr_x]
						inserted = True
						break
					#if they have same weight, check x
					elif (downWeight == frontier[spot][2]):
						if ((curr_x) < frontier[spot][1]):
							frontier.insert(spot, [curr_y+1,curr_x, downWeight])
							parent[curr_y+1][curr_x] = [curr_y,curr_x]
							inserted = True
							break

						#if they have same x, check y
						if ((curr_x) == frontier[spot][1]):
							if((curr_y+1) < frontier[spot][0]):
								frontier.insert(spot, [curr_y+1,curr_x, downWeight])
								parent[curr_y+1][curr_x] = [curr_y,curr_x]
								inserted = True
								break
						elif(spot == len(frontier)-1):
							frontier.insert(spot+1, [curr_y+1,curr_x, downWeight])
							parent[curr_y+1][curr_x] = [curr_y,curr_x]
							inserted = True
							break
				if inserted == False:
					frontier.insert(len(frontier), [curr_y+1,curr_x, downWeight])
					parent[curr_y+1][curr_x] = [curr_y,curr_x]





		#check move right
		if(checkRange(curr_y, curr_x+1)):
			#check not wall or invalid 
			if (((map[curr_y][curr_x+1]) == 0) or ((map[curr_y][curr_x+1]) == 3)):
				#check distance to end
				rightWeight = findDistance(curr_y, curr_x+1, goalY, goalX)
				rightWeight = rightWeight + distanceFromStart + 1

				#check to see if frontier is empty
				
				if (frontier == []):
					#add to frontier
					frontier.append([curr_y,curr_x+1, rightWeight])
					#MARK IN PARENT ARR
					parent[curr_y][curr_x+1] = [curr_y,curr_x]
				
				#if frontier not empty, put in right spot
				inserted = False
				for spot in range(0, len(frontier)): 
					if (rightWeight < frontier[spot][2]):
						frontier.insert(spot, [curr_y,curr_x+1, rightWeight])
						parent[curr_y][curr_x+1] = [curr_y,curr_x]
						inserted = True
						break

					#if they have same weight, check x
					elif (rightWeight == frontier[spot][2]):
						if ((curr_x+1) < frontier[spot][1]):
							frontier.insert(spot, [curr_y,curr_x+1, rightWeight])
							parent[curr_y][curr_x+1] = [curr_y,curr_x]
							inserted = True
							break

						#if they have same x, check y
						if ((curr_x+1) == frontier[spot][1]):
							if((curr_y) < frontier[spot][0]):
								frontier.insert(spot, [curr_y,curr_x+1, rightWeight])
								parent[curr_y][curr_x+1] = [curr_y,curr_x]
								inserted = True
								break

						elif(spot == len(frontier)-1):
							frontier.insert(spot+1, [curr_y,curr_x+1, rightWeight])
							parent[curr_y][curr_x+1] = [curr_y,curr_x]
							inserted = True
							break
				if inserted == False:
					frontier.insert(len(frontier), [curr_y,curr_x+1, rightWeight])
					parent[curr_y][curr_x+1] = [curr_y,curr_x]

	

	# if solved: 

	if found == True:
		#back through parent array marking nodes as 5 (the path)
		#set goal to found
		map[curr_y][curr_x] = 5

		while (curr_y != startY) or (curr_x != startX):
			temp_parent = parent[curr_y][curr_x]
			curr_x = temp_parent.pop()
			curr_y = temp_parent.pop()
			map[curr_y][curr_x] = 5

	return found
