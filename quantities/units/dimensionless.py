"""
"""
from __future__ import absolute_import

from ..unitquantity import dimensionless, UnitQuantity

percent = UnitQuantity(
    'percent',
    .01*dimensionless,
    symbol='%'
)

count = counts = UnitQuantity(
    'count',
    1*dimensionless,
    symbol='ct',
    aliases=['cts', 'counts']
)

parts_per_million = UnitQuantity(
    'parts_per_million',
    1e-6*dimensionless,
    symbol='ppm'
)

del UnitQuantity
