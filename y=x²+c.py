# Automating Math: y=x²+c

searched = input("What is searched (press: y or x or c then enter): ") # what is searched

if searched == "y":
    print("everything in cm | y is searched")
    xy = int(input("what is x? : "))
    cy = int(input("what is c? : "))
    yy = (xy*xy)+cy
    print("y is ", yy)
elif searched == "x":
    print("everything in cm | x is searched")
    yx = int(input("what is y? : "))
    cx = int(input("what is c? : "))
    x2x = yx-cx
    xx = x2x ** 0.5
    print("x is: ", xx)
elif searched == "c":
    print("everything in cm | c is searched")
    yc = int(input("what is y? : "))
    xc = int(input("what is x? : "))
    cc = yc-(xc*xc)
    print("c is: ", cc)
else : 
    print("Invalid input")

input("press enter: ")