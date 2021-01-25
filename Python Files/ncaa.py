"""
@author: Ross Drucker
"""
import math
import requests
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

import playing_surface_helper as helper
import coordinate_transforms as transform

def get_center_circle(full_court = True, rotate = False, rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the center circle as
    specified in Rule 1, Section 4, Article 1 of the NCAA rule book

    Returns
    -------
    center_circle: a pandas dataframe containing the points that comprise the
        center circle of the court
    """
    # Draw the right outer semicircle, then move in 2" per the NCAA's required
    # line thickness, and draw inner semicircle. Doing it this way alleviates
    # future fill issues.
    center_circle = helper.create_circle(
        d = 12,
        start = 1/2,
        end = 3/2
    ).append(
        pd.DataFrame({
            'x': [0],
            'y': [6 - (2/12)]
        })
    ).append(
        helper.create_circle(
            d = 12 - (4/12),
            start = 3/2,
            end = 1/2
        )
    ).append(
        pd.DataFrame({
            'x': [0],
            'y': [-6]
        })
    )
    
    if full_court:
        # Reflect the x coordinates over the y axis    
        center_circle = center_circle.append(
            transform.reflect(center_circle, over_y = True)
        )
        
    # Rotate the coordinates if necessary
    if rotate:
        center_circle = transform.rotate(
            center_circle,
            rotation_dir
        )
            
    return center_circle

def get_division_line(full_court = True, rotate = False, rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the bounding box of
    the division line as specified in Rule 1, Section 5, Article 1 of the NCAA
    rule book

    Returns
    -------
    division_line: a pandas dataframe of the interior boundaries of the court
    """
    # The line's center should be 47' from the interior side of the baselines,
    # and must be 2" thick
    division_line = pd.DataFrame({
        'x': [
            -1/12,
            0,
            0,
            -1/12,
            -1/12
        ],
        
        'y': [
            25,
            25,
            -25,
            -25,
            25
        ]
    })
    if full_court:
        # Reflect the x coordinates over the y axis
        division_line = division_line.append(
            transform.reflect(division_line, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        division_line = transform.rotate(
            division_line,
            rotation_dir
        )
    
    return division_line

def get_endlines_sidelines(full_court = True, rotate = False,
                           rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the bounding box of the
    end lines and sidelines as specified in Rule 1, Section 3, Article 2 of
    the NCAA rule book

    Returns
    -------
    endline_sideline: a pandas dataframe of the end lines and side lines
    """
    endline_sideline = pd.DataFrame({
        'x': [
            0,
            -47,
            -47,
            0,
            0,
            -47 - (2/12),
            -47 - (2/12),
            0,
            0
            
        ],
        
        'y': [
            -25,
            -25,
            25,
            25,
            25 + (2/12),
            25 + (2/12),
            -25 - (2/12),
            -25 - (2/12),
            -25
        ]
    })
    
    if full_court:
        # Reflect the x coordinates over the y axis
        endline_sideline = endline_sideline.append(
            transform.reflect(endline_sideline, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        endline_sideline = transform.rotate(
            endline_sideline,
            rotation_dir
        )
    
    return endline_sideline
    
    
def get_coaching_boxes(full_court = True, rotate = False,
                       rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the bounding box of the
    coaching boxes as specified in Rule 1, Section 9, Articles 1 and 2 of the
    NCAA rule book

    Returns
    -------
    coaching_boxes: a pandas dataframe of the sidelines
    """
    # The coaching boxes are 38' from the interior of the baseline on each
    # side of the court, and extend 2' out of bounds from the exterior of the
    # sideline
    coaching_box = pd.DataFrame({
        'x': [
            -9 - (2/12),
            -9 - (2/12),
            -9,
            -9,
            -9 - (2/12)
        ],
        
        'y': [
            25,
            27,
            27,
            25,
            25
        ]
    })
    
    if full_court:
        # Reflect the x coordinates over the y axis
        coaching_box = coaching_box.append(
            transform.reflect(coaching_box, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        coaching_box = transform.rotate(
            coaching_box,
            rotation_dir
        )
    
    return coaching_box

def get_bench_areas(full_court = True, rotate = False, rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the team bench areas
    as specified on the court diagram in the NCAA rule book

    Returns
    -------
    bench_areas: a pandas dataframe of the team bench areas
    """
    # The bench area is 28 feet from the interior of the endline, is 2" wide,
    # and extends 3' on each side of the sideline
    bench_area = pd.DataFrame({
        'x': [
            -19 - (2/12), -19 - (2/12), -19, -19, -19 - (2/12),
        ],
        
        'y': [22, 28, 28, 22, 22]
    })
    
    if full_court:
        # Reflect the x coordinates over the y axis
        bench_area = bench_area.append(
            transform.reflect(bench_area, over_y = True)
        )
    # Rotate the coordinates if necessary
    if rotate:
        bench_area = transform.rotate(
            bench_area,
            rotation_dir
        )
    
    return bench_area

def get_free_throw_lanes(full_court = True, rotate = False,
                         rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the bounding box of the
    free throw lane as specified in Rule 1, Section 6, Articles 1, 2, 3, and 4
    of the NCAA rule book

    Returns
    -------
    free_throw_lanes: a pandas dataframe of the free throw lanes
    painted_areas: a pandas dataframe of the painted areas
    """
    # The free throw lane goes from the endline inwards a distance of 18' 10"
    # (interior) and 19' (exterior) with a width of 6'
    
    # The first set of blocks are 7' from the interior of the baseline, and
    # measure 1' in width
    
    # The second set of blocks are 3' from the first block, and
    # measure 2" in width
    
    # The third set of blocks are 3' from the second block, and
    # measure 2" in width
    
    # The fourth set of blocks are 3' from the third block, and
    # measure 2" in width
    free_throw_lane = pd.DataFrame({
        'x': [
            # Start
            -47,
            
            # First block lower
            -40,
            -40,
            -39,
            -39,
            
            # Second block lower
            -36,
            -36,
            -36 + (2/12),
            -36 + (2/12),
            
            # Third block lower
            -33 + (2/12),
            -33 + (2/12),
            -33 + (4/12),
            -33 + (4/12),
            
            # Fourth block lower
            -30 + (4/12),
            -30 + (4/12),
            -30 + (6/12),
            -30 + (6/12),
            
            # End
            -28,
            
            # Cross
            -28,
            
            # Fourth block upper
            -30 + (6/12),
            -30 + (6/12),
            -30 + (4/12),
            -30 + (4/12),
            
            # Third block upper
            -33 + (2/12),
            -33 + (2/12),
            -33 + (4/12),
            -33 + (4/12),
            
            # Second block upper
            -36,
            -36,
            -36 + (2/12),
            -36 + (2/12),
            
            # First block upper
            -40,
            -40,
            -39,
            -39,
            
            # End of exterior
            -47,
            
            # Interior
            -47, -28 - (2/12), -28 - (2/12), -47, -47, -47
        ],
        
        'y': [
            -6,
            
            # First block lower
            -6,
            -6 - (8/12),
            -6 - (8/12),
            -6,
            
            # Second block lower
            -6,
            -6 - (8/12),
            -6 - (8/12),
            -6,
            
            # Third block lower
            -6,
            -6 - (8/12),
            -6 - (8/12),
            -6,
            
            # Fourth block lower
            -6,
            -6 - (8/12),
            -6 - (8/12),
            -6,
            
            # End
            -6,
            
            # Cross
            6,
            
            # Fourth block upper
            6,
            6 + (8/12),
            6 + (8/12),
            6,
            
            # Third block upper
            6,
            6 + (8/12),
            6 + (8/12),
            6,
            
            # Second block upper
            6,
            6 + (8/12),
            6 + (8/12),
            6,
            
             # First block upper
            6,
            6 + (8/12),
            6 + (8/12),
            6,
            
            # End of exterior
            6,
            
            # Interior
            6 - (2/12), 6 - (2/12), -6 + (2/12), -6 + (2/12), 6, -6
        ]
    })
    
    if full_court:
        # Reflect the x coordinates over the y axis
        free_throw_lane = free_throw_lane.append(
            transform.reflect(free_throw_lane, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        free_throw_lane = transform.rotate(
            free_throw_lane,
            rotation_dir
        )
    
    return free_throw_lane

def get_painted_areas(full_court = True, rotate = False, rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the bounding box of the
    free throw lane as specified in Rule 1, Section 6, Articles 1, 2, 3, and 4
    of the NCAA rule book
    
    Returns
    -------
    painted_areas: a pandas dataframe of the painted areas
    """
    # The interior of the free throw lane is known as the painted area, and
    # can be a different color than the markings and court. These coordinates
    # can be used to color them on the plot
    painted_area = pd.DataFrame({
        'x': [
            -47,
            -47,
            -28 - (2/12),
            -28 - (2/12),
            -47
        ],
        
        'y': [
            -6 + (2/12),
            6 - (2/12),
            6 - (2/12),
            -6 + (2/12),
            -6 + (2/12)
        ]
    })
    
    if full_court:
        # Reflect the x coordinates over the y axis
        painted_area = painted_area.append(
            transform.reflect(painted_area, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        painted_area = transform.rotate(
            painted_area,
            rotation_dir
        )
    
    return painted_area
    
def get_restricted_area_arcs(full_court = True, rotate = False,
                             rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the restricted-area
    arcs as specified in Rule 1, Section 8 of the NCAA rule book

    Returns
    -------
    restricted_area_arcs: a pandas dataframe of the restricted-area arcs
    """
    # The restricted area arc is an arc of radius 4' from the center of the
    # basket, and extending in a straight line to the front face of the
    # backboard, and having thickness of 2"
    restricted_area_arc = pd.DataFrame({
        'x': [-43],
        'y': [-4 - (2/12)]
    }).append(
        helper.create_circle(
            center = (-41.75, 0),
            d = 8 + (4/12),
            start = -1/2,
            end = 1/2
        )
    ).append(
        pd.DataFrame({
            'x': [-43, -43],
            'y': [4 + (2/12), 4]
        })
    ).append(
        helper.create_circle(
            center = (-41.75, 0),
            d = 8,
            start = 1/2,
            end = -1/2
        )
    ).append(
        pd.DataFrame({
            'x': [-43, -43],
            'y': [-4, -4 - (2/12)]
        })
    )
    
    if full_court:
        # Reflect the x coordinates over the y axis
        restricted_area_arc = restricted_area_arc.append(
            transform.reflect(restricted_area_arc, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        restricted_area_arc = transform.rotate(rotation_dir = rotation_dir, df = restricted_area_arc)
        
    return restricted_area_arc
    
def get_m_three_pt_lines(full_court = True, rotate = False,
                         rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the three-point line
    as specified in Rule 1, Section 7 of the NCAA rule book. These points are
    the men's three-point line after being moved back prior to the 2019-2020
    season

    Returns
    -------
    m_three_pt_lines: a pandas dataframe of the three-point line
    """
    # First, a bit of math is needed to determine the starting and ending
    # angles of the three-point arc, relative to 0 radians. Since in the end,
    # the angle is what matters, the units of measure do not. Inches are easier
    # to use for this calculation. The angle begins 9' 10 3/8" from the
    # interior edge of the endline
    start_x = (9 * 12) + 10 + (3/8)
    
    # However, the rule book describes the arc as having a radius of 22' 1.75"
    # from the center of the basket. The basket's center is 63" away from the
    # interior of the endline, so this must be subtracted from our starting x
    # position to get the starting x position *relative to the center of the
    # basket*
    start_x -= 63
    radius_outer = (22 * 12) + 1.75
    
    # From here, the calculation is relatively straightforward. To determine
    # the angle, the inverse cosine is needed. It will be multiplied by pi
    # so that it can be passed to the create_circle() function
    start_angle_outer = math.acos(start_x / radius_outer) / np.pi
    end_angle_outer = -start_angle_outer
    
    # The same method can be used for the inner angles, however, since the
    # inner radius will be traced from bottom to top, the angle must be
    # negative to start
    radius_inner = (22 * 12) + 1.75 - 2
    start_angle_inner = -math.acos(start_x / radius_inner) / np.pi
    end_angle_inner = -start_angle_inner
    
    # According to the rulebook, the three-point line is 21' 7 7/8" in the
    # corners
    m_three_pt_line = pd.DataFrame({
        'x': [-47],
        'y': [21 + ((7 + (7/8))/12)]
    }).append(
        helper.create_circle(
            center = (-41.75, 0),
            d = 2 * (((22 * 12) + 1.75)/12),
            start = start_angle_outer,
            end = end_angle_outer
        )
    ).append(
        pd.DataFrame({
            'x': [
                -47,
                -47,
                -47 + (((9 * 12) + 10 + (3/8))/12)
            ],
            
            'y': [
                -21 - ((7 + (7/8))/12),
                -21 - ((7 + (7/8))/12) + (2/12),
                -21 - ((7 + (7/8))/12) + (2/12)
            ]
        })
    ).append(
        helper.create_circle(
            center = (-41.75, 0),
            d = 2 * ((((22 * 12) + 1.75)/12) - (2/12)),
            start = start_angle_inner,
            end = end_angle_inner
        )
    ).append(
        pd.DataFrame({
            'x': [
                -47 + (((9 * 12) + 10 + (3/8))/12),
                -47,
                -47
            ],
            
            'y': [
                21 + ((7 + (7/8))/12) - (2/12),
                21 + ((7 + (7/8))/12) - (2/12),
                21 + ((7 + (7/8))/12)
            ]
        })
    )
    
    if full_court:
        # Reflec the x coordinates over the y axis
        m_three_pt_line = m_three_pt_line.append(
            transform.reflect(m_three_pt_line, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        m_three_pt_line = transform.rotate(rotation_dir = rotation_dir, df = m_three_pt_line)
    
    return m_three_pt_line

def get_w_three_pt_lines(full_court = True, rotate = False,
                         rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the three-point line
    as specified in Rule 1, Section 7 of the NCAA rule book. These points are
    the women's three-point line, and also where the men's three-point line was
    prior to the 2019-2020 season

    Returns
    -------
    w_three_pt_lines: a pandas dataframe of the three-point line
    """
    # This can be computed similarly to how the men's line was computed
    w_three_pt_line = pd.DataFrame({
        'x':[-47],
        'y':[-20.75]
    }).append(
        helper.create_circle(
            center = (-41.75, 0),
            d = 41.5,
            start = -1/2,
            end = 1/2
        )
    ).append(
        pd.DataFrame({
            'x':[-47, -47],
            'y':[20.75, 20.75 - (2/12)]
        })
    ).append(
        helper.create_circle(
            center = (-41.75, 0),
            d = 41.5 - (4/12),
            start = 1/2,
            end = -1/2
        )
    ).append(
        pd.DataFrame({
            'x':[-47, -47],
            'y':[-20.75 + (2/12), -20.75]
        })
    )
    
    if full_court:
        # Reflect the x coordinates over the y axis
        w_three_pt_line = w_three_pt_line.append(
            transform.reflect(w_three_pt_line, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        w_three_pt_line = transform.rotate(
            w_three_pt_line,
            rotation_dir
        )
    
    
    return w_three_pt_line

def get_free_throw_circles(full_court = True, rotate = False,
                           rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the free-throw circles
    as specified on the court diagram in the NCAA rule book

    Returns
    -------
    free_throw_circles: a pandas dataframe of the free-throw circle
    """
    # The free-throw circle is 6' in diameter from the center of the free-throw
    # line (exterior)
    free_throw_circle = helper.create_circle(
        center = (-28, 0),
        start = -1/2,
        end = 1/2,
        d = 12
    ).append(
        pd.DataFrame({
            'x':[-28],
            'y':[6]
        })
    ).append(
        helper.create_circle(
            center = (-28, 0),
            start = 1/2,
            end = -1/2,
            d = 12 - (4/12)
        )
    ).append(
        pd.DataFrame({
            'x':[-28],
            'y':[-6]
        })
    )
    
    if full_court:
        # Reflect x coordinates over y axis
        free_throw_circle = free_throw_circle.append(
            transform.reflect(free_throw_circle, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        free_throw_circle = transform.rotate(
            free_throw_circle,
            rotation_dir
        )
    
    return free_throw_circle

def get_backboards(full_court = True, rotate = False, rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the backboard as
    specified in Rule 1, Section 10, Article 2 of the NCAA rule book

    Returns
    -------
    backboard: a pandas dataframe of the backboard
    """
    # Per the rule book, the backboard must by 6' wide. The height of the
    # backboard is irrelevant in this graphic, as this is a bird's eye view
    # over the court
    backboard = pd.DataFrame({
        'x':[-43 - (4/12), -43, -43, -43 - (4/12), -43 - (4/12)],
        'y':[-3, -3, 3, 3, -3]
    })
    
    if full_court:
        # Reflect x coordinates over y axis
        backboard = backboard.append(
            transform.reflect(backboard, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        backboard = transform.rotate(
            backboard,
            rotation_dir
        )
        
    return backboard

def get_goals(full_court = True, rotate = False, rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the goals as specified
    in Rule 1, Sections 14 and 15 of the NCAA rule book

    Returns
    -------
    goals: a pandas dataframe of the goals
    """
    # Get the starting angle of the ring. The connector has a width of 5", so
    # 2.5" are on either side. The ring has a radius of 9", so the arcsine of
    # these measurements should give the angle at which point they connect
    start_angle = np.pi - math.asin(2.5/9)
    
    # The ending angle of the ring would be the negative of the starting angle
    end_angle = -start_angle
    
    # Define the coordinates for the goal
    goal = pd.DataFrame({
        'x': [
            -43,
            -41.75 - ((9/12) * math.cos(start_angle))
        ],
        
        'y': [
            2.5/12,
            2.5/12
        ]
    }).append(
        helper.create_circle(
            center = (-41.75, 0),
            start = start_angle,
            end = end_angle,
            d = 1.5 + (4/12)
        )
    ).append(
        pd.DataFrame({
            'x': [
                -41.75 - ((9/12) * math.cos(start_angle)),
                -43,
                -43
            ],
            
            'y': [
                -2.5/12,
                -2.5/12,
                2.5/12
            ]
        })
    )
        
    if full_court:
        # Reflect x coordinates over y axis
        goal = goal.append(
            transform.reflect(goal, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        goal = transform.rotate(
            goal,
            rotation_dir
        )
        
    return goal

def get_nets(full_court = True, rotate = False, rotation_dir = 'ccw'):
    """
    Generate the dataframe for the points that comprise the rings as specified
    in Rule 1, Section 14, Article 2 of the NCAA rule book

    Returns
    -------
    nets: a pandas dataframe of the nets
    """
    # The ring's center is 15" from the backboard, and 63" from the baseline,
    # which means it is centered at (+/-41.75, 0). The ring has an interior
    # diameter of 18", which is where the net is visible from above
    net = helper.create_circle(
        center = (-41.75, 0),
        d = 1.5
    )
    
    if full_court:
        # Reflect x coordinates over y axis
        net = net.append(
            transform.reflect(net, over_y = True)
        )
    
    # Rotate the coordinates if necessary
    if rotate:
        net = transform.rotate(
            net,
            rotation_dir
        )
    
    return net
    
def draw_court(home = 'illinois', full_court = True, rotate = False,
               rotation_dir = 'ccw'):
    logo_link = ('https://a.espncdn.com/combiner/i?img=/i/teamlogos/'
                 'ncaa/500/356.png')
    
    if full_court:
        im = Image.open(requests.get(logo_link, stream = True).raw)
    
    court_color = '#d2ab6f'
    paint_color = '#e04e39'
    lane_line_color = '#ffffff'
    if home == 'illinois':
        home_line_color = '#13294b'
    
    # Get the dataframes required to plot
    features = {
        'center_circle': get_center_circle(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'division_line': get_division_line(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'endlines_sidelines': get_endlines_sidelines(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'coaching_boxes': get_coaching_boxes(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'bench_areas': get_bench_areas(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'free_throw_lanes': get_free_throw_lanes(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'painted_areas': get_painted_areas(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'restricted_arcs': get_restricted_area_arcs(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'm_three_pt_lines': get_m_three_pt_lines(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'w_three_pt_lines': get_w_three_pt_lines(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'free_throw_circles': get_free_throw_circles(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'backboards': get_backboards(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'goals': get_goals(
            full_court,
            rotate,
            rotation_dir
        ),
        
        'nets': get_nets(
            full_court,
            rotate,
            rotation_dir
        )
    }
    
    if rotate and full_court:
        im = im.rotate(90)
    
    # Create the figure
    fig, ax = plt.subplots()
    
    # Set the figure so that the aspect ratio is 1:1 (no skew to graphic)
    ax.set_aspect('equal')
    
    # Make the plot big
    fig.set_size_inches(50, 50)
    
    # Hide the axis lines
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    
    # Add court coloring
    ax.set_facecolor(court_color)
    
    # Add team logo
    if full_court:
        ax.imshow(im, extent = [-12, 12, -12, 12], zorder = 1)
    
    # Per the NCAA rule book, courts should be drawn from the center outwards
    ax.fill(
        features['center_circle']['x'],
        features['center_circle']['y'],
        home_line_color
    )
    
    # Add the division line
    ax.fill(
        features['division_line']['x'],
        features['division_line']['y'],
        home_line_color
    )
    
    # Add the endlines and sidelines
    ax.fill(
        features['endlines_sidelines']['x'],
        features['endlines_sidelines']['y'],
        home_line_color
    )
        
    # Add the coaching boxes
    ax.fill(
        features['coaching_boxes']['x'],
        features['coaching_boxes']['y'],
        home_line_color
    )
    
    # Add bench areas
    ax.fill(
        features['bench_areas']['x'],
        features['bench_areas']['y'],
        home_line_color
    )
    
    # Add the free throw lanes
    ax.fill(
        features['free_throw_lanes']['x'],
        features['free_throw_lanes']['y'],
        lane_line_color
    )
    
    # Paint the painted areas
    ax.fill(
        features['painted_areas']['x'],
        features['painted_areas']['y'],
        paint_color
    )
    
    # Add restricted-area arcs
    ax.fill(
        features['restricted_arcs']['x'],
        features['restricted_arcs']['y'],
        home_line_color
    )
    
    # Add the men's three-point lines
    ax.fill(
        features['m_three_pt_lines']['x'],
        features['m_three_pt_lines']['y'],
        home_line_color
    )
    
    # Add the women's three-point lines
    ax.fill(
        features['w_three_pt_lines']['x'],
        features['w_three_pt_lines']['y'],
        lane_line_color
    )
    
    # Add the free-throw circles
    ax.fill(
        features['free_throw_circles']['x'],
        features['free_throw_circles']['y'],
        lane_line_color
    )
    
    # Add the backboards
    ax.fill(
        features['backboards']['x'],
        features['backboards']['y'],
        '#000000'
    )
    
    # Add the goals
    ax.fill(
        features['goals']['x'],
        features['goals']['y'],
        '#000000'
    )
    
    # Add the nets
    ax.fill(
        features['nets']['x'],
        features['nets']['y'],
        '#ffffff'
    )
    
    plt.show()
    
    return None

if __name__ == '__main__':
    draw_court(full_court = True, rotate = False, rotation_dir = 'ccw')
    draw_court(full_court = True, rotate = False, rotation_dir = 'cw')
    draw_court(full_court = True, rotate = True, rotation_dir = 'ccw')
    draw_court(full_court = True, rotate = True, rotation_dir = 'cw')
    draw_court(full_court = False, rotate = False, rotation_dir = 'ccw')
    draw_court(full_court = False, rotate = False, rotation_dir = 'cw')
    draw_court(full_court = False, rotate = True, rotation_dir = 'ccw')
    draw_court(full_court = False, rotate = True, rotation_dir = 'cw')