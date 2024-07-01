def wurzel (R:int):
    W = R ** 0.5
    print("Die Wurzel aus ", R,"ist", W)
def Quadrat (B:int):
    P= B*B
    print(B," hoch zwei ist ", P)

Prompt = str(input("Was willst du (wurzel/quadrieren): "))

if Prompt == "wurzel":
    Ra = int(input("Die Wurzel aus: "))
    wurzel(Ra)
else:   
    if Prompt == "quadrieren":
        Basis = int(input("Welche Zahl willst du quadrieren: "))
        Quadrat(Basis)
    else:
        print("Ungültige Eingaben")

input("Drücken sie Enter ")