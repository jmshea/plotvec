'''Module to plot 2-d vectors as arrows using Matplotlib.  
Uses Matplotlib to plot 2-d vectors as directional arrows. Allows
chaining sequence of vectors for effects like sums of vectors, and
allows labeling and color shifting (to coordinate colors of multiple
calls to plotvec).

Created by John M. Shea, copyright 2023
for the book Introduction to Data Science for Engineers

All files in the package are distributed under the MIT License
'''

__version__ = '1.7.2'

from .plotvec import plotvec, plotvecR
from .transforms import transform_unit_vecs, transform_field 
