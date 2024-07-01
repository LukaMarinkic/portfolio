Satz = int(input("Welcher Strahlensatz (1/2):"))
gesucht = str(input("Was ist gesucht(SA/SA'/SB/SB'/AB/AB'): "))
if gesucht == "SA":
    SA1 = float(input("Was ist SA': "))
    SB = float(input("SB: "))
    SB1 = float(input("SB':"))
    SA = (SB/SB1)*SA1
    print("SA =", SA)