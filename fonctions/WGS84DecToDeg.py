#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import trunc

def WGS84DecToDeg(Ddec):
    """
    Convertis les degrés decimal en degrés sexadecimal
    @note: Ddec=D+M/60+S/3600
    @type Ddec: float
    @param Ddec: angle en WGS84 decimal
    @rtype: tuple
    @return: variable WGS84 sexadecimal
    @since: 0.8
    @version: 0.8
    @author: Maxime Favier
    """
    D = trunc(Ddec)
    M = trunc(60 * (abs(Ddec - D)))
    S = 3600 * abs(Ddec - D) - 60 * M
    return D, M, S