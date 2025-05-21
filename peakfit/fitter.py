# fitter.py
# Author: Indrajit Ghosh
# Created On: May 21, 2025
# 
from scipy.interpolate import UnivariateSpline
import numpy as np

def fit_spline(x, y, smooth_factor=0.0):
    return UnivariateSpline(x, y, s=smooth_factor)

def fit_polynomial(x, y, degree=3):
    coeffs = np.polyfit(x, y, degree)
    return np.poly1d(coeffs)
