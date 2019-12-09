#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import degrees, atan2
from PyQt5.QtCore import QLineF


def route_fond(xd, yd, xa, ya):
    line = QLineF(xd, yd, xa, ya)
    angle = atan2(line.dy(), line.dx())
    if degrees(angle) <= -90:
        return round(90 - degrees(angle),1)
    else:
        return round(90 + degrees(angle),1)
