from math import *

#size= len(y) 
#matrizMedia = [[(0,0) for i in range (size)] for i in range (size)]

##rise Exception("incompatible sizes")

def length_test(u,v):
    sizeu=len(u)
    sizev=len(v)
    if sizeu!=sizev:
        rise Exception("incompatible sizes")
    return sizeu

def vsum(u,v):
    size=length_test(u,v)
    sum_=size*[0+0j]
    i=0
    while i<size:
        sum_[i]=u[i]+v[i]
        i=i+1
    return sum_

def vsus(u,v):
    size=length_test(u,v)
    sus_=size*[0+0j]
    i=0;
    while i<size:
        sus_[i]=u[i]-v[i]
        i=i+1
    return sus_

def inv(u):
    size=len(u)
    inv_=size*[0+0j]
    i=0;
    while i<size:
        inv_[i]=-u[i]
        i=i+1
    return inv

def esc_prod(c,u):
    size=len(u)
    prod_=size*[0+0j]
    i=0;
    while i<size:
        prod_[i]=c*u[i]
        i=i+1
    return prod_

