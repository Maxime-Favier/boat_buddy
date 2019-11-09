#!/usr/bin/env python
# -*- coding: utf-8 -*-


def WGS84DegToDec(D, M, S):
    """
    Convertis les degrés sexadecimal en degrés decimal
    @note: Ddec=D+M/60+S/3600
    @type D: int
    @param D: WGS84 degrés
    @type M: int
    @param M: WGS84 minutes
    @type S: float
    @param S: WGS84 secondes
    @rtype: float
    @return: variable WGS84 decimal
    @since: 0.9
    @version: 0.9
    @author: Maxime Favier
    """
    return D + M / 60 + S / 3600
