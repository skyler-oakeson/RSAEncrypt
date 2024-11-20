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
        ### your code here
        pass

    @staticmethod
    def generate_keys_from_pqe(p, q, e):
        ### your code here
        pass
    
    @staticmethod
    def encrypt(m, pk):
        ### your code here
        pass
      
    @staticmethod
    def decrypt(c, sk):
        ### your code here
        pass

    @staticmethod
    def encrypt_text(text, pub_key):
        ### your code here
        pass
       
    @staticmethod
    def decrypt_cryptotexts(cryptotexts, sec_key):
        ### your code here
        pass
    
    


    
