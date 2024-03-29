import common
import solver

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(sudoku, show):
	result=True
	for y in range(9):
		v=""
		for x in range(9):
			value = sudoku[y][x];
			sudoku[y][x]=0
			if (value!=0 and common.can_yx_be_z(sudoku,y,x,value)):
				v+=bcolors.GREEN
			else:
				result = False
				v+=bcolors.RED
			v+=str(value)
			sudoku[y][x]=value
		if (show):
			print(v)
	return result

	
def run_experiment(data, btlimit, fclimit):
	result=True
    
	sudoku = common.init_sudoku();
	common.set_sudoku(sudoku, data);
	bt1 = solver.sudoku_backtracking(sudoku);
	if ( not check_result(sudoku,False)):
		print("Backtracking results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True);
		result=False;
	else:
		print("Backtracking results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL)

	if (bt1!=btlimit):
		print("Backtracking count: "+str(bt1) +"("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False
	else:
		print("Backtracking count: "+str(bt1) +"("+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL+")")

	common.set_sudoku(sudoku, data)
	fc1 = solver.sudoku_forwardchecking(sudoku)
	if (not check_result(sudoku,False)):
		print("Forwardchecking results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True)
		result=False
	else:
		print("Forwardchecking results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL)

	if (fc1!=fclimit):
		print("Forwardchecking count: "+str(fc1) +"("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False;
	else:
		print("Forwardchecking count: "+str(fc1) +"("+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL+")")


	return result



data1 = ("900670000"
"006800470"
"800010003"
"003000001"
"005406900"
"600000300"
"300060008"
"068005200"
"000082006")

data2 = ("006100050"
"200605008"
"000090002"
"000019300"
"002000800"
"003570000"
"900040000"
"800301009"
"040006100")

data3 = ("530070000"
"600195000"
"098000060"
"800060003"
"400803001"
"700020006"
"060000280"
"000419005"
"000080079")

data4 = ("009000400"
"600400020"
"840031090"
"008007041"
"500060003"
"160800700"
"070290065"
"020005004"
"005000900")

data5 = ("295831467"
"846275913"
"371694852"
"014082396"
"630410528"
"082060174"
"160000200"
"458926731"
"020100600")


data6 = ("921786453"
"786453921"
"543912867"
"839671245"
"162549738"
"475328196"
"214835679"
"398267514"
"657194382")


print ("Board 1")
exp1 = run_experiment(data1, 3448, 1078)
print ("Board 2")
exp2 = run_experiment(data2, 21819, 2815)
print ("Board 3")
exp3 = run_experiment(data3, 4209, 334)
print ("Board 4")
exp4 = run_experiment(data4, 655, 235)
print ("Board 5")
exp5 = run_experiment(data5, 22, 20)
print ("Board 6")
exp5 = run_experiment(data6, 1, 1)

all_passed = exp1 and exp2 and exp3 and exp4 and exp5 


if all_passed:
	exit(0)
else:
	exit(1)
