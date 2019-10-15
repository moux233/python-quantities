# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:52:27 2019

@author: maxime_rattier
"""

default_labels_FR = {
        'Vitesse de rotation': ['deg/h', 'mdeg/h', 'µdeg/h', 'rad/s', '°/h'],
        'Accélération': ['m/s²', 'm/s^2', 'gMarly', 'Gal'],
        'Température': ['°C', 'degC', 'm°C', 'mdegC', 'K'],
        'Temps': ['h', 'min', 's'],
        'Angle': ['deg', '°', 'arcmin', 'arcsec', 'rad', 'mrad', 'mdeg', 'µdeg'],
        'Vitesse': ['m/s', 'kn', 'km/h'],
        'Longueur': ['m', 'km', 'mm', 'µm', 'nm', 'Nq'],
        }

plotaxislabels_dict = {}

for label, symbol_list in default_labels_FR.items():
    for symbol in symbol_list:
#        print(label)
#        print(symbol)
        plotaxislabels_dict.update([(symbol, label), ])
