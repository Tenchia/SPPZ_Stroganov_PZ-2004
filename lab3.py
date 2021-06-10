#42(1)
x = int(input("Введіть значення х: "))
y = int(input("Введіть значення y: "))
if x == y:
    print("Занчення не повинні бути однаковими!")
print("Заміна максимального значенння: ")
print(max(x,y)*min(x,y)*2)
print("Заміна мінімального значенння: ")
print((max(x,y)+min(x,y))*0.5)
#52(2)
a = float(input("Введіть a:="))
b = float(input("Введіть b:="))
c = float(input("Введіть c:="))
d = float(input("Введіть d:="))
e = float(input("Введіть e:="))
f = float(input("Введіть f:="))
g = float(input("Введіть g:="))
h = float(input("Введіть h:="))
ab = (a-e)*(h-f)-(b-f)*(g-e)
cd = (c-e)*(h-f)-(d-f)*(g-e)
if (ab>0) and (cd>0) or (ab<0) and (cd<0):
    print("Належать одній і тієї ж півплощині")
else:
    ("Не належать одній і тієї ж півплощині")
#62(3)
n = int(input("Введите значение n: "))
if n % 2 == 0:
    print("Ваше число является четным")
else:
    print("Ваше число не является четным")
#73
b = int(input("b: "))
v = int(input("v: "))

if b == v:
    b = 0
    v = 0
else:
    if b > v:
        v = b
    elif b < v:
        b = v
print(b, v)

#74
a = int(input("a(0-100): "))

while a <= 0 or a > 100:
    a = int(input("a(0-100): "))

str_a = str(a)

if str_a[-1] == "1":
    print(a, "год")
elif str_a[-1] == "2" or "3" or "4":
    print(a, "года")
elif str_a[-1] == ("5" or "6" or "7" or "8" or "9" or "0"):
    print(a, "лет")