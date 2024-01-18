import common

def classify(data, weight):
	result = data[0]*weight[0] + data[1]*weight[1] + weight[2]
	if result >= 0:
		return True
	return False

def part_one_classifier(data_train, data_test):

	weight= [0,0,0]
	data_changed = True
	while data_changed == True:
		data_changed = False

		#for all training data t
		for t in data_train:
			c = classify(t, weight)

			if c != t[2]:
				data_changed = True
				if c == True:
					weight = [weight[0]-t[0], weight[1] -t[1], weight[2] - 0.5]
				else:
					weight = [weight[0]+t[0], weight[1] +t[1], weight[2] + 0.5]

	#classify all data t in test data
	for t in data_test:
		c = classify(t, weight)
		if c == True:
			t[2] = 1
		else: 
			t[2] = 0
	return

def classifyMult(data, weight):
	maxV = -999999999
	
	for i in range(0,10):
		result = data[0]*weight[i][0] + data[1]*weight[i][1]

		if result > maxV:
			maxV = result
			data_class = i

	return data_class

def part_two_classifier(data_train, data_test):
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	weight = common.init_data(10,3)
	
	data_changed = True
	while data_changed == True:
		data_changed = False

		for t in data_train:
			c = classifyMult(t, weight)

			#print("c = " , c, "t[2] = ", int(t[2]))
			if c != int(t[2]):
				data_changed = True
				
				weight[c] = [weight[c][0]-t[0], weight[c][1] -t[1]]
				
				weight[int(t[2])] = [weight[int(t[2])][0]+t[0], weight[int(t[2])][1] +t[1]]

				
	for t in data_test:
		c = classifyMult(t, weight)
		t[2] = c
	return
