"""
@author: Ross Drucker
"""
import numpy as np
import pandas as pd

def create_circle(center = (0, 0), npoints = 500, d = 2, start = 0, end = 2):
    """
    Create a set of x and y coordinates that form a circle (or the arc of a
    circle)
    
    Parameters
    ----------
    center: The (x, y) coordinates of the center of the circle. Default: (0, 0)
    npoints: The number of points with which to create the circle. This will
        also be the length of the resulting data frame. Default: 500
    d: Diameter of the circle IN THE UNITS OF THE PLOT. This default unit will
        be feet. Default: 2 (unit circle)
    start: The angle (in radians) at which to start drawing the circle, where
        zero runs along the +x axis. Default: 0
    end: The angle (in radians) at which to stop drawing the circle, where zero
        runs along the +x axis. Default: 0

    Returns
    -------
    circle_df: A pandas dataframe that contains the circle's coordinate points
    """
    # Create a vector of numbers that are evenly spaced apart between the
    # starting and ending angles. They should be multiplied by pi to be in
    # radians. This vector represents the angle through which the circle is
    # traced
    pts = np.linspace(start * np.pi, end * np.pi, npoints)
    
    # Create the vectors x and y that represent the circle (or arc of a circle)
    # to be created. This is a translation away from the center across (d/2),
    # then rotated by cos(angle) and sin(angle) for x and y respectively. 
    x = center[0] + ((d / 2) * np.cos(pts))
    y = center[1] + ((d / 2) * np.sin(pts))
    
    # Combine points into data frame for output
    circle_df = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    return circle_df