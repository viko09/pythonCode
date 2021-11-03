# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:30:00 2021

@author: luiso
"""
from scipy import special as scipy



SA=(scipy.comb(26, 13, exact=True)-2)/scipy.comb(52, 13, exact=True)

print("P(A) = ",SA)

SB=6*(scipy.comb(26, 13, exact=True)-2)/scipy.comb(52, 13, exact=True)

print("P(B) = ",SB)



