# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:25:54 2018

@author: Bartek
"""
from math import pi


def decimalDeg2dms(decimalDeg):
    d = int(decimalDeg)
    m = int((decimalDeg - d) * 60)
    s = (decimalDeg - d - m/60.0) * 3600
    return(d,m,s)

if __name__ == '__main__':
    wynik = decimalDeg2dms(0.910288764192757*180/pi)
    print(wynik)