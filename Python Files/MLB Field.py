#####################################################################################
#####################################################################################
## This script produces a matplotlib version of a regulation MLB infield. Each     ##
## unit in x and y is equivalent to one foot (12 in) and all parts of the model    ##
## are drawn to scale.                                                             ##
#####################################################################################
#####################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_circle(center = (0, 0), npoints = 500, diameter = 2, start = 0, end = 2):
    """"
    This function creates a circle. It will be used to draw:
     - Home plate circle
     - Pitcher's mound
     - Base indentations
     - Edge of infield
     
     This returns a pandas dataframe, which will be plotted later
    """
    pts = np.linspace(start * np.pi, end * np.pi, npoints)
    x = center[0] + ((diameter / 2) * np.cos(pts))
    y = center[1] + ((diameter / 2) * np.sin(pts))
    
    return pd.DataFrame({'x':x, 'y':y})

a = 2
b = 2 * (((45 - (3 * np.sin(np.pi/4))) - (45 + (3 * np.cos(np.pi/4)))) - 60.5)
c = (((((45 - (3 * np.sin(np.pi/4))) - (45 + (3 * np.cos(np.pi/4)))) - 60.5) ** 2) - (95 ** 2))

# Create infield dirt
infield_dirt = pd.DataFrame({
    'x':[0, (-b + np.sqrt((b ** 2) - (4 * a * c)))/(2 * a)],
    'y':[(45 - (3 * np.sin(np.pi/4))) - (45 + (3 * np.cos(np.pi/4))),
        ((-b + np.sqrt((b ** 2) - (4 * a * c)))/(2 * a)) + ((45 - (3 * np.sin(np.pi/4))) - (45 + (3 * np.cos(np.pi/4))))]
}).append(
    create_circle(
        center = (0, 60.5), 
        diameter = 190, 
        start = np.arctan2(
            ((-b + np.sqrt((b ** 2) - (4 * a * c))) / (2 * a)) - 60.5,
            ((-b + np.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
        )/np.pi,
        end = 1 - (np.arctan2(
            ((-b + np.sqrt((b ** 2) - (4 * a * c))) / (2 * a)) - 60.5,
            ((-b + np.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
        )/np.pi)
    )
).append(
    pd.DataFrame({
        'x':[-((-b + np.sqrt((b ** 2) - (4 * a * c))) / (2 * a))],
        'y':[((-b + np.sqrt((b ** 2) - (4 * a * c))) / (2 * a)) + ((45 - (3 * np.sin(np.pi/4))) - (45 + (3 * np.cos(np.pi/4))))]
    })
).append(
    pd.DataFrame({
        'x':[0],
        'y':[(45 - (3 * np.sin(np.pi/4))) - (45 + (3 * np.cos(np.pi/4)))]
    })
)

# Create infield grass
infield_grass = pd.DataFrame({
    'x':[0, (45 * np.sqrt(2)) - 3, 0, (-45 * np.sqrt(2) + np.sqrt(2 * ((15/12) ** 2))) + 3, 0],
    'y':[3, 45 * np.sqrt(2), (np.sqrt(2 * (90 ** 2)) - .5 * np.sqrt(2 * ((15/12) ** 2))) - 3, 45 * np.sqrt(2), 3]
})

# Create dirt around bases and around pitcher's mound
home_dirt = create_circle(center = (0, 0), diameter = 26, start = 0, end = 2)

first_dirt = pd.DataFrame({
    'x':[45 * np.sqrt(2)],
    'y':[45 * np.sqrt(2)]
}).append(
    create_circle(
        center = ((45 * np.sqrt(2)) - 3, 45 * np.sqrt(2)),
        diameter = 20,
        start = 3/4,
        end = 5/4
    )
).append(
    pd.DataFrame({
        'x':[45 * np.sqrt(2)],
        'y':[45 * np.sqrt(2)]
    })
)

second_dirt = pd.DataFrame({
    'x':[0],
    'y':[((np.sqrt(2 * (90 ** 2))) - .5 * np.sqrt(2 * ((15/12) ** 2))) - 3]
}).append(
    create_circle(
        center = (0, np.sqrt(2 * (90 ** 2)) - .5 * np.sqrt(2 * ((15/12) ** 2))),
        diameter = 20,
        start = 4.9/4,
        end = 7.1/4
    )
).append(
    pd.DataFrame({
        'x':[0],
        'y':[(np.sqrt(2 * (90 ** 2)) - .5 * np.sqrt(2 * ((15/12) ** 2))) - 3]
    })
)

third_dirt = pd.DataFrame({
    'x':-1 * first_dirt['x'],
    'y':first_dirt['y']
})

mound = create_circle(center = (0, 718/12), diameter = 9, start = 0, end = 2)

# Create the bases and pitcher's plate
home_plate = pd.DataFrame({
    'x':[0, -8.5/12, -8.5/12, 8.5/12, 8.5/12, 0],
    'y':[0, np.sqrt(1 - ((8.5/12) ** 2)), np.sqrt(1 - ((8.5/12) ** 2)) + (8.5/12), np.sqrt(1 - ((8.5/12) ** 2)) + (8.5/12), np.sqrt(1 - ((8.5/12) ** 2)), 0]
})

pitchers_plate = pd.DataFrame({
    'x':[-1, -1, 1, 1, -1],
    'y':[60 + (6/12), 61, 61, 60 + (6/12), 60 + (6/12)]
})

first_base = pd.DataFrame({
    'x':[44.375 * np.sqrt(2), 45 * np.sqrt(2), 44.375 * np.sqrt(2), 45 * np.sqrt(2) - np.sqrt(2 * ((15/12) ** 2)), 44.375 * np.sqrt(2)],
    'y':[44.375 * np.sqrt(2), 45 * np.sqrt(2), (44.375 * np.sqrt(2)) + np.sqrt(2 * ((15/12) ** 2)), 45 * np.sqrt(2), 44.375 * np.sqrt(2)]
})

second_base = pd.DataFrame({
    'x':[0, .625 * np.sqrt(2), 0, -.625 * np.sqrt(2), 0],
    'y':[np.sqrt(2 * (90 ** 2)) - .5 * np.sqrt(2 * ((15/12) ** 2)), np.sqrt(2 * (90 ** 2)), np.sqrt(2 * (90 ** 2)) + .5 * np.sqrt(2 * ((15/12) ** 2)), np.sqrt(2 * (90 ** 2)), np.sqrt(2 * (90 ** 2)) - .5 * np.sqrt(2 * ((15/12) ** 2))]
})

third_base = pd.DataFrame({
    'x':-1 * first_base['x'],
    'y':first_base['y']
})

# Create batter's boxes and catcher's box
lhb_box = pd.DataFrame({
    'x':[38.5/12, 14.5/12, 14.5/12, 38.5/12, 38.5/12, 17.5/12, 17.5/12, 38.5/12, 38.5/12, 62.5/12, 62.5/12, 38.5/12, 38.5/12, 59.5/12, 59.5/12, 38.5/12, 38.5/12],
    'y':[np.sqrt(1 - (8.5/12) ** 2) - 3, np.sqrt(1 - (8.5/12) ** 2) - 3, np.sqrt(1 - (8.5/12) ** 2) + 3, np.sqrt(1 - (8.5/12) ** 2) + 3, np.sqrt(1 - (8.5/12) ** 2) + 2.75, np.sqrt(1 - (8.5/12) ** 2) + 2.75, np.sqrt(1 - (8.5/12) ** 2) - 2.75, np.sqrt(1 - (8.5/12) ** 2) - 2.75, np.sqrt(1 - (8.5/12) ** 2) - 3, np.sqrt(1 - (8.5/12) ** 2) - 3, np.sqrt(1 - (8.5/12) ** 2) + 3, np.sqrt(1 - (8.5/12) ** 2) + 3, np.sqrt(1 - (8.5/12) ** 2) + 2.75, np.sqrt(1 - (8.5/12) ** 2) + 2.75, np.sqrt(1 - (8.5/12) ** 2) - 2.75, np.sqrt(1 - (8.5/12) ** 2) - 2.75, np.sqrt(1 - (8.5/12) ** 2) - 3]
})

rhb_box = pd.DataFrame({
    'x':-1 * lhb_box['x'],
    'y':lhb_box['y']
})

catchers_box = pd.DataFrame({
    'x':[-23.5/12, -23.5/12, 23.5/12, 23.5/12, 20.5/12, 20.5/12, -20.5/12, -20.5/12, -23.5/12],
    'y':[np.sqrt(1 - (8.5/12) ** 2) - 3, -8, -8, np.sqrt(1 - (8.5/12) ** 2) - 3, np.sqrt(1 - (8.5/12) ** 2) - 3, -7.75, -7.75, np.sqrt(1 - (8.5/12) ** 2) - 3, np.sqrt(1 - (8.5/12) ** 2) - 3]
})

# Create foul lines
rf_line = pd.DataFrame({
    'x':[np.sqrt(1 - (8.5/12) ** 2) + 3, 155.5, 155.25, np.sqrt(1 - (8.5/12) ** 2) + 2.75, np.sqrt(1 - (8.5/12) ** 2) + 3],
    'y':[np.sqrt(1 - (8.5/12) ** 2) + 3, 155.5, 155.5, np.sqrt(1 - (8.5/12) ** 2) + 3, np.sqrt(1 - (8.5/12) ** 2) + 3]
})

lf_line = pd.DataFrame({
    'x':-1 * rf_line['x'],
    'y':rf_line['y']
})

# Create running lane
running_lane = pd.DataFrame({
    'x':[
        22.5 * np.sqrt(2),
        (22.5 * np.sqrt(2)) + (3 * np.cos(np.pi/4)),
        ((22.5 * np.sqrt(2)) + (3 * np.cos(np.pi/4))) + (45 * np.cos(np.pi/4)),
        (((22.5 * np.sqrt(2)) + (3 * np.cos(np.pi/4))) + (45 * np.cos(np.pi/4))) - ((3/12) * np.cos(np.pi/4)),
        ((((22.5 * np.sqrt(2)) + (3 * np.cos(np.pi/4))) + (45 * np.cos(np.pi/4))) - ((3/12) * np.cos(np.pi/4))) - (44.75 * np.cos(np.pi/4)),
        (((((22.5 * np.sqrt(2)) + (3 * np.cos(np.pi/4))) + (45 * np.cos(np.pi/4))) - ((3/12) * np.cos(np.pi/4))) - (44.75 * np.cos(np.pi/4))) - (3 * np.cos(np.pi/4))
    ],
    'y':[
        22.5 * np.sqrt(2),
        (22.5 * np.sqrt(2)) - (3 * np.sin(np.pi/4)),
        ((22.5 * np.sqrt(2)) - (3 * np.sin(np.pi/4))) + (45 * np.sin(np.pi/4)),
        (((22.5 * np.sqrt(2)) - (3 * np.sin(np.pi/4))) + (45 * np.sin(np.pi/4))) + ((3/12) * np.sin(np.pi/4)),
        ((((22.5 * np.sqrt(2)) - (3 * np.sin(np.pi/4))) + (45 * np.sin(np.pi/4))) + ((3/12) * np.sin(np.pi/4))) - (44.75 * np.cos(np.pi/4)),
        (((((22.5 * np.sqrt(2)) - (3 * np.sin(np.pi/4))) + (45 * np.sin(np.pi/4))) + ((3/12) * np.sin(np.pi/4))) - (44.75 * np.cos(np.pi/4))) + (3 * np.sin(np.pi/4))
    ]
})

#################
# Make the plot #
#################

fig, ax = plt.subplots()

ax.set_aspect('equal')
fig.set_size_inches(50, 50)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Set background field color
ax.set_facecolor('#395d33')

# Add infield dirt and grass
ax.fill(infield_dirt['x'], infield_dirt['y'], '#9b7653')
ax.fill(infield_grass['x'], infield_grass['y'], '#395d33')

# Add dirt areas around each base and pitcher's mound
ax.fill(home_dirt['x'], home_dirt['y'], '#9b7653')
ax.fill(first_dirt['x'], first_dirt['y'], '#9b7653')
ax.fill(second_dirt['x'], second_dirt['y'], '#9b7653')
ax.fill(third_dirt['x'], third_dirt['y'], '#9b7653')
ax.fill(mound['x'], mound['y'], '#9b7653')

# Add bases and pitcher's plate
ax.fill(home_plate['x'], home_plate['y'], '#ffffff')
ax.fill(pitchers_plate['x'], pitchers_plate['y'], '#ffffff')
ax.fill(first_base['x'], first_base['y'], '#ffffff')
ax.fill(second_base['x'], second_base['y'], '#ffffff')
ax.fill(third_base['x'], third_base['y'], '#ffffff')

# Add batter's boxes and catcher's box
ax.fill(lhb_box['x'], lhb_box['y'], '#ffffff')
ax.fill(rhb_box['x'], rhb_box['y'], '#ffffff')
ax.fill(catchers_box['x'], catchers_box['y'], '#ffffff')

# Add foul lines and running lane
ax.fill(rf_line['x'], rf_line['y'], '#ffffff')
ax.fill(lf_line['x'], lf_line['y'], '#ffffff')
ax.fill(running_lane['x'], running_lane['y'], '#ffffff')

plt.show()
