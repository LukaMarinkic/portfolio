from calc import *# Calculations for the things

print("Dieses Programm kann den Oberflächeninhalt und das Volumen von Würfeln, Quadern, Quadratpyramiden, Kugeln, Dreiecks- und Paralelogrammprismen berechnen. Das Ergebnis ist in der gleichen Einheit wie die Eingabe")
Körper = str(input("Welchen Körper möchtest du berechnen (Großschreiben und in ): "))
if Körper == "Würfel":
    a_dice = float(input("Kantenlänge (a):"))
    print("Volumen", Vdice(a_dice), "Oberflächeninhalt", Odice(a_dice))
elif Körper == "Quader":
     a_cube = float(input("1.Kante (a):"))
     b_cube = float(input("2.Kante (b):"))
     c_cube = float(input("3.Kante (c):"))
     print("Volumen", Vcube(a_cube, b_cube, c_cube), "Oberflächeninhalt", Ocube(a_cube, b_cube, c_cube))
elif Körper == "Dreiecksprisma":
    a_3prism = float(input("Eine Seite des Dreiecks: "))
    ha_3prism = float(input("Höhe dieser Seite: "))
    hb_3prism = float(input("Höhe des Prismas: "))
    u =float(input("Umfang des Dreiecks: "))
    print("Volumen", Vtriangleprism(hb_3prism, ha_3prism, a_3prism), "Oberflächeninhalt", Otriangleprism(a_3prism, hb_3prism, ha_3prism, u))
elif Körper == "Paralelogrammprisma":
    a_Pprism = float(input("Eine Seite des Paralelogramms: "))
    ha_Pprism = float(input("Höhe dieser Seite: "))
    hb_Pprism = float(input("Körperhöhe: "))
    u_Pprism = float(input("Grundseitenumfang: "))
    Vparalelogrammprism(hb_Pprism, ha_Pprism, a_Pprism)
    Oparalelogrammprism(ha_Pprism, hb_Pprism, ha_Pprism, u_Pprism)
elif Körper == "Quadratpyramide":
    a_Py = float(input("Kantenlänge des Quadrats: "))
    hb_Py = float(input("Pyramidenhöhe: "))
    hs_py = float(input("Seitenhöhe der Seiten: "))
    VPyramid(a_Py, hb_Py)
    OPyramid(a_Py, hs_py)
elif Körper == "Kugel":
    r_ball = float(input("radius: "))
    VBall(r_ball)
    OBall(r_ball)
else:
    print("Ungültige Eingabe! Gültige Eingaben sind: 'Würfel';'Quader';'Dreiecksprisma';'Paralelogrammprisma';'Quadratpyramide' und 'Kugel'.")