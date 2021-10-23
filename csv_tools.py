#  _____   ___            
# /       /      \      / 
# |       \___    \    /  
# |           \    \  /   
# \_____   ___/     \/    tools 2021 REV.01
#                         ----------

# Внимание! Старый CSV файл будет заменён новым! 
# Рекомендую сделать резервную копию CSV файла!
# JErfurt 2021

def getListfromFile(file_name='Alldialogs'):
	f = open("{}.csv".format(file_name), 'r')
	List = f.readlines()
	f.close()
	return List

def delRptdMsgs(List):
	original = len(List)
	last_deleted = 1
	while last_deleted != 0:
		last_deleted = 0
		for x in List: 
			if List.count(x) > 1:
				List.remove(x)
				last_deleted = last_deleted + 1
		print('Строчек удалено:', last_deleted)
	return List

def delStrsWthSpclSmbl(List, smbl):
	last_deleted = 0
	for i in range(len(List)): 
		List[i] = List[i].replace('  ', ' ')
		last_deleted = last_deleted + 1
	print("Особых символов удалено:", last_deleted)
	return List

def delStrsWthSpclWrdStartwith(List, wrd):
	original = len(List)
	List = [value for value in List if not value.startswith(wrd)]
	print('Особых строчек удалено:', original - len(List))
	return List

def sortList(List):
	List.sort()
	return List

def writeInFile(List):
	print("Строчек записываем:", len(List))
	g = open("{}.csv".format(file_name), 'w')
	for i in range(len(List)):
		g.write(List[i])
	g.close()


if __name__ == "__main__":
	pass