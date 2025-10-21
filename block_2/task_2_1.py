#Was passiert wenn ich diese zwei zahlen eingebe:
#zahl1 = 6 zahl2 = 3
#zahl1 = 7 zahl2 = 7

zahl1 = int(input("Zahl 1: "))
zahl2 = int(input("Zahl 2: "))
if zahl2 < zahl1 and zahl1 > 5:
    temp = zahl1
    zahl1 = zahl2
    zahl2 = temp
else:
    if zahl1 == zahl2:
        zahl1 = 5
    zahl2 = 8
print("Ausgabe 1 =", zahl1)
print("Ausgabe 2 =", zahl2)