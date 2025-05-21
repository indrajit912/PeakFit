# analyzer.py
# Author: Indrajit Ghosh
# Created On: May 21, 2025
# 
from scipy.signal import find_peaks
import numpy as np

def find_local_maxima(df, x_min=0.3):
    filtered = df[df['time'] > x_min]
    peaks, _ = find_peaks(filtered['amplitude'])
    peak_x = filtered.iloc[peaks]['time'].values
    peak_y = filtered.iloc[peaks]['amplitude'].values
    return peak_x, peak_y

