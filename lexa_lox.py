print('Калькулятор от Сереги')
print(' ')
# python test.py
one = int(input("Введите первое число: "))
oper = input("Доступные операции '+' '-' '*' '/' : ")
if oper == '+' :
	two = int(input("Введите второе число: "))
	print('Ответ: ' + str(one + two))
elif oper == '-' :
	two = int(input("Введите второе число: "))
	print('Ответ: ' + str(one - two))
elif oper == '*' :
	two = int(input("Введите второе число: "))
	print('Ответ: ' + str(one * two))
elif oper == '/' :
	two = int(input("Введите второе число: "))
	print('Ответ: ' + str(one / two))
else:
	print('Для разблокировки данной операции необходимо прислать 149 руб на номер 89179533537')

print('Спасибо за использование =)')