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
	main_count = 0
	while True:
		last_deleted = 0
		for x in List: 
			if List.count(x) > 1:
				List.remove(x)
				last_deleted = last_deleted + 1
				main_count = main_count + 1
		if last_deleted == 0:
			break
	print('Строчек удалено:', main_count)
	return List

def delStrsWthSpclSmbl(List, smbl):
	main_count = 0
	while True:
		last_edited = 0
		for i in range(len(List)): 
			previous_item = List[i]
			List[i] = List[i].replace(smbl, ' ')
			if previous_item != List[i]:
				last_edited = last_edited + 1
				main_count = main_count + 1
		if last_edited == 0:
			break
	print("Особых символов удалено:", main_count)
	return List

def delStrsWthSpclWrdStartwith(List, wrd):
	original = len(List)
	List = [value for value in List if not value.startswith(wrd)]
	print('Особых строчек удалено:', original - len(List))
	return List

def sortList(List):
	List.sort()
	return List

def writeInFile(List, file_name='Alldialogs'):
	print("Строчек записываем:", len(List))
	g = open("{}.csv".format(file_name), 'w')
	for i in range(len(List)):
		g.write(List[i])
	g.close()


if __name__ == "__main__":
	List = getListfromFile('one_of_two_rost24_10')
	List = delRptdMsgs(List)
	writeInFile(List, 'one_of_two_rost24_10')
	pass