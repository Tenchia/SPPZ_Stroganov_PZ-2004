#1
print("#1")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
print("Перше число: ", num1)
print("Друге число: ", num2)
print("Сума: ", num1 + num2)
print("Різниця: ", num1 - num2)
print("Добуток: ", num1 * num2)

#2
print("#2")
x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
print("x: ", x)
print("y: ", y)
z = (abs(x)-abs(y))/(1 + abs(x*y))
print("Результат: ", z)

#3
print("#3")
x = float(input("Введіть ребро куба: "))
v = x*x*x
s = x*x*6
print("Об'єм: ", v)
print("Площа бокової поверхні: ", s)

#4
print("#4")
import math

x = float(input("Введіть додатний x: "))
while x <= 0:
    x = float(input("Введіть додатний x: "))
y = float(input("Введіть додатний y: "))
while y <= 0:
    y = float(input("Введіть додатний y: "))
print("x: ", x)
print("y: ", y)
a = (x + y)/2
b = math.sqrt(x*y)
print("Середнє арифметичне: ", a)
print("Середнє геометричне: ", b)

#5
print("#5")
import math

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
print("x: ", x)
print("y: ", y)
a = (x + y)/2
b = math.sqrt(abs(x)*abs(y))
print("Середнє арифметичне: ", a)
print("Середнє геометричне: ", b)

#6
print("#6")
import math

x = float(input("Перший катет: "))
y = float(input("Другий катет: "))
print("Перший катет: ", x)
print("Другий катет: ", y)
a = math.sqrt(math.pow(x,2) + math.pow(y,2))
b = 0.5 * x * y
print("Гіпотенуза: ", a)
print("Площа: ", b)

#7
print("#7")
v1 = float(input("Об'єм першої частини води: "))
t1 = float(input("Температура першої частини води: "))
v2 = float(input("Об'єм другої частини води: "))
t2 = float(input("Температура другої частини води: "))
V = v1+v2
T = (v1*t1+v2*t2)/V
print("Об'єм води", V, "\nТемпература води", T)

#8
print("#8")
import math

n = int(input("Кількість сторін: "))
r = int(input("Радіус вписаного кола: "))

a = r * 2 * math.tan(180/n)

print(a)

#9
print("#9")
import math

n = int(input("Кількість сторін: "))
r = float(input("радіус вписаного кола: "))

P = n * 2 * r * math.tan(math.pi/n)

print(n, r, "\nпериметр: ", P)

#10
print("#10")
import math

h = float(input("Вкажіть висоту: "))

g = 9.81
t = math.sqrt((2*h)/g)

print(h, "\nчас: ", t)
