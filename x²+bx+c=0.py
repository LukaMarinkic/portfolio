def Lösungsformel():
    print("Normalform: x² + bx + c = 0 muss gegeben sein")
    b = int(input("b = "))
    c = int(input("c = "))
    print( "x1 =", -(b/2) + ((b/2) ** 2 -c) ** 0.5,  "x2 =", -(b/2) - ((b/2) ** 2 -c) ** 0.5)

Lösungsformel()

input("press enter: ")