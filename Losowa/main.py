import random

wylosowanaLiczba = random.randint(0,10)

x = input()
if (wylosowanaLiczba < int(x)):
    print("Podałeś za dużą liczbę.")
elif (wylosowanaLiczba > int(x)):
    print("Podałeś za małą liczbę.")
else:
    print("Gratulacje! Zgadłeś!")