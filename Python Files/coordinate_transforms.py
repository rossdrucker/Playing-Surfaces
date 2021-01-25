"""
@author: Ross Drucker
"""
import math
import numpy as np
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

def rotate(df, rotation_dir = 'ccw', angle = .5):
    if rotation_dir.lower() not in ['ccw', 'counter', 'counterclockwise']:
        angle *= -1
    theta = angle * np.pi
    rotated = df.copy()
    rotated['x'] = (df['x'] * math.cos(theta)) - (df['y'] * math.sin(theta))
    rotated['y'] = (df['x'] * math.sin(theta)) + (df['y'] * math.cos(theta))
    
    return rotated