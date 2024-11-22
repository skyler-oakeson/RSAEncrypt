#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa_aux.py
# description: auxiliay functions for RSA
# Skyler Oakeson
# A02308556
##############################################################

import numpy as np
import math

def xgcd(a, b):
    ''' 
    extended gcd that returns d, x, y such that
    d = ax + by.
    '''

    if a == 0:
        return b, 0, 1

    d, x1, y1 = xgcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1

    return d, x, y

    pass


def mult_inv(a, n):
    """
    multiplicative inverse of a in Z^{*}_{n}.
    """
    d, x, y = xgcd(a, n)
    if d != 1:
        return None

    return (x % n + n) % n

### A tool you may want to use in your code.
### it's used in rsa_uts.py.
def z_star_sub_n(n):
    """
    compute the elements of Z^{*}_{n}; same as z_star_sub_n_elts.
    """
    return np.array([i for i in range(n) if xgcd(i, n)[0] == 1])

### A tool you may want to use in your code (e.g., euler's totient)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 2:
        for d in range(3, int(math.floor(math.sqrt(n)))+1, 2):
            if n % d == 0:
                return False
        return True

### A tool you may want to use in your tests (e.g., euler's totient)
def find_primes_in_range(a, b):
    return [i for i in range(a, b+1) if is_prime(i)]


def euler_phi(n):
    """ Euler's Totient """
    tot = 0
    for i in range(1, n):
        d, _, _ = xgcd(i, n) 
        if d == 1:
            tot += 1
    return tot
