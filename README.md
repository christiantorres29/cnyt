# README

This is a README for `libcomplex.py`, a complex library functions for python

Installation
==========

Download the folder "cnyt" from this repository with
```
git clone https://github.com/christiantorres29/cnyt.git
```
You will get a folrder with `libcomplex.py`, just copy-paste the file to your working directory and import it with

```
from libcomplex import *
```
Usage
======
For this library, a complex number *a+bj* is denoted as a tuple like (a,b)

This complex library contents the following functions

* [cplxsum()](#cplxx)
* [cplxsus()](#cplxx)
* [cplxprod()](#cplxx)
* [cplxdiv()](#cplxx)
* [module()](#other-operations)
* [phase()](#other-operations)
* [conj()](#other-operations)
* [rec2pol()](#coordinates-convertion)
* [pol2rec()](#coordinates-convertion)
* [pcarprint()](#pretty-printing)
* [ppolprint()](#pretty-printing)

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

## Author

* **Christian Torres** - *First commit* - [christiantorres29](https://github.com/christiantorres29/cnyt)

## License

This project is not licensed, trust me I'm a dolphin, not a virus



