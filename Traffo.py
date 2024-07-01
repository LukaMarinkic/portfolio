searched = str(input("Was ist gesucht: "))

if searched == "U1":
    U2 = float(input("U2: "))
    Wdg1 = float(input("Wdg1: "))
    Wdg2 = float(input("Wdg2: "))
    print("U1 =", (Wdg1/Wdg2)*U2)
elif searched == "U2":
    U1 = float(input("U1:"))
    Wdg1 = float(input("Wdg1: "))
    Wdg2 = float(input("Wdg2: "))
    print("U2 =", U1 / (Wdg1/Wdg2))
elif searched == "I2":
    I1 = float(input("I1: "))
    Wdg1 = float(input("Wdg1: "))
    Wdg2 = float(input("Wdg2: "))
    print("I2 =", (Wdg1/Wdg2)*I1)
elif searched == "I1":
    I2 = float(input("I2:"))
    Wdg1 = float(input("Wdg1: "))
    Wdg2 = float(input("Wdg2: "))
    print("I1 =", I2 / (Wdg1/Wdg2))
elif searched == "Wdg1":
    Wdg2  = float(input("Wdg2: "))
    U1 = float(input("U1: "))
    U2 = float(input("U2: "))
    print("Wdg1  =", (U1/U2)*Wdg2) 
elif searched == "Wdg2":
    Wdg1 = float(input("Wdg1:"))
    U1 = float(input("U1: "))
    U2 = float(input("U2: "))
    print("I1 =", Wdg1 / (U1/U2))
else :
    print("Ungültige Eingabe! Gültige Eingaben sind: 'U1','U2','I1','I2','Wdg1','Wdg2' ")