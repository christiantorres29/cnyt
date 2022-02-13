from math import *


def len_test(u,v):#compare the size of u and v
    sizeu=len(u)
    sizev=len(v)
    if sizeu!=sizev:
        raise Exception("Incompatible sizes, both vectors must be the same sizes")
    return sizeu

def square_test(u):
    rows=len(u)
    columns=len(u[0])
    if rows!=columns:
        raise Exception("Unacceptable dimension, matrix must be square")
    return rows

def dim_test(u,v):
    rowsu=len(u)
    columnsu=len(u[0])
    rowsv=len(v)
    columnsv=len(v[0])
    if (rowsu-rowsv)+(columnsu-columnsv)!=0:
        raise Exception("Incompatible dimensions, both matrices must be the same dimensions")
    return rowsu,columnsu

##vector functions
def vsum(u,v):## u plus v
    size=len_test(u,v)
    sum_=size*[0+0j]
    i=0
    while i<size:
        sum_[i]=u[i]+v[i]
        i=i+1
    return sum_

def vinv(u):## u additive inverse
    size=len(u)
    inv_=size*[0+0j]
    i=0;
    while i<size:
        inv_[i]=-u[i]
        i=i+1
    return inv_

def vscp(c,u):## c*u, scalar vector product
    size=len(u)
    prod_=size*[0+0j]
    i=0
    while i<size:
        prod_[i]=c*u[i]
        i=i+1
    return prod_

def vtrans(u):## transpose of vector u
    return u

def vconj(u):## conjugate of vector u
    size=len(u)
    vconj_=size*[0+0j]
    i=0
    while i<size:
        vconj_[i]=u[i].conjugate()
        i=i+1
    return vconj_

def vdagger(u):## adjoint of vector u
    u_t=vtrans(u)
    u_T=vconj(u_t)
    return u_T

def vinnp(u,v):## inner product of vectors u and v
    size=len_test(u,v)
    conjv=vconj(v)
    innp=0
    i=0
    while i<size:
        innp=u[i]*conjv[i]+innp
        i=i+1
    return innp

def vnorm(u):##norm of u
    vnorm_=sqrt(vinnp(u,u))
    return vnorm_

def vdist(u,v):## distance of u and v
    diff=vsus(u,v)
    dist_=vnorm(diff)
    return dist_

def vtprod(u,v):## vectorial tensor product
    lenu=len(u)
    lenv=len(v)
    result=(lenu*lenv)*[0+0j]
    i=0
    k=0
    l=0
    while i<lenu:
        while k<lenv:
            result[l]=u[i]*v[k]
            l=1+l
            k=k+1
        i=i+1
    return result

## matrix functions

def msum(u,v):## adition of matrices u and v
    size=dim_test(u, v)##########columns###################rows#####
    msum_=[[0+0j for i in range (size[1])] for i in range (size[0])]
    i=0
    k=0
    while i<size[0]:
        while k<size[1]:
            msum_[i][k]=u[i][k]+v[i][k]
            k=k+1
        i=i+1
    return msum_   

def minv(u):## additive inverse of matrix u
    size=dim_test(u, u)##########columns###################rows#####
    minv_=[[0+0j for i in range (size[1])] for i in range (size[0])]
    i=0
    k=0
    while i<size[0]:
        while k<size[1]:
            minv_[i][k]=-u[i][k]
            k=k+1
        i=i+1
    return minv_ 

def mscp(c,u):## matrix scalar product of c and u
    size=dim_test(u, u)
    mscp_=[[0+0j for i in range (size[1])] for i in range (size[0])]
    i=0
    k=0
    while i<size[0]:
        while k<size[1]:
            mscp_[i][k]=c*u[i][k]
            k=k+1
        i=i+1
    return mscp_

def mtrans(u):## transpose of matrix u
    size=dim_test(u, u)
    mtrans_==[[0+0j for i in range (size[0])] for i in range (size[1])]
    i=0
    k=0
    while i<size[1]:
        while k<size[0]:
            mtrans_[i][k]=u[k][i]
            k=k+1
        i=i+1
    return mtrans_

def mconj(u):## conjugate of matrix u
    size=dim_test(u, u)
    mconj_=[[0+0j for i in range (size[1])] for i in range (size[0])]
    i=0
    k=0
    while i<size[0]:
        while k<size[1]:
            mconj_[i][k]=u[i][k].conjugate()
            k=k+1
        i=i+1
    return mconj_

def mdagger(u):## adjoint of matrix u
    size=dim_test(u, u)
    mconju_=[[0+0j for i in range (size[1])] for i in range (size[0])]
    mconju_=mconj(u)
    mdagger_=[[0+0j for i in range (size[0])] for i in range (size[1])]
    mdagger_=mtrans(mconju_)
    return mdagger_

def mprod(u,v):## matrix product between u and v
    sizeu=dim_test(u, u)
    sizev=dim_test(v, v)
    if sizeu[1]!=sizev[0]:
        raise Exception("Incompatible dimensions, number of columns of u must be the same as the number of rows of v")
    size=(sizeu[0],sizev[1])
    result=[[0+0j for i in range (size[1])] for i in range (size[0])]
    v_t=mtrans(v)
    i=0
    k=0
    while i<size[0]:
        while k<size[1]:
            result[i][k]=vinnp(u[i][:], v_t[k][:])
            k=k+1
        i=i+1
    return result    

def actmov(u,v):## action of matrix u on vector v
    (m,n)=dim_test(u, u)
    n_=len(v)
    if n!=n_:
        raise Exception("Incompatible dimensions, number of columns of u must be the same as the number of elements of v")
    result=m*[0+0j]
    i=0
    while i<m:
        result[i]=vinnp(u[i][:], v[i])
        i=i+1
    return result  

def unitm(u):## returns 1 if u is an unitary matrix, else 0
    size=square_test(u)######columns#################rows#####
    mI=[[0+0j for i in range (size)] for i in range (size)]
    while i<size:
        mI[i][i]=1
        i=i+1
    andjoint=mdagger(u)
    uut=mprod(u, u)
    if uut==mI:
        return 1
    else:
        return 0

def hertm(u):## returns 1 if u is an hermitian matrix, else 0
    size=square_test(u)
    andjoint=mdagger(u)
    if u==andjoint:
        return 1
    else:
        return 0

def mtprod(u,v):## matricial tensor product
    sizeu=dim_test(u, u)
    sizev=dim_test(v, v)
    m=sizeu[0]*sizev[0]##rows
    n=sizeu[1]*sizev[1]##columns
    result_=[[0+0j for i in range (n)] for i in range (m)]
    i=0
    k=0    
    while i<m:
        while k<n:
            result_[i][k]=u[j//sizev[0]][k//sizev[1]]*v[i%sizev[0]][k%sizev[1]]
            k=k+1
        i=i+1
    return result_