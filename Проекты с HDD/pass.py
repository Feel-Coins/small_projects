q = '0'
z = 0
i = '0'
while not i == '25042021':
	i = input('Введите пароль: ')
	if not i == '25042021':
		z = z+1
	while z >= 3:
		q = input ('Нужна подсказка?')
		if q == 'да':
			print ('Дата вашей встречи')
			z = 0
		if q == 'нет':
			print ('ok')
			z = 0
else:
	print('Вход выполнен успешно!')



print (' ')
