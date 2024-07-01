def Vdice(a:float):
    return a ** 3
def Vcube(a:float,b:float,c:float):
    return a*b*c
def Vtriangleprism(hb:float,ha:float,a:float,):
    G = 1/2*ha*a
    return G*hb
def Vparalelogrammprism(hb:float,ha:float,a:float):
    G = ha*a
    return G*hb
def VPyramid(a:float,h:float):
    G= a*a
    V = 1/3 * G * h
    return V
def VBall(r:float):
    return 4/3 * r**3 * 22/7
def VCilnder (r:float, h:float):
    return (22/7 * (r ** 2)) * h

def Odice(a:float):
    return 6*(a**2)
def Ocube(a:float,b:float,c:float):
    return 2*(a*b+b*c+c*a)
def Otriangleprism(a:float,hb:float,ha:float,u:float):
    G = 1/2*ha*a
    M = u*hb
    return 2*G + M
def Oparalelogrammprism(a:float,hb:float,ha:float,u:float):
    G = a*ha
    M = u*hb 
    return 2*G + M
def OPyramid(a:float,hs:float):
    return a ** 2 + 4 * ((a + hs)/2)
def OBall(r:float):
    return 4*(22/7)*r ** 2
def OCilinder (r:float, h:float):
    return 2*22/7* r ** 2 + 2 * 22/7 * r *h