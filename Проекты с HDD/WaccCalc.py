print ('Привет, давай посчитаем WACC!')

E = float(input('Введи процент собственного капитала: '))
D = float(input('Отлично! Теперь введи процент заемного капитала: '))
V = float(E) + float(D)
Re = float(input('Нужна ставка по вкладу, чтобы сравнить доходность: '))
Rd = float(input('А еще ставка по кредиту: '))
Tc = float(input('Финальный штрих. Введите ставку налога на прибыль (обычно 0.2): '))

a = float(E) / float(V)
print(a)

b = float(D) / float(V)
print(b)

WACC = float(float(a) * float(Re) + float(b) * float(Rd)) * float(1-Tc)

print('WACC получился: ' + str(WACC))

