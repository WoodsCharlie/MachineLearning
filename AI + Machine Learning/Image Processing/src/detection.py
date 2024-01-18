import common
import math 

def detect_slope_intercept(image):

	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# use "space=common.init_space(heigh, width)"
	line=common.Line()
	line.m=0
	line.b=0

	#vote_space = 2000 x 2000 array 
	vote_space = []
	for yy in range(0, 2000):
		temp = []
		for xx in range(0, 2000):
			temp.append([1])
		vote_space.append(temp)

	#for all y,x that are black:
	for y in range(0,200):
		for x in range(0,200):
			if image[y][x] != 255:
				#m is between -10 and 10
				for m in range(-1000,1000):
					m = m/100
					#compute b given x,y,m
					# y - mx = b
					b = y - m*x

					#if b is within bounds -1000,1000:
					if b <= 999 and b >= -1000:
						b = int(b) + 1000
						m = int(m * 100) + 1000
						vote_space[m][b][0] = vote_space[m][b][0] + 1

					#m is between -10 and 10
					#for all m in range(-10,10):
						#compute b given x,y,m
						#if b is within bounds -1000,1000:
							#add the vote to voting space
							#ex - vote_space[m][b] += 1

	#return max vote space
	max_count = 1
	for y in range(0,2000):
		for x in range(0,2000):
			if vote_space[y][x][0] > max_count:
				line.m = (y - 1000) / 100
				line.b = x - 1000
			
				max_count = vote_space[y][x][0]
	return line

def detect_circles(image):
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
		#vote_space = 2000 x 2000 array 
	vote_space = []
	for yy in range(0, 200):
		temp = []
		for xx in range(0, 200):
			temp.append([1])
		vote_space.append(temp)
	#vote_space[m][b]?

	#for all y,x that are black:
	for k in range(0,200):
		for h in range(0,200):
			if image[k][h] != 255:

				#for each x within 30 of either side
				for x in range(h-30, h+30):
					if x > 0 and x <200:
						y = math.sqrt(900 - pow((x-h), 2)) + k

						if (y < 200) and (y > 0):
							y = int(y)
							vote_space[y][x][0] = vote_space[y][x][0] + 1


	#return max vote space
	threshhold = 49
	
	circ_count = 0
	for y in range(0,200):
		for x in range(0,200):
			if vote_space[y][x][0] >= threshhold:
				
				circ_count = circ_count + 1

	return circ_count
				