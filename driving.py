country = input('Where are you from?')
age = input('How old are you?')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you can get the driver licence')
	else:
		print('you can not get the licence')	
