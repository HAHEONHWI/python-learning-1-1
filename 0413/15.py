for dan in range(2, 10):
	for num in range(1, 10):
		result = dan * num
		if result % 2 == 0:
			print(dan, "*", num, "=", result)
