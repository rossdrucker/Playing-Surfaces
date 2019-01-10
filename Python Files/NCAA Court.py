######################################################################################
######################################################################################
## This script produces a matplotlib version of a regulation NCAA basketball court. ##
## Each unit in x and y is equivalent to one foot (12 in) and all parts of the      ##
## model are drawn to scale.                                                        ##
######################################################################################
######################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_circle(center = (0, 0), npoints = 500, diameter = 2, start = 0, end = 2):
    """"
    This function creates a circle. It will be used to draw:
     - Center circle
     - Three-point arc
     - Restricted area
     - Hoop
     - Top of free throw lane
     
     This returns a pandas dataframe, which will be plotted later
    """
    pts = np.linspace(start * np.pi, end * np.pi, npoints)
    x = center[0] + ((diameter / 2) * np.cos(pts))
    y = center[1] + ((diameter / 2) * np.sin(pts))
    
    return pd.DataFrame({'x':x, 'y':y})

# Create court interior
court = pd.DataFrame({
    'x':[-47, 47, 47, -47, -47],
    'y':[-25, -25, 25, 25, -25]
})

# Create court boundaries
baseline = pd.DataFrame({
    'x':[-47 - (8/12), -47, -47, -47 - (8/12), -47 - (8/12)],
    'y':[-25 - (8/12), -25 - (8/12), 25 + (8/12), 25 + (8/12), -25 - (8/12)]
})

baselines = baseline.append(pd.DataFrame({
    'x':-1 * baseline['x'],
    'y':baseline['y']
}))

sideline = pd.DataFrame({
    'x':[-47 - (8/12), 47 + (8/12), 47 + (8/12), -47 - (8/12), -47 - (8/12)],
    'y':[-25 - (8/12), -25 - (8/12), -25, -25, -25 - (8/12)]
})

sidelines = sideline.append(pd.DataFrame({
    'x':sideline['x'],
    'y':-1 * sideline['y']
}))

coaches_box = pd.DataFrame({
    'x':[
         -19 - (2/12), -19 - (2/12), -19, -19, -19 - (2/12),
          19 + (2/12),  19 + (2/12),  19,  19,  19 + (2/12)
    ],
    'y':[22, 28, 28, 22, 22, 22, 28, 28, 22, 22]
})

substitution_area = pd.DataFrame({
    'x':[
         -9 - (2/12), -9 - (2/12), -9, -9, -9 - (2/12),
          9 + (2/12),  9 + (2/12),  9,  9,  9 + (2/12)
    ],
    'y':[
         25 + (8/12), 27 + (8/12), 27 + (8/12), 25 + (8/12), 25 + (8/12),
         25 + (8/12), 27 + (8/12), 27 + (8/12), 25 + (8/12), 25 + (8/12)
    ]
})

# Create time line
timeline = pd.DataFrame({
    'x':[-1/12, 1/12, 1/12, -1/12, -1/12],
    'y':[-25, -25, 25, 25, -25]
})

# Create center circle
center_circle = create_circle(center = (0, 0), diameter = 12, start = -1/2, end = 1/2).append(
    pd.DataFrame({
        'x':[0],
        'y':[6 - (2/12)]
    })
).append(
    create_circle(center = (0, 0), diameter = 12 - (4/12), start = 1/2, end = -1/2)
).append(
    pd.DataFrame({
        'x':[0],
        'y':[-6]
    })
)

center_circle = center_circle.append(pd.DataFrame({
    'x':-1 * center_circle['x'],
    'y':center_circle['y']
}))

# Create 3-point lines
three_pt_line = pd.DataFrame({
    'x':[-47],
    'y':[-20.75]
}).append(
    create_circle(center = (-41.75, 0), diameter = 41.5, start = -1/2, end = 1/2)
).append(
    pd.DataFrame({
        'x':[-47, -47],
        'y':[20.75, 20.75 - (2/12)]
    })
).append(
    create_circle(center = (-41.75, 0), diameter = 41.5 - (4/12), start = 1/2, end = -1/2)
).append(
    pd.DataFrame({
        'x':[-47, -47],
        'y':[-20.75 + (2/12), -20.75]
    })
)

three_pt_line = three_pt_line.append(
    pd.DataFrame({
        'x':-1 * three_pt_line['x'],
        'y':three_pt_line['y']
    })
)

# Create the lane
lane = pd.DataFrame({
    'x':[-47, -28, -28, -47, -47, -28 - (2/12), -28 - (2/12), -47, -47, -47,
          47,  28,  28,  47,  47,  28 + (2/12),  28 + (2/12),  47,  47,  47],
    'y':[-6, -6, 6, 6, 6 - (2/12), 6 - (2/12), -6 + (2/12), -6 + (2/12), 6, -6,
         -6, -6, 6, 6, 6 - (2/12), 6 - (2/12), -6 + (2/12), -6 + (2/12), 6, -6]
})

# Create free throw circle
free_throw_circle = create_circle(center = (-28, 0), start = -1/2, end = 1/2, diameter = 12).append(
    pd.DataFrame({
        'x':[-28],
        'y':[6]
    })
).append(
    create_circle(center = (-28, 0), start = 1/2, end = -1/2, diameter = 12 - (4/12))
).append(
    pd.DataFrame({
        'x':[-28],
        'y':[-6]
    })
)

free_throw_circles = free_throw_circle.append(
    pd.DataFrame({
        'x':-1 * free_throw_circle['x'],
        'y':free_throw_circle['y']
    })
)

# Create blocks for free throws
blocks1_l = pd.DataFrame({
    'x':[
        -40, -39, -39, -40, -40,
        -40, -39, -39, -40, -40
    ],
    'y':[
        -6 - (8/12), -6 - (8/12), -6, -6, -6 - (8/12),
         6 + (8/12),  6 + (8/12),  6,  6,  6 + (8/12)
    ]
})


blocks1_r = pd.DataFrame({
    'x':-1 * blocks1_l['x'],
    'y':blocks1_l['y']
})

blocks2_l = pd.DataFrame({
    'x':[
        -36, -36 + (2/12), -36 + (2/12), -36, -36,
        -36, -36 + (2/12), -36 + (2/12), -36, -36
    ],
    'y':[
        -6 - (8/12), -6 - (8/12), -6, -6, -6 - (8/12),
         6 + (8/12),  6 + (8/12),  6,  6,  6 + (8/12)
    ]
})

blocks2_r = pd.DataFrame({
    'x':-1 * blocks2_l['x'],
    'y':blocks2_l['y']
})

blocks3_l = pd.DataFrame({
    'x':[
        -33 + (2/12), -33 + (4/12), -33 + (4/12), -33 + (2/12), -33 + (2/12),
        -33 + (2/12), -33 + (4/12), -33 + (4/12), -33 + (2/12), -33 + (2/12)
    ],
    'y':[
        -6 - (8/12), -6 - (8/12), -6, -6, -6 - (8/12),
         6 + (8/12),  6 + (8/12),  6,  6,  6 + (8/12)
    ]
})

blocks3_r = pd.DataFrame({
    'x':-1 * blocks3_l['x'],
    'y':blocks3_l['y']
})

blocks4_l = pd.DataFrame({
    'x':[
        -30 + (4/12), -30 + (6/12), -30 + (6/12), -30 + (4/12), -30 + (4/12),
        -30 + (4/12), -30 + (6/12), -30 + (6/12), -30 + (4/12), -30 + (4/12)
    ],
    'y':[
        -6 - (8/12), -6 - (8/12), -6, -6, -6 - (8/12),
         6 + (8/12),  6 + (8/12),  6,  6,  6 + (8/12)
    ]
})

blocks4_r = pd.DataFrame({
    'x':-1 * blocks4_l['x'],
    'y':blocks4_l['y']
})

# Create restricted arc
restricted_arc = pd.DataFrame({
    'x':[-43],
    'y':[-4 - (2/12)]
}).append(
    create_circle(center = (-41.75, 0), diameter = 8 + (4/12), start = -1/2, end = 1/2)
).append(
    pd.DataFrame({
        'x':[-43, -43],
        'y':[4 + (2/12), 4]
    })
).append(
    create_circle(center = (-41.75, 0), diameter = 8, start = 1/2, end = -1/2)
).append(
    pd.DataFrame({
        'x':[-43, -43],
        'y':[-4, -4 - (2/12)]
    })
)

restricted_arcs = restricted_arc.append(
    pd.DataFrame({
        'x':-1 * restricted_arc['x'],
        'y':restricted_arc['y']
    })
)

# Create backboards
backboard = pd.DataFrame({
    'x':[-43 - (4/12), -43, -43, -43 - (4/12), -43 - (4/12)],
    'y':[-3, -3, 3, 3, -3]
})

backboards = backboard.append(
    pd.DataFrame({
        'x':-1 * backboard['x'],
        'y':backboard['y']
    })
)

# Create rim
rim_connector = pd.DataFrame({
    'x':[-43, -42.3, -42.3, -43, -43],
    'y':[-4/12, -4/12, 4/12, 4/12, -4/12]
})

rim_connectors = rim_connector.append(
    pd.DataFrame({
        'x':-1 * rim_connector['x'],
        'y':rim_connector['y']
    })
)

rim = create_circle(center = (-41.75, 0), diameter = 1.5 + (4/12))
rims = rim.append(
    pd.DataFrame({
        'x':-1 * rim['x'],
        'y':rim['y']
    })
)

# Create nets
net = create_circle(center = (-41.75, 0), diameter = 1.5)
nets = net.append(
    pd.DataFrame({
        'x':-1 * net['x'],
        'y':net['y']
    })
)

#################
# Make the plot #
#################

fig, ax = plt.subplots()

ax.set_aspect('equal')
fig.set_size_inches(50, 50)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Add court coloring
ax.fill(court['x'], court['y'], '#d2ab6f')

# Add baselines, sidelines, substitution area, and coaches' box markings to court
ax.fill(baselines['x'], baselines['y'], '#000000')
ax.fill(sidelines['x'], sidelines['y'], '#000000')
ax.fill(substitution_area['x'], substitution_area['y'], '#000000')
ax.fill(coaches_box['x'], coaches_box['y'], '#000000')

# Add time line
ax.fill(timeline['x'], timeline['y'], '#000000')

# Add center circle
ax.fill(center_circle['x'], center_circle['y'], '#000000')

# Add 3-point lines
ax.fill(three_pt_line['x'], three_pt_line['y'], '#000000')

# Add the lanes and free throw circles
ax.fill(lane['x'], lane['y'], '#000000')
ax.fill(free_throw_circles['x'], free_throw_circles['y'], '#000000')

# Add the blocks
ax.fill(blocks1_l['x'], blocks1_l['y'], '#000000')
ax.fill(blocks1_r['x'], blocks1_r['y'], '#000000')
ax.fill(blocks2_l['x'], blocks2_l['y'], '#000000')
ax.fill(blocks2_r['x'], blocks2_r['y'], '#000000')
ax.fill(blocks3_l['x'], blocks3_l['y'], '#000000')
ax.fill(blocks3_r['x'], blocks3_r['y'], '#000000')
ax.fill(blocks4_l['x'], blocks4_l['y'], '#000000')
ax.fill(blocks4_r['x'], blocks4_r['y'], '#000000')

# Add the restricted arcs
ax.fill(restricted_arcs['x'], restricted_arcs['y'], '#000000')

# Add backboards, rims, nets
ax.fill(backboards['x'], backboards['y'], '#000000')
ax.fill(rim_connectors['x'], rim_connectors['y'], '#e04e39')
ax.fill(rims['x'], rims['y'], '#e04e39')
ax.fill(nets['x'], nets['y'], '#ffffff')

plt.show()
