import math
pi=math.pi
#C=a+bj ó a+bi
# all arguments are tuples, num, c1, c2
def pcarprint(num):#pretty print of complex number in cartesian coordinates
    print(str(num[0])+"+"+str(num[1])+"i")

def ppolprint(num):#pretty print of complex number in polar coordinates
    phi=num[1]/pi
    rho=num[0]
    print(str(rho)+"∠"+str(phi)+'\u03C0')

def cplxsum(c1,c2):#addition of complex c1 & c2
    a=c1[0]+c2[0]
    b=c1[1]+c2[1]
    return (a,b)

def cplxsus(c1,c2):#sustraction of complex c1 & c2
    a=c1[0]-c2[0]
    b=c1[1]-c2[1]
    return (a,b)

def cplxprod(c1,c2):#product of complex c1 & c2
    a=c1[0]*c2[0]-c1[1]*c2[1]
    b=c1[0]*c2[1]+c1[1]*c2[0]
    return (a,b)

def conj(c1):#conjugate of complex c1 
    a=c1[0]
    b=-c1[1]
    return (a,b)

def module(c1):#module, magnitude of complex c1
    rho=math.sqrt(c1[0]**2 +c1[1]**2)
    return rho

def cplxdiv(c1,c2):#division between complex c1 & c2
    d=module(c2)
    try:
        d=1/d
    except ZeroDivisionError:#error verification
        print("Error in calling 'div' function from libcomplex, ZeroDivisionError: division by zero")
        return 
    d=module(c2)**2
    a=(c1[0]*c2[0]+c1[1]*c2[1])/d
    b=(-c1[0]*c2[1]+c1[1]*c2[0])/d
    return (a,b) 

def phase(c1):#phase of complex c1,   a+bj form, a & b are positive real numbers
    if (c1[0]==0 and c1[1]==0):# 0+0j case
        return 0
    if (c1[0]==0 and c1[1]>0):# 0+bj case
        return pi
    if (c1[0]==0 and c1[1]<0):# 0-bj case
        return 3*pi/2

    theta=math.atan(c1[1]/c1[0])# a+bj case, first cuadrant
    if (c1[0]>0) and (c1[1]>=0):# a+bj case, first cuadrant, b can be 0
        return theta
    if (c1[0]<0) and (c1[1]>0):# -a+bj case, second cuadrant
        return abs(theta)+pi/2       
    if (c1[0]<0) and (c1[1]<=0):# -a-bj case, third cuadrant, b can be 0
        return abs(theta)+pi
    if (c1[0]>0) and (c1[1]<0):# a+bj case, fourth cuadrant
        return abs(theta)+3*pi/2

def rec2pol(c1):#rectangular to polar coordinates
    rho=module(c1)
    phi=phase(c1)
    return (rho,phi)

def pol2rec(c1):#polar to rectangular coordinates
    a=c1[0]*math.cos(c1[1])
    b=c1[0]*math.sin(c1[1])
    return (a,b)
