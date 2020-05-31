# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:15:28 2018

@author: User
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:44:42 2018
 
@author: kinga
Algorytm Hirvonena - algorytm służący do transformacji współrzędnych ortokartezjańskich (prostokątnych) x, y, z 
na współrzędne geodezyjne B, L, h. Jest to proces iteracyjny. 
W wyniku 3-4-krotnego powtarzania procedury można przeliczyć współrzędne na poziomie dokładności 1 cm.
"""
from math import sin, cos,  atan, sqrt, degrees
from moje_metody import decimalDeg2dms
import linecache 

def Np(B, a, e2):
    '''Compute East-West Radius of curvature at current position'''
    N = a/(1-e2*(sin(B))**2)**(0.5)
    return N
 
def hirvonen(X, Y, Z, a = 6378137., e2 = 0.00669438002290):
    r  = sqrt(X**2 + Y**2)          # promień
    B  = atan(Z / (r * (1 - e2)))    # pierwsze orzyblizenie m:0.908177798236740
    # 1) pętla for: iteracyjne wyznaczenie B
    B_next = B
    i = 0
    while True:
        i +=1
        B_prev = B_next
#        print('------------- numer iteracji',i)
#        print('B_prev', B_prev)
#        N  = Np(B_prev, a, e2)
        N = a/(1-e2*(sin(B_prev))**2)**(0.5)
        H  = (r/cos(B_prev))- N
        B_next = atan(Z/(r *(1 - (e2 * (N/(N + H))))))
#        print('B_next', B_next)
        B_next = B_next
        if abs(B_next - B_prev) <(0.0000001/206265): # warunek iteracji(rho'' =206265)
            break
    B = B_prev
    L = atan(Y/X)
#    N = Np(B, a, e2)
    N = a/(1-e2*(sin(B))**2)**(0.5)
    H = (r/cos(B))- N
    return degrees(B), degrees(L), H  # 

#plik = open("hirv_data.txt", "r")
#linie = plik.readlines()
#del linie[0]
#for linia in linie:
#    b = linia.split(',')
#    X = float(b[0])
#    Y = float(b[1])
#    Z = float(b[2])
#    B, L, H = hirvonen(X, Y, Z)
#    print('\nB', decimalDeg2dms(B))
#    print('L', decimalDeg2dms(L))
#    print('H', H)
#plik.close()
 
# inicjalizacja współrzednych XYZ:
X = 3721407.0; Y= 1240527.0; Z = 5005587.0
r = sqrt(X**2 + Y**2 + Z**2)
print('promien', r)
B, L, H = hirvonen(X, Y, Z) # wywołanie funkcji hirvonen: wyniki: (52, 2, 5.05901) (18, 23, 23.92083)  555.40334
print('\nB', B)
print('L', decimalDeg2dms(L))
print('H', H)


