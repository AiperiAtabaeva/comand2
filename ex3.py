#Напишите программу, которая измеряет длину введенной строки.
# Если строка длиннее десяти символов, то выносится предупреждение.
# Если короче, то к строке добавляется столько символов *,
# чтобы ее длина составляла десять символов, после чего новая строка должна выводиться на экран.


s=input()
if len(s)>10:
    print('длинная строка')
else :
   for i in range (len(s),10):
      s+='*'
   print(s)

# Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
# На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
# Выполните задание без использования встроенных функций min() и max().

   import sys

   min = sys.float_info.max
   max = sys.float_info.min

   for i in range(6):
       a = float(input('введите число '))
       if a > max:
           max = a
       if a < min:
           min = a
   print('\n', 'min is: ', round(min, 2), '\n', 'max is: ', round(max, 2))


#задание 14:
#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).
n = int(input("Введите номер месяца (1-12): "))
def season(num):
   if num == 12 or 1 <= num <= 2:
      print("Зима")
   elif  3 <= num <= 5:
       print("Весна")
   elif 6 <= num <= 8:
       print("Лето")
   elif 9 <= num <= 11:
       print("Осень")
   else:
       print("Неверно введён номер месяца!")

season(n)

Задание 6:
#     Функция
#     Напишите функцию, которая берет текст, и возвращает строковое значение, состоящее из заглавных букв.
#     Используйте текст, данный выше (The Zen of Python).
#     Подсказка: используйте метод строчных значений, который проверяет, “заглавность” буквы.

numbers = int(input("Введите число : "))

maxs = None
min = None

for i in range(5):

    a = int(input("Введите число : "))

    if maxs == None or a > maxs:
        maxs = a
    elif min == None or a < min:
        min = a
print(maxs, min)

text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""

#Задание 2:
        # Напишите программу, которая циклично запрашивает у пользователя номера символов по таблице Unicode и выводит соответствующие им символы.
        # Завершает работу при вводе нуля.
proverka = str.title(text)

print(proverka)


while True:
    symbol = int(input("Введите символ по таблице Unicode: ))
    if symbol == 0:
        break
    print(chr(symbol))