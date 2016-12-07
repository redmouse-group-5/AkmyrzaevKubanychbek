#-*- coding: UTF-8 -*-
print ('1. Написать программу поиска самого длинного слова в строке, разделенной пробелами.')
s = "Eto stroka, a eto samoe-bolshoe-slovo-v-stroke"
print('Исходный текст: ' + s)
d = s.split(" ")
t = [x for x in d if len(x)==max(map(len, d))]
print('Результат: ')
print (t)

print ('\n2. Написать программу поиска самого длинного слова в строке, разделенной точкой запятой.')
s = "Eto stroka; a eto samoe bolshoe slovo v stroke razdelenyyi tochka zapyatoi"
print('Исходный текст: ' + s)
d = s.split(";")
t = [x for x in d if len(x)==max(map(len, d))]
print ('Результат: ')
print (t)

print ('\n3. Написать программу самого короткого слова который выделяется знаком который пользователь вводит в интерактивном режиме')
s = "Eto stroka, a eto samoe bolshoe slovo-v-stroke"
print('Исходный текст: ' + s)
str = raw_input("Введите пробел или зяпятой: ")
d = s.split(str)
t = [x for x in d if len(x)==min(map(len, d))]
print ('Результат: ')
print (t)

print ('\n5. Посчитать количество слов в предложении которое вводит пользователь')
s = "Eto stroka, a eto samoe samoe bolshoe slovo v stroke"
str = raw_input("Введите слово которое нужно посчитать его количество в предложении: ")
sum = 0
for word in s.split(" "):
	if word == str:
		sum += 1
print (sum)