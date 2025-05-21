# io.py
# Author: Indrajit Ghosh
# Created On: May 21, 2025
# 
import pandas as pd

def load_csv(filepath):
    df = pd.read_csv(filepath, skiprows=2)
    df.columns = ['time', 'amplitude']
    return df