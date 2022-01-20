import math
pi=math.pi
#C=a+bj ó a+bi

def pcarprint(num):
    print(str(num[0])+"+"+str(num[1])+"i")

def ppolprint(num):
    print(str(num[0])+"∠"+str(num[1]))

def suma(c1,c2):
    a=c1[0]+c2[0]
    b=c1[1]+c2[1]
    return (a,b)

def resta(c1,c2):
    a=c1[0]-c2[0]
    b=c1[1]-c2[1]
    return (a,b)

def prod(c1,c2):
    a=c1[0]*c2[0]-c1[1]*c2[1]
    b=c1[0]*c2[1]+c1[1]*c2[0]
    return (a,b)

def conj(c1):
    a=c1[0]
    b=-c1[1]
    return (a,b)

def module(c1):
    rho=math.sqrt(c1[0]**2 +c1[1]**2)
    return rho

def div(c1,c2):
    d=module(c2)
    try:
        d=1/d
    except ZeroDivisionError:
        print("Error in calling \"div\" function from 'libcomplex', ZeroDivisionError: division by zero")
        return 
    d=module(c2)**2
    a=(c1[0]*c2[0]+c1[1]*c2[1])/d
    b=(-c1[0]*c2[1]+c1[1]*c2[0])/d
    return (a,b) 

def phase(c1):
    if (c1[0]==0 and c1[1]==0):
        return 0
    if (c1[0]==0 and c1[1]>0):
        return pi
    if (c1[0]==0 and c1[1]<0):
        return 3*pi/2

    theta=math.atan(c1[1]/c1[0])
    if (c1[0]>0) and (c1[1]>=0):
        return theta
    if (c1[0]<0) and (c1[1]>0):
        return abs(theta)+pi/2       
    if (c1[0]<0) and (c1[1]<=0):
        return abs(theta)+pi
    if (c1[0]>0) and (c1[1]<0):
        return abs(theta)+3*pi/2

def rec2pol(c1):
    rho=module(c1)
    phi=phase(c1)
    return (rho,phi)

def pol2rec(c1):
    a=c1[0]*math.cos(c1[1])
    b=c1[0]*math.sin(c1[1])
    return (a,b)