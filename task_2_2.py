#Was passiert wenn ich zwei Noten eingebe
#Note1 = 4.2 Note2 = 3.5 typ1
#Note1 = 5.2 Note2 = 5.8 typ4
#Note1 = 3.8 Note2 = 3.3 typ0
#was passiert wenn ich ein feld frei lasse? fehler und wenn ich eine null schreibe gibt es mir den durschnitt 2.5 darum den typ1

anzahl = 0
note1 = 0.0
note2 = 0.0
note1 = float(input("Note 1:"))
anzahl += 1
note2 = float(input("Note 2:"))
anzahl += 1
schnitt = (note1 + note2) / anzahl
if schnitt >= 4:
    print("*****")
    durchschnitt = int(schnitt * 2)
    durchschnitt = (durchschnitt + 1) // 2
    if durchschnitt == 4:
        print("Typ 2")
    else:
        if durchschnitt == 5:
            print("Typ 3")
        else:
            print("Typ 4")
else:
    print("-----")
    if note1 >= 4 or note2 >= 4:
        print("Typ 1")
    else:
        print("Typ 0")