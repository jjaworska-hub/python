print ("Hello World")

print("Ala ma 3 koty \nAla kupila 2 koty \nAla ma 5 kotow \n1 kot utonal podczas proby zlapania ryby w wannie \nAla ma 4 koty \n2 koty uciekly przed mysza \nAla ma 2 koty \n1-na kotka jest w ciazy \nAla ma 50 kotow .")

a = input()
iloczynLiczb = int(a) * int(a)
print("Kwadrat liczby to:" + str(iloczynLiczb))

b = input()
c = input()
iloczynLiczbprost = int(b) * int(c)
sumaLiczbprost = int(b) + int(c) + int(b) + int(c)
print("Pole:" + str(iloczynLiczbprost))
print("Obwód:" + str(sumaLiczbprost))

print("Zadanie 5")
sumaLiczbzao = float(5.32) + float(2.77)
print("Wynik dodawania:" + str(round(sumaLiczbzao)))

print("Zadanie 6")
a = 0.4
b = 2
b = b - 0.5
a = a * b
print("Wynik b:" + str(b))
print("Wynik a:" + str(a))

print("Zadanie 7")
d = 5.1
e = -(d+1)
if (d > e):
     print(str(d))
else:
    print(str(e))

print("Zadanie 8")
a = input()
b = input()
x = input()
y = int(x)*int(a)+int(b)
if (y == 0):
    print(str(x) + str(y))
elif(x == 0):
    print(str(x) + str(y))
else:
    print("Nie ma miejsc zerowych.")