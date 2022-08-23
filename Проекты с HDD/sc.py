# Дебильный калькулятор V1

from colorama import init
init()
from colorama import Fore, Back, Style

print (Fore.YELLOW )

what = input ('Что делаем? (+, -, *, /): ')

a = float (input ('Введите число a: '))
b = float (input('Введите число b: '))
z = 0

if what == "+" :
	c = a + b
	print(Fore.GREEN + 'Результат: ' + str(c))

elif what == '-' :
	c = a - b
	print(Fore.GREEN + 'Результат: ' + str(c))
elif what == '*' :
	c = a * b
	print(Fore.GREEN + 'Результат: ' + str(c))
elif what == '/' :
	c = a / b
	print(Fore.GREEN + 'Результат: ' + str(c))

else:
	print( Fore.RED + 'Выбрана неверная операция!')	

while z != '':
	z = input ('press Enter')
