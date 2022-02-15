d = " Daria"
x = "18 лет"
l = (d + " ") * 5
print("я", d, "мне", x)
print(l)

print("как вас зовут? Сколько вам лет")
a = input()
b = int(input())
print("привеет", a, ".")
if b >= 1 and b <= 18:
   print("ты выглядишь моложе")
if b > 18 and b <= 25:
   print("ты в самом расцвете сил")
y = a[::-1]
print(y)

print(a[1:-1])
print(a[-3:])
print(a[0:5])
d = len(a)
print(d)
sum = 0
pr = 1
c=b
while c != 0:
   z = c % 10
   sum = sum + c
   pr = pr * z
   c = c // 10
print(sum, " ", pr)

print(a.lower())
print(a.upper())

print(a.replace(' ', ''))
if b < 0 or b > 150:
   print("Ошибка, проверьте корректность введенных данных, вы слишком старый или не существуете")
print("Сколько будет 6*6+6?")
q=int(input())
if q==42 :
   print("yes")
else:
   print("no")
