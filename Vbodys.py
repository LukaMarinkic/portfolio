#Volumen von Köpern

searched = str(input("Was ist gesucht? (Würfel/Quader/Dreiecksprisma/Parralelogrammprisma) :"))

if searched == "Würfel" :
    print("Würfelberechnung ist ausgewählt - Alles bitte in cm angeben")
    aW = int(input("Seite a= "))
    VW = aW*aW*aW
    print("V ist gleich ", VW,"cm³")
elif searched == "Quader" :
    print("Quaderberechnung ist ausgewählt - Alles bitte in cm angeben")
    aQ = int(input("Seite a= "))
    bQ = int(input("Seite b= "))
    cQ = int(input("Seite c= "))
    VQ = aQ*bQ*cQ
    print("V ist gleich ", VQ)
elif searched == "Dreiecksprisma" :
    print("Dreiecksprismaberechnung ist ausgewählt - Alles bitte in cm angeben")
    aD = int(input("Seite a= "))
    haD = int(input("Höhe von seite a ha= "))
    GD = 1/2*aD*haD
    hD = int(input("Höhe vom Prisma h= "))
    VD = GD*hD
    print("V= ", VD)

elif searched == "Parralelogrammprisma" :
    print("Fünfecksprismaberechnung ist ausgewählt - Alles bitte in cm angeben")
    aP = int(input("Seite a= "))
    haP = int(input("Höhe von seite a ha= "))
    GP = 1/2*aP*haP
    hP = int(input("Höhe vom Prisma h= "))
    VP = GP*hP    
    print("V= ", VP)
else :
    print("Ungültige Eingabe - Gültige Eingaben sind: 'Würfel', 'Quader', 'Dreiecksprisma' 'Parralelogrammprisma'")

input("Drück enter: ")