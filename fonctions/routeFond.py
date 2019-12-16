#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import degrees, atan2
from PyQt5.QtCore import QLineF


def route_compas(xd, yd, xa, ya):
    line = QLineF(xd, yd, xa, ya)
    angle = atan2(line.dy(), line.dx())
    if degrees(angle) <= -90:
        return round(90 - degrees(angle),1)
    else:
        return round(90 + degrees(angle),1)


def cap_compas(Rs,Der,D,d):
    Cv = Rs - Der
    Cm = Cv - D
    Cc = Cm - d
    if Cc > 360:
        Cc = Cc - 360
    print ("Cap compas", Cc,"°")
    return Cc

# route fond -> cap compas
# route de fond -> route de surface

def route_surface (Cc, d,D ,Der) :
    Cm = Cc + d
    Cv = Cm + D
    Rs = Cv + Der
    print("Route de surface", Rs,"°")
    return Rs

"""
def xxxx(Rf, *****):
    return Cc, Rs
"""