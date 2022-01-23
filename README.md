# README

This is a README for `libcomplex.py`, a complex library functions for python

INSTALLING
==========

Download the folder "cnyt" from this repository with
```
git clone https://github.com/christiantorres29/cnyt.git
```
You will get a folrder with `libcomplex.py`, just copy-paste the file to your working directory and import it with

```
from libcomplex import *
```
USAGE
======
For this library, a complex number *a+bj* is denoted as a tuple like (a,b)

This complex library contents the following functions

* [cplxsum()](##cplxX())
* [cplxsus()](##cplxX())
* [cplxprod()](##cplxX())
* [cplxdiv()](##cplxX())
* [module()](##Other-operations)
* [phase()](##Other-operations)
* [conj()](##Other-operations)
* [rec2pol()](##Coordinates-convertion)
* [pol2rec()](##Coordinates-convertion)
* [pcarprint()](##Pretty-printing)
* [ppolprint()](##Pretty-printing)

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

Phase `phase()` in radians of a complex number, this function takes values from cero to 2 $\pi$ (6.283185307179586).

Conjugate `conj()` of a complex number

whole functions returns a float.
```
module((a,b))

phase((a,b))

conj((a,b))
```
## Coordinates convertion
Convert a tuple in cartesian coordinates to polar coordinates or visceversa.

```
rec2pol((a,b))

pol2rec((a,b))
```
## Pretty printing
Pretty cartesian print and pretty polar print.

The `pcarprint()` print in *a+bj* format.

The `ppolprint()` print in *r∠$\theta$* format, where $\theta$ are expressed in terms of $\pi$

```
pcarprint((a,b))

ppolprint((a,b))
```

## Authors

* **Christian Torres** - *First commit* - [christiantorres29](https://github.com/christiantorres29/cnyt)

## License

This project is not licensed, trust me I'm a dolphin, not a virus



