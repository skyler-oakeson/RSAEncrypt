#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: rsa.py
# description: RSA
# Skyler Oakeson
# A02308556
#############################################################

import numpy as np
from rsa_aux import xgcd
from rsa_aux import mult_inv, euler_phi, is_prime
import math
import random

class rsa(object):

    @staticmethod
    def choose_e(eu_phi_n):
        rel = [i for i in range(1, eu_phi_n) if xgcd(i, eu_phi_n)[0] == 1]
        return rel[random.randint(0, len(rel)-1)]

    @staticmethod
    def generate_keys_from_pqe(p, q, e):
        n = p*q
        d = mult_inv(e, euler_phi(n))
        return (e, n), (d, n)

    
    @staticmethod
    def encrypt(m, pk):
        e, n = pk
        return (m**e) % n
      
    @staticmethod
    def decrypt(c, sk):
        d, n = sk
        return (c**d) % n


    @staticmethod
    def encrypt_text(text, pub_key):
        encrypted = []
        for char in text:
            encrypted.append(rsa.encrypt(ord(char), pub_key))
        return encrypted

       
    @staticmethod
    def decrypt_cryptotexts(cryptotexts, sec_key):
        decrypted = ""
        for num in cryptotexts:
            decrypted += chr(rsa.decrypt(num, sec_key))
        return decrypted
    
    


    
