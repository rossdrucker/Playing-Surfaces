#####################################################################################
#####################################################################################
## This script produces a matplotlib version of a regulation NBA court. Each unit  ##
## in x and y is equivalent to one foot (12 in) and all parts of the model are     ##
## drawn to scale.                                                                 ##
#####################################################################################
#####################################################################################

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

# Create court
court_border = pd.DataFrame({
    'x':[-55, 55, 55, -55, -55],
    'y':[-30, -30, 30, 30, -30]
})

court = pd.DataFrame({
    'x':[-47, 47, 47, -47, -47],
    'y':[-25, -25, 25, 25, -25]
})

# Create court boundaries
baselines = pd.DataFrame({
    'x':[-47 - (2/12), -47, -47, -47 - (2/12), -47 - (2/12)],
    'y':[-25 - (2/12), -25 - (2/12), 25 + (2/12), 25 + (2/12), -25 - (2/12)]
}).append(
    pd.DataFrame({
        'x':[47, 47 + (2/12), 47 + (2/12), 47, 47],
        'y':[-25 - (2/12), -25 - (2/12), 25 + (2/12), 25 + (2/12), -25 - (2/12)]
    })
)

sidelines = pd.DataFrame({
    'x':[-47 - (2/12), 47 + (2/12), 47 + (2/12), -47 - (2/12), -47 - (2/12)],
    'y':[-25 - (2/12), -25 - (2/12), -25, -25, -25 - (2/12)]
}).append(
    pd.DataFrame({
        'x':[-47 - (2/12), 47 + (2/12), 47 + (2/12), -47 - (2/12), -47 - (2/12)],
        'y':[25, 25, 25 + (2/12), 25 + (2/12), 25]
    })
)

coaches_box_l = pd.DataFrame({
    'x':[-19, -19 + (2/12), -19 + (2/12), -19, -19,
         -19, -19 + (2/12), -19 + (2/12), -19, -19],
    'y':[-25, -25, -22, -22, -25,
          22,  22,  25,  25,  22]
})

coaches_box_r = pd.DataFrame({
    'x':-1 * coaches_box_l['x'],
    'y':coaches_box_l['y']
})

substitution_area = pd.DataFrame({
    'x':[-4 - (4/12), -4 - (2/12), -4 - (2/12), -4 - (4/12), -4 - (4/12),
          4 + (2/12),  4 + (4/12),  4 + (4/12),  4 + (2/12),  4 + (2/12)],
    'y':[25 + (2/12), 25 + (2/12), 29 + (2/12), 29 + (2/12), 25 + (2/12),
         25 + (2/12), 25 + (2/12), 29 + (2/12), 29 + (2/12), 25 + (2/12)]
})

# Create time line
timeline = pd.DataFrame({
    'x':[-1/12, 1/12, 1/12, -1/12, -1/12],
    'y':[-25, -25, 25, 25, -25]
})

# Create center circles
inner_circle = create_circle(center = (0, 0), diameter = 4, start = 1/2, end = 3/2).append(
    pd.DataFrame({
        'x':[0],
        'y':[-2 - (2/12)]
    })
).append(
    create_circle(center = (0, 0), diameter = 4 + (4/12), start = 3/2, end = 1/2)
).append(
    pd.DataFrame({
        'x':[0],
        'y':[2]
    })
)

inner_circle = inner_circle.append(
    pd.DataFrame({
        'x':-1 * inner_circle['x'],
        'y':inner_circle['y']
    })
)

outer_circle = create_circle(center = (0, 0), diameter = 12, start = 1/2, end = 3/2).append(
    pd.DataFrame({
        'x':[0],
        'y':[-6 + (2/12)]
    })
).append(
    create_circle(center = (0, 0), diameter = 12 - (4/12), start = 3/2, end = 1/2)
).append(
    pd.DataFrame({
        'x':[0],
        'y':[6 - (2/12)]
    })
)

outer_circle = outer_circle.append(
    pd.DataFrame({
        'x':-1 * outer_circle['x'],
        'y':outer_circle['y']
    })
)

# Create lane and free throw circle
lane = pd.DataFrame({
    'x':[-47, -28, -28, -47, -47, -28 - (2/12), -28 - (2/12), -47, -47, -28 - (2/12), -28 - (2/12), -47, -47, -28 - (2/12), -28 - (2/12), -47, -47],
    'y':[-8, -8, 8, 8, 8 - (2/12), 8 - (2/12), 6, 6, 6 - (2/12), 6 - (2/12), -6 + (2/12), -6 + (2/12), -6, -6, -8 + (2/12), -8 + (2/12), -8]
})

lane = lane.append(
    pd.DataFrame({
        'x':-1 * lane['x'],
        'y':lane['y']
    })
)

free_throw_circle = create_circle(
    center = (-28, 0), 
    diameter = 12, 
    start = (-1/2) - ((12.29/72)/np.pi), 
    end = (1/2) + ((12.29/72)/np.pi)
).append(
    create_circle(
        center = (-28, 0),
        diameter = 12 - (4/12),
        start = (1/2) + ((12.20/72)/np.pi),
        end = (-1/2) - ((12.29/72)/np.pi)
    )
)

free_throw_circle = free_throw_circle.append(
    free_throw_circle[:1]
)

free_throw_circle = free_throw_circle.append(
    pd.DataFrame({
        'x':-1 * free_throw_circle['x'],
        'y':free_throw_circle['y']
    })
)

d1 = create_circle(
    center = (-28, 0), 
    diameter = 12, 
    start = (1/2) + (((12.29/72) + (15.5/72))/np.pi),
    end = (1/2) + (((12.29/72) + (31/72))/np.pi)
).append(
    create_circle(
        center = (-28, 0),
        diameter = 12 - (4/12),
        start = (1/2) + (((12.29/72) + (31/72))/np.pi),
        end = (1/2) + (((12.29/72) + (15.5/72))/np.pi)
    )
)

# Dashes for bottom half of free throw circle
d1 = d1.append(
    d1[:1]
)

d1 = d1.append(
    pd.DataFrame({
        'x':-1 * d1['x'],
        'y':d1['y']
    })
)

d2 = pd.DataFrame({
        'x':d1['x'],
        'y':-1 * d1['y']
})

d3 = create_circle(
    center = (-28, 0),
    diameter = 12,
    start = (1/2) + (((12.29/72) + (46.5/72))/np.pi), 
    end = (1/2) + (((12.20/72) + (62/72))/np.pi)
).append(
    create_circle(
        center = (-28, 0),
        diameter = 12 - (4/12),
        start = (1/2) + (((12.20/72) + (62/72))/np.pi),
        end = (1/2) + (((12.29/72) + (46.5/72))/np.pi)
    )
)

d3 = d3.append(
    d3[:1]
)

d3 = d3.append(
    pd.DataFrame({
        'x':-1 * d3['x'],
        'y':d3['y']
    })
)

d4 = pd.DataFrame({
        'x':d3['x'],
        'y':-1 * d3['y']
})

d5 = create_circle(
    center = (-28, 0),
    diameter = 12,
    start = (1/2) + (((12.29/72) + (77.5/72))/np.pi),
    end = (1/2) + (((12.20/72) + (93/72))/np.pi)
).append(
    create_circle(
        center = (-28, 0),
        diameter = 12 - (4/12),
        start = (1/2) + (((12.20/72) + (93/72))/np.pi),
        end = (1/2) + (((12.29/72) + (77.5/72))/np.pi)
    )
)

d5 = d5.append(
    d5[:1]
)

d5 = d5.append(
    pd.DataFrame({
        'x':-1 * d5['x'],
        'y':d5['y']
    })
)

d6 = pd.DataFrame({
        'x':d5['x'],
        'y':-1 * d5['y']
})

# Create hash marks in lane and on baseline
hash_baseline_l = pd.DataFrame({
    'x':[-47, -46.5, -46.5, -47, -47,
         -47, -46.5, -46.5, -47, -47],
    'y':[-11 - (2/12), -11 - (2/12), -11, -11, -11 - (2/12),
          11, 11, 11 + (2/12), 11 + (2/12), 11]
})

hash_baseline_r = pd.DataFrame({
    'x':-1 * hash_baseline_l['x'],
    'y':hash_baseline_l['y']
})

hash_lane_l = pd.DataFrame({
    'x':[-34, -34 + (2/12), -34 + (2/12), -34, -34,
         -34, -34 + (2/12), -34 + (2/12), -34, -34],
    'y':[-5, -5, -4.5, -4.5, -5,
          4.5, 4.5, 5, 5, 4.5]
})

hash_lane_r = pd.DataFrame({
    'x':-1 * hash_lane_l['x'],
    'y':hash_lane_l['y']
})

# Add blocks
blocks1_out_l = pd.DataFrame({
    'x':[-40, -40 + (2/12), -40 + (2/12), -40, -40,
         -40, -40 + (2/12), -40 + (2/12), -40, -40],
    'y':[-8, -8, -8.5, -8.5, -8,
          8,  8,  8.5,  8.5,  8]
})

blocks1_out_r = pd.DataFrame({
    'x':-1 * blocks1_out_l['x'],
    'y':blocks1_out_l['y']
})

blocks1_in_l = pd.DataFrame({
    'x':[-40, -39, -39, -40, -40,
         -40, -39, -39, -40, -40],
    'y':[-6, -6, -6.5, -6.5, -6,
          6,  6,  6.5,  6.5,  6]
})

blocks1_in_r = pd.DataFrame({
    'x':-1 * blocks1_in_l['x'],
    'y':blocks1_in_l['y']
})

blocks2_out_l = pd.DataFrame({
    'x':[-39 - (2/12), -39, -39, -39 - (2/12), -39 - (2/12),
         -39 - (2/12), -39, -39, -39 - (2/12), -39 - (2/12)],
    'y':[-8, -8, -8.5, -8.5, -8,
          8,  8,  8.5,  8.5,  8]
})

blocks2_out_r = pd.DataFrame({
    'x':-1 * blocks2_out_l['x'],
    'y':blocks2_out_l['y']
})

blocks2_in_l = pd.DataFrame({
    'x':[-36, -36 + (2/12), -36 + (2/12), -36, -36,
         -36, -36 + (2/12), -36 + (2/12), -36, -36],
    'y':[-6, -6, -6.5, -6.5, -6,
          6,  6,  6.5,  6.5,  6]
})

blocks2_in_r = pd.DataFrame({
    'x':-1 * blocks2_in_l['x'],
    'y':blocks2_in_l['y']
})

blocks3_out_l = pd.DataFrame({
    'x':[-36, -36 + (2/12), -36 + (2/12), -36, -36,
         -36, -36 + (2/12), -36 + (2/12), -36, -36],
    'y':[-8, -8, -8.5, -8.5, -8,
          8,  8,  8.5,  8.5,  8]
})

blocks3_out_r = pd.DataFrame({
    'x':-1 * blocks3_out_l['x'],
    'y':blocks3_out_l['y']
})

blocks3_in_l = pd.DataFrame({
    'x':[-33 + (2/12), -33 + (4/12), -33 + (4/12), -33 + (2/12), -33 + (2/12),
         -33 + (2/12), -33 + (4/12), -33 + (4/12), -33 + (2/12), -33 + (2/12)],
    'y':[-6, -6, -6.5, -6.5, -6,
          6,  6,  6.5,  6.5,  6]
})

blocks3_in_r = pd.DataFrame({
    'x':-1 * blocks3_in_l['x'],
    'y':blocks3_in_l['y']
})

blocks4_out_l = pd.DataFrame({
    'x':[-33 + (2/12), -33 + (4/12), -33 + (4/12), -33 + (2/12), -33 + (2/12),
         -33 + (2/12), -33 + (4/12), -33 + (4/12), -33 + (2/12), -33 + (2/12)],
    'y':[-8, -8, -8.5, -8.5, -8,
          8,  8,  8.5,  8.5,  8]
})

blocks4_out_r = pd.DataFrame({
    'x':-1 * blocks4_out_l['x'],
    'y':blocks4_out_l['y']
})

blocks4_in_l = pd.DataFrame({
    'x':[-30 + (4/12), -30 + (6/12), -30 + (6/12), -30 + (4/12), -30 + (4/12),
         -30 + (4/12), -30 + (6/12), -30 + (6/12), -30 + (4/12), -30 + (4/12)],
    'y':[-6, -6, -6.5, -6.5, -6,
          6,  6,  6.5,  6.5,  6]
})

blocks4_in_r = pd.DataFrame({
    'x':-1 * blocks4_in_l['x'],
    'y':blocks4_in_l['y']
})

# Create three-point arc
three_pt_arc_out = create_circle(center = (-41.75, 0), diameter = 47.5, start = 1/2, end = -1/2)
three_pt_arc_out = three_pt_arc_out[(three_pt_arc_out['y'] >= -22) & (three_pt_arc_out['y'] <= 22)]

three_pt_arc_in = create_circle(center = (-41.75, 0), diameter = 47.5 - (4/12), start = -1/2, end = 1/2)
three_pt_arc_in = three_pt_arc_in[(three_pt_arc_in['y'] >= -22 + (2/12)) & (three_pt_arc_in['y'] <= 22 - (2/12))]

three_pt_line = pd.DataFrame({
    'x':[-47],
    'y':[22]
}).append(
    three_pt_arc_out
).append(
    pd.DataFrame({
        'x':[-47, -47],
        'y':[-22, -22 + (2/12)]
    })
).append(
    three_pt_arc_in
).append(
    pd.DataFrame({
        'x':[-47, -47],
        'y':[22 - (2/12), 22]
    })
)

three_pt_line = three_pt_line.append(
    pd.DataFrame({
        'x':-1 * three_pt_line['x'],
        'y':three_pt_line['y']
    })
)

# Create restricted area
restricted_area = pd.DataFrame({
    'x':[-41.7 - (15/12), -41.7],
    'y':[-4, -4]
}).append(
    create_circle(
        center = (-42 + (3/12), 0),
        diameter = 8,
        start = -1/2,
        end = 1/2
    )
).append(
    pd.DataFrame({
        'x':[-41.7, -41.7 - (15/12), -41.7 - (15/12), -41.7],
        'y':[4, 4, 4 - (2/12), 4 - (2/12)]
    })
).append(
    create_circle(
        center = (-42 + (3/12), 0),
        diameter = 8 - (4/12),
        start = 1/2,
        end = -1/2
    )
).append(
    pd.DataFrame({
        'x':[-41.7, -41.7 - (15/12), -41.7 - (15/12)],
        'y':[-4 + (2/12), -4 + (2/12), -4]
    })
)

restricted_area = restricted_area.append(
    pd.DataFrame({
        'x':-1 * restricted_area['x'],
        'y':restricted_area['y']
    })
)

# Create backboard and basket
backboard = pd.DataFrame({
    'x':[-43 - (2/12), -43, -43, -43 - (2/12), -43 - (2/12)],
    'y':[-3, -3, 3, 3, -3]
})

backboard = backboard.append(
    pd.DataFrame({
        'x':-1 * backboard['x'],
        'y':backboard['y']
    })
)

rim_connector = pd.DataFrame({
    'x':[-43, -42.3, -42.3, -43, -43],
    'y':[-4/12, -4/12, 4/12, 4/12, -4/12]
})

rim_connector = rim_connector.append(
    pd.DataFrame({
        'x':-1 * rim_connector['x'],
        'y':rim_connector['y']
    })
)

rim = create_circle(center = (-41.75, 0), diameter = 1.5 + (4/12), start = 0, end = 2)
rim = rim.append(
    pd.DataFrame({
        'x':-1 * rim['x'],
        'y':rim['y']
    })
)

net = create_circle(center = (-41.75, 0), diameter = 1.5, start = 0, end = 2)
net = net.append(
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
ax.fill(court_border['x'], court_border['y'], '#000000')
ax.fill(court['x'], court['y'], '#d2ab6f')

# Add baselines, sidelines, substitution area, and coaches' box markings to court
ax.fill(baselines['x'], baselines['y'], '#ffffff')
ax.fill(sidelines['x'], sidelines['y'], '#ffffff')
ax.fill(substitution_area['x'], substitution_area['y'], '#ffffff')
ax.fill(coaches_box_l['x'], coaches_box_l['y'], '#ffffff')
ax.fill(coaches_box_r['x'], coaches_box_r['y'], '#ffffff')

# Add time line
ax.fill(timeline['x'], timeline['y'], '#000000')

# Add center circles
ax.fill(inner_circle['x'], inner_circle['y'], '#000000')
ax.fill(outer_circle['x'], outer_circle['y'], '#000000')

# Add the lane
ax.fill(lane['x'], lane['y'], '#000000')
ax.fill(free_throw_circle['x'], free_throw_circle['y'], '#000000')
ax.fill(d1['x'], d1['y'], '#000000')
ax.fill(d2['x'], d2['y'], '#000000')
ax.fill(d3['x'], d3['y'], '#000000')
ax.fill(d4['x'], d4['y'], '#000000')
ax.fill(d5['x'], d5['y'], '#000000')
ax.fill(d6['x'], d6['y'], '#000000')

# Add hash marks
ax.fill(hash_baseline_l['x'], hash_baseline_l['y'], '#ffffff')
ax.fill(hash_baseline_r['x'], hash_baseline_r['y'], '#ffffff')
ax.fill(hash_lane_l['x'], hash_lane_l['y'], '#000000')
ax.fill(hash_lane_r['x'], hash_lane_r['y'], '#000000')

# Add blocks
ax.fill(blocks1_out_l['x'], blocks1_out_l['y'], '#000000')
ax.fill(blocks1_out_r['x'], blocks1_out_r['y'], '#000000')
ax.fill(blocks2_out_l['x'], blocks2_out_l['y'], '#000000')
ax.fill(blocks2_out_r['x'], blocks2_out_r['y'], '#000000')
ax.fill(blocks3_out_l['x'], blocks3_out_l['y'], '#000000')
ax.fill(blocks3_out_r['x'], blocks3_out_r['y'], '#000000')
ax.fill(blocks4_out_l['x'], blocks4_out_l['y'], '#000000')
ax.fill(blocks4_out_r['x'], blocks4_out_r['y'], '#000000')
ax.fill(blocks1_in_l['x'], blocks1_in_l['y'], '#000000')
ax.fill(blocks1_in_r['x'], blocks1_in_r['y'], '#000000')
ax.fill(blocks2_in_l['x'], blocks2_in_l['y'], '#000000')
ax.fill(blocks2_in_r['x'], blocks2_in_r['y'], '#000000')
ax.fill(blocks3_in_l['x'], blocks3_in_l['y'], '#000000')
ax.fill(blocks3_in_r['x'], blocks3_in_r['y'], '#000000')
ax.fill(blocks4_in_l['x'], blocks4_in_l['y'], '#000000')
ax.fill(blocks4_in_r['x'], blocks4_in_r['y'], '#000000')

# Add three-point lines
ax.fill(three_pt_line['x'], three_pt_line['y'], '#000000')

# Add restricted areas
ax.fill(restricted_area['x'], restricted_area['y'], '#000000')

# Add backboards and baskets
ax.fill(backboard['x'], backboard['y'], '#000000')
ax.fill(rim_connector['x'], rim_connector['y'], '#e04e39'),
ax.fill(rim['x'], rim['y'], '#e04e39')
ax.fill(net['x'], net['y'], '#ffffff')

plt.show()