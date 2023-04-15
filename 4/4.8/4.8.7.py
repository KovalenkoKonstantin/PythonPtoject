# Напиши программу,
# которая считает координаты шахматного короля
# и координаты произвольной клетки на шахматной доске,
# и выведет "YES" (без кавычек) если король может походить на эту клетку,
# и "NO" (без кавычек) в противном случае.
# Король ходит на соседнюю по вертикали, горизонтали или диагонали клетку.
# На первых двух строчках вводятся координаты короля,
# на третьей и четвертой строчке вводятся координаты клетки доски.
# Все координаты - целые числа от 1 до 8 включительно
# нумерация начинается из левого верхнего угла
# вначале вводится вертикальная составляющая координаты,
# потом горизонтальная
import random

a = random.randint(1, 8)
b = random.randint(1, 8)
c = random.randint(1, 8)
d = random.randint(1, 8)
print(a)
print(b)
print(c)
print(d)
a = 3
b = 3
c = 4
d = 4
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) < 2 and abs(b - d) < 2:
    print("YES")
else:
    print("NO")

a, b, c, d = (int(input()) for x in '1234')
print("YES" if abs(a - c) < 2
               and abs(b - d) < 2 else "NO")
