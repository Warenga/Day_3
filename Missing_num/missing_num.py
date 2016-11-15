def find_missing(num1, num2):
	set1 = set(num1)
	set2 = set(num2)
	missing = set1 ^ set2
	missing_list = list(missing)
	if missing_list == []:
		return 0
	for num in missing_list:
		return num


