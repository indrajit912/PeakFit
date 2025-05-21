# analyzer.py
# Author: Indrajit Ghosh
# Created On: May 21, 2025
# 
from scipy.signal import find_peaks
import numpy as np


from scipy.signal import find_peaks

def find_local_maxima(df, x_min=0.3, prominence=0.001):
    filtered_df = df[df['time'] >= x_min].reset_index(drop=True)
    y = filtered_df['amplitude'].values

    peaks, _ = find_peaks(y, prominence=prominence)
    x_max = filtered_df['time'].iloc[peaks].values
    y_max = y[peaks]

    return x_max, y_max
