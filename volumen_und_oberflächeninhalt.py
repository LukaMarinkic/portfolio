import Körper as K# Calculations for the things

print("Dieses Programm kann den Oberflächeninhalt und das Volumen von Würfeln, Quadern, Quadratpyramiden, Kugeln, Dreiecks- und Paralelogrammprismen berechnen. Das Ergebnis ist in der gleichen Einheit wie die Eingabe")
Fläche = str(input("Welchen Körper möchtest du berechnen (Großschreiben und in ): "))
if Fläche == "Würfel":
    a_dice = float(input("Kantenlänge (a):"))
    print("Volumen", K.Vdice(a_dice), "Oberflächeninhalt", K.Odice(a_dice))
elif Fläche == "Quader":
     a_cube = float(input("1.Kante (a):"))
     b_cube = float(input("2.Kante (b):"))
     c_cube = float(input("3.Kante (c):"))
     print("Volumen", K.Vcube(a_cube, b_cube, c_cube), "Oberflächeninhalt", K.K.K.Ocube(a_cube, b_cube, c_cube))
elif Fläche == "Dreiecksprisma":
    a_3prism = float(input("Eine Seite des Dreiecks: "))
    ha_3prism = float(input("Höhe dieser Seite: "))
    hb_3prism = float(input("Höhe des Prismas: "))
    u =float(input("Umfang des Dreiecks: "))
    print("Volumen", K.Vtriangleprism(hb_3prism, ha_3prism, a_3prism), "Oberflächeninhalt", K.Otriangleprism(a_3prism, hb_3prism, ha_3prism, u))
elif Fläche == "Paralelogrammprisma":
    a_Pprism = float(input("Eine Seite des Paralelogramms: "))
    ha_Pprism = float(input("Höhe dieser Seite: "))
    hb_Pprism = float(input("Körperhöhe: "))
    u_Pprism = float(input("Grundseitenumfang: "))
    K.Vparalelogrammprism(hb_Pprism, ha_Pprism, a_Pprism)
    K.Oparalelogrammprism(ha_Pprism, hb_Pprism, ha_Pprism, u_Pprism)
elif Fläche == "Quadratpyramide":
    a_Py = float(input("Kantenlänge des Quadrats: "))
    hb_Py = float(input("Pyramidenhöhe: "))
    hs_py = float(input("Höhe der Seiten: "))
    K.VPyramid(a_Py, hb_Py)
    K.OPyramid(a_Py, hs_py)
elif Fläche == "Kugel":
    r_ball = float(input("radius: "))
    K.VBall(r_ball)
    K.OBall(r_ball)
else:
    print("Ungültige Eingabe! Gültige Eingaben sind: 'Würfel';'Quader';'Dreiecksprisma';'Paralelogrammprisma';'Quadratpyramide' und 'Kugel'.")