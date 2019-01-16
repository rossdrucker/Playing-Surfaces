#####################################################################################
#####################################################################################
## This script produces a matplotlib version of a regulation NFL field. Each unit  ##
## in x and y is equivalent to one foot (12 in) and all parts of the model are     ##
## drawn to scale.                                                                 ##
#####################################################################################
#####################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create field, sideline markings, goal lines, and the 50 yard line
field = pd.DataFrame({
    'x':[-190, 190, 190, -190, -190],
    'y':[-90, -90, 90, 90, -90]
})

sideline = pd.DataFrame({
    'x':[-180, 180, 180, -180, -180],
    'y':[-86, -86, -80, -80, -86]
}).append(
    pd.DataFrame({
        'x':[-180, 180, 180, -180, -180],
        'y':[80, 80, 86, 86, 80]
    })
)

endline = pd.DataFrame({
    'x':[-186, -180, -180, -186, -186],
    'y':[-86, -86, 86, 86, -86]
}).append(
    pd.DataFrame({
        'x':[180, 186, 186, 180, 180],
        'y':[-86, -86, 86, 86, -86]
    })
)

goal_line = pd.DataFrame({
    'x':[-150 - (2/12), -150 + (2/12), -150 + (2/12), -150 - (2/12), -150 - (2/12)],
    'y':[-86, -86, 86, 86, -86]
}).append(
    pd.DataFrame({
        'x':[150 - (2/12), 150 + (2/12), 150 + (2/12), 150 - (2/12), 150 - (2/12)],
        'y':[-86, -86, 86, 86, -86]
    })
)

midline = pd.DataFrame({
    'x':[-2/12, 2/12, 2/12, -2/12, -2/12],
    'y':[-80 + (4/12), -80 + (4/12), -20 + (4/12), -20 + (4/12), -80 + (4/12)]
}).append(
    pd.DataFrame({
        'x':[-2/12, 2/12, 2/12, -2/12, -2/12],
        'y':[20 - (4/12), 20 - (4/12), 80 - (4/12), 80 - (4/12), 20 - (4/12)]
    })
)

# Create all of the minor yard lines (there are four sets)
minor_yd_lines_b = pd.DataFrame({
    'x':[],
    'y':[]
})

for i in range(1, 50):
    minor_yd_lines_b = minor_yd_lines_b.append(
        pd.DataFrame({
            'x':[(0 - (3 * i)) - (2/12), (0 - (3 * i)) + (2/12), (0 - (3 * i)) + (2/12), (0 - (3 * i)) - (2/12), (0 - (3 * i)) - (2/12)],
            'y':[-80 + (4/12), -80 + (4/12), -78 + (4/12), -78 + (4/12), -80 + (4/12)]
        })
    )

minor_yd_lines_b = minor_yd_lines_b.append(
    pd.DataFrame({
        'x':-1 * minor_yd_lines_b['x'],
        'y':minor_yd_lines_b['y']
    })
)

minor_yd_lines_t = pd.DataFrame({
    'x':minor_yd_lines_b['x'],
    'y':-1 * minor_yd_lines_b['y']
})

minor_yd_lines_l = pd.DataFrame({
    'x':minor_yd_lines_b['x'],
    'y':minor_yd_lines_b['y'] + 58
})

minor_yd_lines_u = pd.DataFrame({
    'x':minor_yd_lines_l['x'],
    'y':-1 * minor_yd_lines_l['y']
})

# Create the major yard lines (every 5 yards excluding the 50)
major_yd_lines = pd.DataFrame({
    'x':[],
    'y':[]
})

major_yd_lines_ft = np.arange(15, 150, 15)

for i in range(0, len(major_yd_lines_ft)):
    major_yd_lines = major_yd_lines.append(
        pd.DataFrame({
            'x':[major_yd_lines_ft[i] - (2/12), major_yd_lines_ft[i] + (2/12), major_yd_lines_ft[i] + (2/12), major_yd_lines_ft[i] - (2/12), major_yd_lines_ft[i] - (2/12)],
            'y':[-80 + (4/12), -80 + (4/12), 80 - (4/12), 80 - (4/12), -80 + (4/12)]
        })
    )
    
major_yd_lines = major_yd_lines.append(
    pd.DataFrame({
        'x':-1 * major_yd_lines['x'],
        'y':major_yd_lines['y']
    })
)

# Create the hash marks at every 5 yard line
hashes = pd.DataFrame({
    'x':[],
    'y':[]
})

for i in range(1, 10):
    hashes = hashes.append(
        pd.DataFrame({
            'x':[(0 - (15 * i)) - (10/12), (0 - (15 * i)) + (10/12), (0 - (15 * i)) + (10/12), (0 - (15 * i)) - (10/12), (0 - (15 * i)) - (10/12)],
            'y':[-20 + (4/12), -20 + (4/12), -20 + (2/12), -20 + (2/12), -20 + (4/12)]
        })
    )
    
hashes_l = hashes.append(
    pd.DataFrame({
        'x':-1 * hashes['x'],
        'y':hashes['y']
    })
)

hashes_u = pd.DataFrame({
    'x':hashes_l['x'],
    'y':hashes_l['y'] + 39.5
})

# Create the extra point marker
extra_pt_mark = pd.DataFrame({
    'x':[-141 - (2/12), -141 + (2/12), -141 + (2/12), -141 - (2/12), -141 - (2/12)],
    'y':[-1, -1, 1, 1, -1]
})

extra_pt_mark = extra_pt_mark.append(
    pd.DataFrame({
        'x':-1 * extra_pt_mark['x'],
        'y':extra_pt_mark['y']
    })
)

# Create the arrows next to each of the numbers on the field indicating direction
arrow_40 = pd.DataFrame({
    'x':[-36.5 - (6/12), -36.5 - (6/12), -36.5 - ((np.sqrt((36 ** 2) - 36))/12), -36.5 - (6/12), -36.5 - (6/12)],
    'y':[-44, -44 + (9/12), -44, -44 - (9/12), -44]
})

arrow_40_l = arrow_40.append(
    pd.DataFrame({
        'x':-1 * arrow_40['x'],
        'y':arrow_40['y']
    })
)

arrow_40_u = pd.DataFrame({
    'x':arrow_40_l['x'],
    'y':arrow_40_l['y'] + 92
})

arrow_30 = pd.DataFrame({
    'x':[-66.5 - (6/12), -66.5 - (6/12), -66.5 - ((np.sqrt((36 ** 2) - 36))/12), -66.5 - (6/12), -66.5 - (6/12)],
    'y':[-44, -44 + (9/12), -44, -44 - (9/12), -44]
})

arrow_30_l = arrow_30.append(
    pd.DataFrame({
        'x':-1 * arrow_30['x'],
        'y':arrow_30['y']
    })
)

arrow_30_u = pd.DataFrame({
    'x':arrow_30_l['x'],
    'y':arrow_30_l['y'] + 92
})

arrow_20 = pd.DataFrame({
    'x':[-96.5 - (6/12), -96.5 - (6/12), -96.5 - ((np.sqrt((36 ** 2) - 36))/12), -96.5 - (6/12), -96.5 - (6/12)],
    'y':[-44, -44 + (9/12), -44, -44 - (9/12), -44]
})

arrow_20_l = arrow_20.append(
    pd.DataFrame({
        'x':-1 * arrow_20['x'],
        'y':arrow_20['y']
    })
)

arrow_20_u = pd.DataFrame({
    'x':arrow_20_l['x'],
    'y':arrow_20_l['y'] + 92
})

arrow_10 = pd.DataFrame({
    'x':[-126.5 - (6/12), -126.5 - (6/12), -126.5 - ((np.sqrt((36 ** 2) - 36))/12), -126.5 - (6/12), -126.5 - (6/12)],
    'y':[-44, -44 + (9/12), -44, -44 - (9/12), -44]
})

arrow_10_l = arrow_10.append(
    pd.DataFrame({
        'x':-1 * arrow_10['x'],
        'y':arrow_10['y']
    })
)

arrow_10_u = pd.DataFrame({
    'x':arrow_10_l['x'],
    'y':arrow_10_l['y'] + 92
})

#################
# Make the plot #
#################
fig, ax = plt.subplots()

ax.set_aspect('equal')
fig.set_size_inches(50, 22.2)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Set field color
ax.set_facecolor('#196f0c')

# Put NFL logo at midfield
img = 'League Logos/nfl.png'
img = plt.imread(img)
ax.imshow(img, extent = [-18., 18., -18., 18.])

# Add sidelines, goal line, and 50 yard line
ax.fill(sideline['x'], sideline['y'], '#ffffff')
ax.fill(endline['x'], endline['y'], '#ffffff')
ax.fill(goal_line['x'], goal_line['y'], '#ffffff')
ax.fill(midline['x'], midline['y'], '#ffffff')

# Add minor yard lines and major yard lines
ax.fill(minor_yd_lines_b['x'], minor_yd_lines_b['y'], '#ffffff')
ax.fill(minor_yd_lines_t['x'], minor_yd_lines_t['y'], '#ffffff')
ax.fill(minor_yd_lines_l['x'], minor_yd_lines_l['y'], '#ffffff')
ax.fill(minor_yd_lines_u['x'], minor_yd_lines_u['y'], '#ffffff')
ax.fill(major_yd_lines['x'], major_yd_lines['y'], '#ffffff')

# Add hash marks and extra point markers
ax.fill(hashes_l['x'], hashes_l['y'], '#ffffff')
ax.fill(hashes_u['x'], hashes_u['y'], '#ffffff')
ax.fill(extra_pt_mark['x'], extra_pt_mark['y'], '#ffffff')

# Add the numbers to the field
ax.text(-6.5, -46, '5', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(.25, 46, '5', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(1.25, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-6.75, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(-36.5, -46, '4', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-29.75, 46, '4', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(-28.75, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-36.75, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(-66.5, -46, '3', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-59.75, 46, '3', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(-58.75, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-66.75, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(-96.5, -46, '2', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-89.75, 46, '2', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(-88.75, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-96.75, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(-126.5, -46, '1', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-119.75, 46, '1', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(-118.75, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(-126.75, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(23.5, -46, '4', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(30.25, 46, '4', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(31.25, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(23.25, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(53.5, -46, '3', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(60.25, 46, '3', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(61.25, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(53.25, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(83.5, -46, '2', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(90.25, 46, '2', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(91.25, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(83.25, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

ax.text(113.5, -46, '1', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(120.25, 46, '1', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)
ax.text(121.25, -46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold')
ax.text(113.25, 46, '0', color = '#ffffff', fontsize = 50, fontweight = 'bold', rotation = 180)

# Add the arrows to the field
ax.fill(arrow_40_l['x'], arrow_40_l['y'], '#ffffff')
ax.fill(arrow_40_u['x'], arrow_40_u['y'], '#ffffff')
ax.fill(arrow_30_l['x'], arrow_30_l['y'], '#ffffff')
ax.fill(arrow_30_u['x'], arrow_30_u['y'], '#ffffff')
ax.fill(arrow_20_l['x'], arrow_20_l['y'], '#ffffff')
ax.fill(arrow_20_u['x'], arrow_20_u['y'], '#ffffff')
ax.fill(arrow_10_l['x'], arrow_10_l['y'], '#ffffff')
ax.fill(arrow_10_u['x'], arrow_10_u['y'], '#ffffff')

plt.show()