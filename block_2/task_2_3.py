anzahl = 1
wert1 = 0
wert2 = 0
wert3 = 0
max_wert = 0

wert1 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1

wert2 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1

wert3 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1

if wert1 > wert2 and wert1 > wert3:                     #Kompilierfehler: zeile 16, grund: operator kann nicht vergleichen mit logischen operatoren, Lösung: wert vergleichen mit wert
      max_wert = wert1
elif wert3 > wert2:                                     #Kompilirfehler: zeile 18, grund: else anstatt elif und nicht alle werte verglichen, Lösung: elif und alle vergleichen
    max_wert = wert3
elif wert2 > wert3:
    max_wert = wert2

print("Der grösste Wert ist:", max_wert)