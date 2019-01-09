import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_circle(center = (0, 0), npoints = 500, diameter = 2, start = 0, end = 2):
    """"
    This function creates a circle. It will be used to draw:
     - Rounded corners of boards
     - Faceoff circles
     - Faceoff dots
     - Referee's crease
     
     This returns a pandas dataframe, which will be plotted later
    """
    pts = np.linspace(start * np.pi, end * np.pi, npoints)
    x = center[0] + ((diameter / 2) * np.cos(pts))
    y = center[1] + ((diameter / 2) * np.sin(pts))
    
    return pd.DataFrame({'x':x, 'y':y})

def make_faceoff_spot(spot):
    """
    This function makes the spot for the faceoff circles. It returns a pandas dataframe to be plotted later.
    """
    
    center = (0, 0)
    
    c1 = create_circle(center = center, diameter = 2, start = -1/2, end = 1/2)
    c2 = create_circle(center = center, diameter = 2 - (4/12), start = 1/2, end = -1/2)
    
    dot = c1
    dot = dot.append(pd.DataFrame({'x':[0], 'y':[1 - (4/12)]}))
    dot = dot.append(c2)
    dot = dot.append(pd.DataFrame({'x':[0], 'y':[-1]}))
    dot = dot.append(pd.DataFrame({'x':-1 * dot['x'], 'y':dot['y']}))
    
    dot['x'] = dot['x'] + spot[0]
    dot['y'] = dot['y'] + spot[1]
    
    return dot

def make_faceoff_spot(spot):
    """
    This function makes the spot for the faceoff circles. It returns a pandas dataframe to be plotted later.
    """
    
    center = (0, 0)
    
    c1 = create_circle(center = center, diameter = 2, start = -1/2, end = 1/2)
    c2 = create_circle(center = center, diameter = 2 - (4/12), start = 1/2, end = -1/2)
    
    dot = c1
    dot = dot.append(pd.DataFrame({'x':[0], 'y':[1 - (4/12)]}))
    dot = dot.append(c2)
    dot = dot.append(pd.DataFrame({'x':[0], 'y':[-1]}))
    dot = dot.append(pd.DataFrame({'x':-1 * dot['x'], 'y':dot['y']}))
    
    dot['x'] = dot['x'] + spot[0]
    dot['y'] = dot['y'] + spot[1]
    
    return dot

def make_faceoff_spot_det(spot):
    """
    This function makes the details for the inside of a faceoff spot. It returns a pandas data frame to be plotted later.
    """    
    center = (0, 0)
    
    c1 = create_circle(center = center, diameter = 2, start = np.arccos(7/10)/np.pi, end = .5 + (np.arccos(7/10)/np.pi))
    
    dot_fill = pd.DataFrame({'x':c1['x'], 'y':c1['y'] * -1})
    
    rev = c1[::-1]
    
    dot_fill = dot_fill.append(rev)
    
    dot_fill['y'] = dot_fill['y'] * -1
    
    dot_fill['x'] = dot_fill['x'] + spot[0]
    dot_fill['y'] = dot_fill['y'] + spot[1]
    
    return dot_fill

def make_hashes(center):
    """
    This function makes the hash marks around each faceoff dot and on the outside of the circles. It returns a pandas dataframe to be plotted later.
    """
    hash1 = pd.DataFrame({
        'x':[center[0] - 6, center[0] - 2, center[0] - 2, center[0] - 6, center[0] - 6],
        'y':[center[1] - .75, center[1] - .75, center[1] - .75 - (2/12), center[1] - .75 - (2/12), center[1] - .75]
    })
    
    hash2 = pd.DataFrame({
        'x':[center[0] - 6, center[0] - 2, center[0] - 2, center[0] - 6, center[0] - 6],
        'y':[center[1] + .75, center[1] + .75, center[1] + .75 + (2/12), center[1] + .75 + (2/12), center[1] + .75]
    })
    
    hash3 = pd.DataFrame({
        'x':[center[0] + 2, center[0] + 6, center[0] + 6, center[0] + 2, center[0] + 2],
        'y':[center[1] + .75, center[1] + .75, center[1] + .75 + (2/12), center[1] + .75 + (2/12), center[1] + .75]
    })
    
    hash4 = pd.DataFrame({
        'x':[center[0] + 2, center[0] + 6, center[0] + 6, center[0] + 2, center[0] + 2],
        'y':[center[1] - .75, center[1] - .75, center[1] - .75 - (2/12), center[1] - .75 - (2/12), center[1] - .75]
    })
    
    hash5 = pd.DataFrame({
        'x':[center[0] - 2 - (2/12), center[0] - 2, center[0] - 2, center[0] - 2 - (2/12), center[0] - 2 - (2/12)],
        'y':[center[1] - .75, center[1] - .75, center[1] - 3.75, center[1] - 3.75, center[1] - .75]
    })
    
    hash6 = pd.DataFrame({
        'x':[center[0] - 2 - (2/12), center[0] - 2, center[0] - 2, center[0] - 2 - (2/12), center[0] - 2 - (2/12)],
        'y':[center[1] + .75, center[1] + .75, center[1] + 3.75, center[1] + 3.75, center[1] + .75]
    })
    
    hash7 = pd.DataFrame({
        'x':[center[0] + 2 + (2/12), center[0] + 2, center[0] + 2, center[0] + 2 + (2/12), center[0] + 2 + (2/12)],
        'y':[center[1] + .75, center[1] + .75, center[1] + 3.75, center[1] + 3.75, center[1] + .75]
    })
    
    hash8 = pd.DataFrame({
        'x':[center[0] + 2 + (2/12), center[0] + 2, center[0] + 2, center[0] + 2 + (2/12), center[0] + 2 + (2/12)],
        'y':[center[1] - .75, center[1] - .75, center[1] - 3.75, center[1] - 3.75, center[1] - .75]
    })
    
    hash9 = pd.DataFrame({
        'x':[center[0] - ((5 + (9/12)) / 2), center[0] - ((5 + (7/12)) / 2), center[0] - ((5 + (7/12)) / 2), center[0] - ((5 + (9/12)) / 2), center[0] - ((5 + (9/12)) / 2)],
        'y':[center[1] - (15 - (4/12)), center[1] - (15 - (4/12)), center[1] - 17, center[1] - 17, center[1] - (15 - (4/12))]
    })
    
    hash10 = pd.DataFrame({
        'x':[center[0] + ((5 + (9/12)) / 2), center[0] + ((5 + (7/12)) / 2), center[0] + ((5 + (7/12)) / 2), center[0] + ((5 + (9/12)) / 2), center[0] + ((5 + (9/12)) / 2)],
        'y':[center[1] - (15 - (4/12)), center[1] - (15 - (4/12)), center[1] - 17, center[1] - 17, center[1] - (15 - (4/12))]
    })
    
    hash11 = pd.DataFrame({
        'x':[center[0] - ((5 + (9/12)) / 2), center[0] - ((5 + (7/12)) / 2), center[0] - ((5 + (7/12)) / 2), center[0] - ((5 + (9/12)) / 2), center[0] - ((5 + (9/12)) / 2)],
        'y':[center[1] + (15 - (4/12)), center[1] + (15 - (4/12)), center[1] + 17, center[1] + 17, center[1] + (15 - (4/12))]
    })
    
    hash12 = pd.DataFrame({
        'x':[center[0] + ((5 + (9/12)) / 2), center[0] + ((5 + (7/12)) / 2), center[0] + ((5 + (7/12)) / 2), center[0] + ((5 + (9/12)) / 2), center[0] + ((5 + (9/12)) / 2)],
        'y':[center[1] + (15 - (4/12)), center[1] + (15 - (4/12)), center[1] + 17, center[1] + 17, center[1] + (15 - (4/12))]
    })
    
    return hash1, hash2, hash3, hash4, hash5, hash6, hash7, hash8, hash9, hash10, hash11, hash12
    

# Create the boards
corner_1_in = create_circle(center = (72, 14.5), diameter = 56, start = 1/2, end = 0)
corner_2_in = create_circle(center = (72, -14.5), diameter = 56, start = 0, end = -1/2)
corner_2_out = create_circle(center = (72, -14.5), diameter = 56 + (4/12), start = -1/2, end = 0)
corner_1_out = create_circle(center = (72, 14.5), diameter = 56 + (4/12), start = 0, end = 1/2)

boards = pd.DataFrame({'x':[0, 72], 'y':[42.5, 42.5]})
boards = boards.append(corner_1_in)
boards = boards.append(corner_2_in)
boards = boards.append(pd.DataFrame({'x':[72, 0, 0, 72], 'y':[-42.5, -42.5, -42.5 - (2/12), -42.5 - (2/12)]}))
boards = boards.append(corner_2_out)
boards = boards.append(corner_1_out)
boards = boards.append(pd.DataFrame({'x':[72, 0, 0], 'y':[42.5 + (2/12), 42.5 + (2/12), 42.5]}))

boards = boards.append(pd.DataFrame({'x':-1 * boards['x'], 'y':boards['y']}))

############################
# The five faceoff circles #
############################

# Create center faceoff circle
center_circle_in = create_circle(center = (0, 0), diameter = 30, start = -1/2, end = 1/2)
center_circle_out = create_circle(center = (0, 0), diameter = 30 - (4/12), start = 1/2, end = -1/2)

center_circle = center_circle_in
center_circle = center_circle.append(pd.DataFrame({'x':[0], 'y':[15 - (2/12)]}))
center_circle = center_circle.append(center_circle_out)
center_circle = center_circle.append(pd.DataFrame({'x':-1 * center_circle['x'], 'y':center_circle['y']}))

# Create zone faceoff circles
faceoff_circle = create_circle(center = (0, 0), diameter = 30, start = -1/2, end = 1/2)
faceoff_circle = faceoff_circle.append(pd.DataFrame({'x':[0], 'y':[7 - (2/12)]}))
faceoff_circle = faceoff_circle.append(create_circle(center = (0, 0), diameter = 30 - (4/12), start = 1/2, end = -1/2))
faceoff_circle = faceoff_circle.append(pd.DataFrame({'x':[0], 'y':[-7]}))
faceoff_circle = faceoff_circle.append(pd.DataFrame({'x':-1 * faceoff_circle['x'], 'y':faceoff_circle['y']}))

faceoff_circle_ur = pd.DataFrame({'x':faceoff_circle['x'] + 69, 'y':faceoff_circle['y'] + 22})
faceoff_circle_lr = pd.DataFrame({'x':faceoff_circle['x'] + 69, 'y':faceoff_circle['y'] - 22})
faceoff_circle_ul = pd.DataFrame({'x':faceoff_circle['x'] - 69, 'y':faceoff_circle['y'] + 22})
faceoff_circle_ll = pd.DataFrame({'x':faceoff_circle['x'] - 69, 'y':faceoff_circle['y'] - 22})


# Create ref's crease
ref_crease_out = create_circle(center = (0, -42.5), diameter = 20, start = 0, end = 1)
ref_crease_in = create_circle(center = (0, -42.5), diameter = 20 - (4/12), start = 1, end = 0)

ref_crease = ref_crease_out.append(ref_crease_in)

# Lines on the ice
blue_lines = pd.DataFrame({
    'x':[26, 25, 25, 26, 26, -26, -25, -25, -26, -26],
    'y':[-42.5, -42.5, 42.5, 42.5, -42.5, -42.5, -42.5, 42.5, 42.5, -42.5]
})

goal_lines = pd.DataFrame({
    'x':[89 - (1/12), 89 + (1/12), 89 + (1/12), 89 - (1/12), 89 - (1/12),
         -89 + (1/12), -89 - (1/12), -89 - (1/12), -89 + (1/12), -89 + (1/12)],
    'y':[-36.77, -36.77, 36.77, 36.77, -36.77, -36.77, -36.77, 36.77, 36.77, -36.77]
})

red_line = pd.DataFrame({
    'x':[-.5, .5, .5, -.5, -.5],
    'y':[-42.5, -42.5, 42.5, 42.5, -42.5]
})

restricted_area_r = pd.DataFrame({
    'x':[89, 100, 100, 89, 89,
        89, 100, 100, 89, 89, 89],
    'y':[11 - (1/12), 14 - (1/12), 14 + (1/12), 11 + (1/12), 11 - (1/12), 
        -11 + (1/12), -14 + (1/12), -14 - (1/12), -11 - (1/12), -11 + (1/12), 11 - (1/12)]
})

restricted_area_l = pd.DataFrame({
    'x':[-89, -100, -100, -89, -89, 
         -89, -100, -100, -89, -89],
    'y':[11 - (1/12), 14 - (1/12), 14 + (1/12), 11 + (1/12), 11 - (1/12), 
        -11 + (1/12), -14 + (1/12), -14 - (1/12), -11 - (1/12), -11 + (1/12)]
})

centers_b = np.linspace(-40.5, -5.5, 8).tolist()
centers_t = np.linspace(5.5, 40.5, 8).tolist()
centers = centers_b
centers.append(0)
centers.extend(centers_t)

x_bounds = [-3/12, 3/12, 3/12, -3/12, -3/12] * len(centers)
y_bounds = [-40.5 - (5/12), -40.5 - (5/12), -40.5 + (5/12), -40.5 + (5/12), -40.5 - (5/12),
            -35.5 - (5/12), -35.5 - (5/12), -35.5 + (5/12), -35.5 + (5/12), -35.5 - (5/12),
            -30.5 - (5/12), -30.5 - (5/12), -30.5 + (5/12), -30.5 + (5/12), -30.5 - (5/12),
            -25.5 - (5/12), -25.5 - (5/12), -25.5 + (5/12), -25.5 + (5/12), -25.5 - (5/12),
            -20.5 - (5/12), -20.5 - (5/12), -20.5 + (5/12), -20.5 + (5/12), -20.5 - (5/12),
            -15.5 - (5/12), -15.5 - (5/12), -15.5 + (5/12), -15.5 + (5/12), -15.5 - (5/12),
            -10.5 - (5/12), -10.5 - (5/12), -10.5 + (5/12), -10.5 + (5/12), -10.5 - (5/12),
            -5.5 - (5/12), -5.5 - (5/12), -5.5 + (5/12), -5.5 + (5/12), -5.5 - (5/12),
            -5/12, -5/12, 5/12, 5/12, -5/12,
             5.5 - (5/12), 5.5 - (5/12), 5.5 + (5/12), 5.5 + (5/12), 5.5 - (5/12),
             10.5 - (5/12), 10.5 - (5/12), 10.5 + (5/12), 10.5 + (5/12), 10.5 - (5/12),
             15.5 - (5/12), 15.5 - (5/12), 15.5 + (5/12), 15.5 + (5/12), 15.5 - (5/12),
             20.5 - (5/12), 20.5 - (5/12), 20.5 + (5/12), 20.5 + (5/12), 20.5 - (5/12),
             25.5 - (5/12), 25.5 - (5/12), 25.5 + (5/12), 25.5 + (5/12), 25.5 - (5/12),
             30.5 - (5/12), 30.5 - (5/12), 30.5 + (5/12), 30.5 + (5/12), 30.5 - (5/12),
             35.5 - (5/12), 35.5 - (5/12), 35.5 + (5/12), 35.5 + (5/12), 35.5 - (5/12),
             40.5 - (5/12), 40.5 - (5/12), 40.5 + (5/12), 40.5 + (5/12), 40.5 - (5/12)
           ]
        
red_line_details = pd.DataFrame({
    'x':x_bounds,
    'y':y_bounds
})

# Create goal crease
crease_l_outline = pd.DataFrame({
    'x':[-89],
    'y':[-4]
})

crease_l_outline = crease_l_outline.append(pd.DataFrame({
    'x':(-83 - ((1.5 * np.linspace(-4, 4, 100)**2) / 16)),
    'y':np.linspace(-4, 4, 100)
}))

crease_l_outline = crease_l_outline.append(pd.DataFrame({
    'x':[-89, -89, -85, -85, -85 + (2/12), -85 + (2/12)],
    'y':[4, 4 - (2/12), 4 - (2/12), 4 - (7/12), 4 - (7/12), 4 - (2/12)]
}))

crease_l_outline = crease_l_outline.append(pd.DataFrame({
    'x':((-83 - (2/12)) - (1.5 * np.linspace(-4, 4, 100)**2 / 16))[::-1],
    'y':np.linspace(4 - (2/12), -4 + (2/12), 100)
}))

crease_l_outline = crease_l_outline.append(pd.DataFrame({
    'x':[-85 + (2/12), -85 + (2/12), -85, -85, -89, -89],
    'y':[-4 + (2/12), -4 + (7/12), -4 + (7/12), -4 + (2/12), -4 + (2/12), -4]
}))

crease_r_outline = pd.DataFrame({
    'x': -1 * crease_l_outline['x'],
    'y': crease_l_outline['y']
})

crease_l_fill = pd.DataFrame({
    'x':[-89],
    'y':[-4 + (2/12)]
})

crease_l_fill = crease_l_fill.append(pd.DataFrame({
    'x':(-83 - (2/12)) - ((1.5 * np.linspace(-4, 4, 100)**2) / 16),
    'y':np.linspace(-4 + (2/12), 4 - (2/12), 100)
}))

crease_l_fill = crease_l_fill.append(pd.DataFrame({
    'x':[-89, -89],
    'y':[4 - (2/12), -4 + (2/12)]
}))

crease_r_fill = pd.DataFrame({
    'x':-1 * crease_l_fill['x'],
    'y':crease_l_fill['y']
})

# Create center dot
center_dot = create_circle(center = (0, 0), diameter = 1)

########################################
# The eight faceoff spots and fillings #
########################################

ur_spot = make_faceoff_spot((69, 22))
ur_spot_fill   = make_faceoff_spot_det((69, 22))

lr_spot = make_faceoff_spot((69, -22))
lr_spot_fill   = make_faceoff_spot_det((69, -22))

urnz_spot = make_faceoff_spot((20, 22))
urnz_spot_fill = make_faceoff_spot_det((20, 22))

lrnz_spot = make_faceoff_spot((20, -22))
lrnz_spot_fill =  make_faceoff_spot_det((20, -22))

ulnz_spot = make_faceoff_spot((-20, 22))
ulnz_spot_fill =  make_faceoff_spot_det((-20, 22))

llnz_spot = make_faceoff_spot((-20, -22))
llnz_spot_fill =  make_faceoff_spot_det((-20, -22))

ul_spot = make_faceoff_spot((-69, 22))
ul_spot_fill   = make_faceoff_spot_det((-69, 22))

ll_spot = make_faceoff_spot((-69, -22))
ll_spot_fill   = make_faceoff_spot_det((-69, -22))

# Create the faceoff details
ur_h1, ur_h2, ur_h3, ur_h4, ur_h5, ur_h6, ur_h7, ur_h8, ur_h9, ur_h10, ur_h11, ur_h12 = make_hashes(center = (69, 22))
lr_h1, lr_h2, lr_h3, lr_h4, lr_h5, lr_h6, lr_h7, lr_h8, lr_h9, lr_h10, lr_h11, lr_h12 = make_hashes(center = (69, -22))
ul_h1, ul_h2, ul_h3, ul_h4, ul_h5, ul_h6, ul_h7, ul_h8, ul_h9, ul_h10, ul_h11, ul_h12 = make_hashes(center = (-69, 22))
ll_h1, ll_h2, ll_h3, ll_h4, ll_h5, ll_h6, ll_h7, ll_h8, ll_h9, ll_h10, ll_h11, ll_h12 = make_hashes(center = (-69, -22))

# Create goals
goal_l_out = pd.DataFrame({
    'x':[-89],
    'y':[3]
}).append(
    create_circle(center = (-89 - (20/12), 2), diameter = (40/12), start = 1/3, end = 1)
).append(
    create_circle(center = (-89 - (20/12), -2), diameter = (40/12), start = 1, end = 5/3)
).append(
    pd.DataFrame({
        'x':[-89, -89],
        'y':[-3, -3 - (2.375/12)]
    })
).append(
    create_circle(center = (-89 - (20/12), -2), diameter = (40/12) + (4.75/12), start = 5/3, end = 1)
).append(
    create_circle(center = (-89 - (20/12), 2), diameter = (40/12) + (4.75/12), start = 1, end = 1/3)
).append(
    pd.DataFrame({
        'x':[-89],
        'y':[3 + (2.375/12)]
    })
)

goal_r_out = pd.DataFrame({
    'x':-1 * goal_l_out['x'],
    'y':goal_l_out['y']
})

goal_l_fill = pd.DataFrame({
    'x':[-89],
    'y':[3]
}).append(
    create_circle(center = (-89 - (20/12), 2), diameter = (40/12), start = 1/3, end = 1)
).append(
    create_circle(center = ((-89 - 20/12), -2), diameter = (40/12), start = 1, end = 5/3)
).append(
    pd.DataFrame({
        'x':[-89],
        'y':[-3]
    })
)

goal_r_fill = pd.DataFrame({
    'x':-1 * goal_l_fill['x'],
    'y':goal_l_fill['y']
})

#################
# Make the plot #
#################

img = 'League Logos/NHL.png'
img = plt.imread(img)

fig, ax = plt.subplots()

ax.set_aspect('equal')
fig.set_size_inches(50, 50)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Add NHL Logo
ax.imshow(img, extent = [-1 * np.sqrt(225 - (15/np.sqrt(2))**2), np.sqrt(225 - (15/np.sqrt(2))**2),-1 * np.sqrt(225 - (15/np.sqrt(2))**2), np.sqrt(225 - (15/np.sqrt(2))**2)])

# Add boards
ax.fill(boards['x'], boards['y'], '#ffcb05')

# Add goals
ax.fill(goal_l_out['x'], goal_l_out['y'], '#c8102e')
ax.fill(goal_r_out['x'], goal_r_out['y'], '#c8102e')
ax.fill(goal_l_fill['x'], goal_l_fill['y'], '#a5acaf')
ax.fill(goal_r_fill['x'], goal_r_fill['y'], '#a5acaf')

# Add hashmarks
ax.fill(ur_h1['x'], ur_h1['y'], '#c8102e')
ax.fill(ur_h2['x'], ur_h2['y'], '#c8102e')
ax.fill(ur_h3['x'], ur_h3['y'], '#c8102e')
ax.fill(ur_h4['x'], ur_h4['y'], '#c8102e')
ax.fill(ur_h5['x'], ur_h5['y'], '#c8102e')
ax.fill(ur_h6['x'], ur_h6['y'], '#c8102e')
ax.fill(ur_h7['x'], ur_h7['y'], '#c8102e')
ax.fill(ur_h8['x'], ur_h8['y'], '#c8102e')
ax.fill(ur_h9['x'], ur_h9['y'], '#c8102e')
ax.fill(ur_h10['x'], ur_h10['y'], '#c8102e')
ax.fill(ur_h11['x'], ur_h11['y'], '#c8102e')
ax.fill(ur_h12['x'], ur_h12['y'], '#c8102e')
ax.fill(lr_h1['x'], lr_h1['y'], '#c8102e')
ax.fill(lr_h2['x'], lr_h2['y'], '#c8102e')
ax.fill(lr_h3['x'], lr_h3['y'], '#c8102e')
ax.fill(lr_h4['x'], lr_h4['y'], '#c8102e')
ax.fill(lr_h5['x'], lr_h5['y'], '#c8102e')
ax.fill(lr_h6['x'], lr_h6['y'], '#c8102e')
ax.fill(lr_h7['x'], lr_h7['y'], '#c8102e')
ax.fill(lr_h8['x'], lr_h8['y'], '#c8102e')
ax.fill(lr_h9['x'], lr_h9['y'], '#c8102e')
ax.fill(lr_h10['x'], lr_h10['y'], '#c8102e')
ax.fill(lr_h11['x'], lr_h11['y'], '#c8102e')
ax.fill(lr_h12['x'], lr_h12['y'], '#c8102e')
ax.fill(ul_h1['x'], ul_h1['y'], '#c8102e')
ax.fill(ul_h2['x'], ul_h2['y'], '#c8102e')
ax.fill(ul_h3['x'], ul_h3['y'], '#c8102e')
ax.fill(ul_h4['x'], ul_h4['y'], '#c8102e')
ax.fill(ul_h5['x'], ul_h5['y'], '#c8102e')
ax.fill(ul_h6['x'], ul_h6['y'], '#c8102e')
ax.fill(ul_h7['x'], ul_h7['y'], '#c8102e')
ax.fill(ul_h8['x'], ul_h8['y'], '#c8102e')
ax.fill(ul_h9['x'], ul_h9['y'], '#c8102e')
ax.fill(ul_h10['x'], ul_h10['y'], '#c8102e')
ax.fill(ul_h11['x'], ul_h11['y'], '#c8102e')
ax.fill(ul_h12['x'], ul_h12['y'], '#c8102e')
ax.fill(ll_h1['x'], ll_h1['y'], '#c8102e')
ax.fill(ll_h2['x'], ll_h2['y'], '#c8102e')
ax.fill(ll_h3['x'], ll_h3['y'], '#c8102e')
ax.fill(ll_h4['x'], ll_h4['y'], '#c8102e')
ax.fill(ll_h5['x'], ll_h5['y'], '#c8102e')
ax.fill(ll_h6['x'], ll_h6['y'], '#c8102e')
ax.fill(ll_h7['x'], ll_h7['y'], '#c8102e')
ax.fill(ll_h8['x'], ll_h8['y'], '#c8102e')
ax.fill(ll_h9['x'], ll_h9['y'], '#c8102e')
ax.fill(ll_h10['x'], ll_h10['y'], '#c8102e')
ax.fill(ll_h11['x'], ll_h11['y'], '#c8102e')
ax.fill(ll_h12['x'], ll_h12['y'], '#c8102e')

# Add the details to each faceoff circle: the spot, the filling of the spot, the hash marks, and the faceoff configuration
ax.fill(ur_spot['x'], ur_spot['y'], '#c8102e')
ax.fill(lr_spot['x'], lr_spot['y'], '#c8102e')
ax.fill(urnz_spot['x'], urnz_spot['y'], '#c8102e')
ax.fill(lrnz_spot['x'], lrnz_spot['y'], '#c8102e')
ax.fill(ulnz_spot['x'], ulnz_spot['y'], '#c8102e')
ax.fill(llnz_spot['x'], llnz_spot['y'], '#c8102e')
ax.fill(ul_spot['x'], ul_spot['y'], '#c8102e')
ax.fill(ll_spot['x'], ll_spot['y'], '#c8102e')
ax.fill(ur_spot_fill['x'], ur_spot_fill['y'], '#c8102e')
ax.fill(lr_spot_fill['x'], lr_spot_fill['y'], '#c8102e', )
ax.fill(urnz_spot_fill['x'], urnz_spot_fill['y'], '#c8102e')
ax.fill(lrnz_spot_fill['x'], lrnz_spot_fill['y'], '#c8102e')
ax.fill(ulnz_spot_fill['x'], ulnz_spot_fill['y'], '#c8102e')
ax.fill(llnz_spot_fill['x'], llnz_spot_fill['y'], '#c8102e')
ax.fill(ul_spot_fill['x'], ul_spot_fill['y'], '#c8102e',)
ax.fill(ll_spot_fill['x'], ll_spot_fill['y'], '#c8102e')

# Add circles and referee's crease
ax.fill(center_circle['x'], center_circle['y'], '#0033a0')
ax.fill(faceoff_circle_ur['x'], faceoff_circle_ur['y'], '#c8102e')
ax.fill(faceoff_circle_lr['x'], faceoff_circle_lr['y'], '#c8102e')
ax.fill(faceoff_circle_ul['x'], faceoff_circle_ul['y'], '#c8102e')
ax.fill(faceoff_circle_ll['x'], faceoff_circle_ll['y'], '#c8102e')
ax.fill(ref_crease['x'], ref_crease['y'], '#c8102e')

# Add red line and blue lines
ax.fill(red_line['x'], red_line['y'], '#c8102e')
ax.fill(red_line_details['x'], red_line_details['y'], '#ffffff')
ax.fill(blue_lines['x'], blue_lines['y'], '#0033a0')
ax.fill(restricted_area_r['x'], restricted_area_r['y'], '#c8102e')
ax.fill(restricted_area_l['x'], restricted_area_l['y'], '#c8102e')

# Add center dot
ax.fill(center_dot['x'], center_dot['y'], '#0033a0')

# Add goal creases
ax.fill(crease_l_fill['x'], crease_l_fill['y'], '#0088ce')
ax.fill(crease_r_fill['x'], crease_r_fill['y'], '#0088ce')
ax.fill(crease_l_outline['x'], crease_l_outline['y'], '#c8102e')
ax.fill(crease_r_outline['x'], crease_r_outline['y'], '#c8102e')

# Add goal lines
ax.fill(goal_lines['x'], goal_lines['y'], '#c8102e')


plt.show()
