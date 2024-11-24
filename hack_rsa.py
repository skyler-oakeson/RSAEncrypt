#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: hack_rsa.py
# description: obtaining RSA's secret key from messages,
# cryptotexts, and public keys.
# Skyler Oakeson
# A02308556
#############################################################

import math
from rsa_aux import xgcd
from rsa_aux import mult_inv, euler_phi, is_prime, find_primes_in_range
from rsa import rsa

class hack_rsa(object):

    @staticmethod
    def get_sec_key(message, cryptotext, pub_key):
        e, n = pub_key
        primes = find_primes_in_range(1, n)
        for p in primes:
            for q in primes:
                if p * q == n:
                    d = mult_inv(e, (p-1)*(q-1))
                    return (d, n)
        return None
