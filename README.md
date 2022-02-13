# README

This is a README for `libcomplex.py`  and `libmatcplx.py`, a complex libraries functions for python.

---

Installation
==========

Download the folder "cnyt" from this repository with

```
git clone https://github.com/christiantorres29/cnyt.git
```

You will get a folrder with `libcomplex.py` & `libmatcplx.py`, just copy-paste the file to your working directory and import it with

```
from libcomplex import *
from libmatcplx import *
```

Usage
======

For `libcomplex.py`, a complex number *a+bj* is denoted as a tuple (a,b).

This complex library contents the following functions

* [cplxsum()](#cplxx)
* [cplxsus()](#cplxx)
* [cplxprod()](#cplxx)
* [cplxdiv()](#cplxx)
* [module()](#other-operations)
* [phase()](#other-operations)
* [conj()](#other-operations)
* [rec2pol()](#coordinates-conversion)
* [pol2rec()](#coordinates-conversion)
* [pcarprint()](#pretty-printing)
* [ppolprint()](#pretty-printing)

For `libmatcplx.py` arrays are defined like [a, b, c...] and matrices  as array of arrays, like this [[a, b, c], [d, e, f], ...]. In both cases a, b, c, d ... elements are complex numbers in form *a+bj* .

The library contents the following functions

**Vector functions**

- [vsum()](#vector-functions)
- [vinv()](#vector-functions)
- [vscp()](#vector-functions)
- [vtrans()](#vector-functions)
- [vconj()](#vector-functions)
- [vdagger()](#vector-functions)
- [vinp()](#vector-functions)
- [vnorm()](#vector-functions)
- [vdist()](#vector-functions)
- [vtprod()](#vector-functions)

**Matrix functions**

- [msum()](#cplxx)
- [minv()](#cplxx)
- [mscp()](#cplxx)
- [mtrans()](#other-operations)
- [mconj()](#other-operations)
- [mdagger()](#other-operations)
- [mprod()](#coordinates-convertion)
- [actmov()](#coordinates-convertion)
- [unitm()](#pretty-printing)
- [hertm()](#pretty-printing)
- [mtprod()](#pretty-printing)

---

## cplxX()

All these functions receive two parameters, two complex numbers as tuples, and returns one tuple. 
Resolves correspondingly to addition, sustraction, multiplication and divition of 2 complex numbers. 

```
cplxsum((a,b),(c,d))

cplxsus((a,b),(c,d))

cplxprod((a,b),(c,d))

cplxdiv((a,b),(c,d))
```

## Other operations

Magnitude `module()` of a complex number. 

Phase `phase()` in radians of a complex number, this function takes values from cero to 2 π (6.283185307179586).

Conjugate `conj()` of a complex number

whole functions returns a float.

```
module((a,b))

phase((a,b))

conj((a,b))
```

## Coordinates conversion

Convert a tuple in cartesian coordinates to polar coordinates or visceversa.

```
rec2pol((a,b))

pol2rec((a,b))
```

## Pretty printing

Pretty cartesian print and pretty polar print.

The `pcarprint()` print in *a+bj* format.

The `ppolprint()` print in *r∠θ* format, where θ are expressed in terms of π

```
pcarprint((a,b))

ppolprint((a,b))
```

---

## Vector functions

Whole vector functions receive one, or two vectors, but the functions cannot recognize between column or row vectors. 

Legend: u and v are arrays, and c is a scalar

```
vsum(u,v) ## add of v and u
vinv(u) ## aditive inverse of u
vscp(c,u) ## scalar product of c and v
vtrans(v) ## transpose(do nothing)
vconj(u) ## conjugate of u
vdagger(u) ## adjoint of u
vinnp(u,v) ## inner product between u and v
vnorm(u) ## norm of u
vdist(u,v) ## distance between u and v
vtproduct(u,v) ## tensor product between u and v
```

## Matrix functions

Whole matrix functions receive one, or two arrays.

Legend: u and v are matrices, and c is a scalar

```
msum(u,v) ## add of v and u
minv(u) ## aditive inverse of u
mscp(c,u) ## scalar product of c and v
mtrans(v) ## transpose of v
mconj(u) ## conjugate of u
mdagger(u) ## adjoint of u
mprod(u,v) ## matricial product between u and v
actmov(u,v) ## action of u on vector v
unitm(u) ## determines if u is an unitary matrix (1 yes, 0 not)
hertm(u,v) ## determines if u is an hermitian matrix (1 yes, 0 not)
mtprod(u,v) ## tensor product between u and v
```

## Author

* **Christian Torres** - *nothing to say* - [christiantorres29](https://github.com/christiantorres29/cnyt)

## License

This project is not licensed, trust me I'm a dolphin, not a virus


