"""
@author: Ross Drucker
"""
import pandas as pd

def reflect(df, over_x = False, over_y = True):
    out = df.copy()
    if over_y:
        out = pd.DataFrame({
            'x': -1 * out['x'],
            'y': out['y']
        })
        
    if over_x:
        out = pd.DataFrame({
            'x': out['x'],
            'y': -1 * out['y']
        })
        
    return out