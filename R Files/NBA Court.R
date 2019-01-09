#####################################################################################
#####################################################################################
## This script produces a ggplot version of a regulation NBA court. Each unit      ##
## in x and y is equivalent to one foot (12 in) and all parts of the model are     ##
## drawn to scale.                                                                 ##
#####################################################################################
#####################################################################################

library(ggplot2)
library(png)
library(grid)
library(raster)
library(magick)

create_circle = function(center = c(0, 0), npoints = 500, diameter = 1, start = 0, end = 2) {
  pts = seq(start * pi, end * pi, length.out = npoints)
  data.frame(x = center[1] + ((diameter/2) * cos(pts)),
             y = center[2] + ((diameter/2) * sin(pts)))
}

draw_nba = function(){
  nba_logo = readPNG('League Logos/nba.png')
  nba_logo = rasterGrob(nba_logo, interpolate = TRUE)
  
  logo_borders = data.frame(xmin = -2, xmax = 2, ymin = 25 + (2/12), ymax = 29 + (2/12))
  
  # Create court
  court_out = data.frame(xmin = -55, xmax = 55, ymin = -30, ymax = 30)
  court_in = data.frame(xmin = -47, xmax = 47, ymin = -25, ymax = 25)
  
  # Create baseline
  baseline = data.frame(xmin = -47 - (2/12), xmax = -47, ymin = -25 - (2/12), ymax = 25 + (2/12))
  baseline = rbind(baseline, data.frame(xmin = -baseline$xmax, xmax = -baseline$xmin, ymin = baseline$ymin, ymax = baseline$ymax))
  
  # Create sideline
  sideline = data.frame(xmin = -47 - (2/12), xmax = 47 + (2/12), ymin = -25 - (2/12), ymax = -25)
  sideline = rbind(sideline, data.frame(xmin = sideline$xmax, xmax = sideline$xmin, ymin = -sideline$ymax, ymax = -sideline$ymin))
  
  
  # Create time line
  timeline = data.frame(xmin = -(1/12), xmax = (1/12), ymin = -25, ymax = 25)
  
  # Create coaches' boxes and substitution area
  coach_box = data.frame(xmin = -19, xmax = -19 + (2/12), ymin = -25, ymax = -22)
  coach_box = rbind(coach_box, data.frame(xmin = coach_box$xmin, xmax = coach_box$xmax, ymin = -coach_box$ymax, ymax = -coach_box$ymin))
  coach_box = rbind(coach_box, data.frame(xmin = -coach_box$xmin, xmax = -coach_box$xmax, ymin = coach_box$ymin, ymax = coach_box$ymax))
  
  substitution_area = data.frame(xmin = -4 - (4/12), xmax = -4 - (2/12), ymin = 25 + (2/12), ymax = 29 + (2/12))
  substitution_area = rbind(substitution_area, data.frame(xmin = -substitution_area$xmax, xmax = -substitution_area$xmin, ymin = substitution_area$ymin, ymax = substitution_area$ymax))
  
  # Create inner circle
  inner_circle = create_circle(center = c(0, 0), diameter = 4, start = 1/2, end = 3/2)
  inner_circle = rbind(inner_circle, data.frame(x = 0, y = -2 - (2/12)))
  inner_circle = rbind(inner_circle, create_circle(center = c(0, 0), diameter = 4 + (4/12), start = 3/2, end = 1/2))
  inner_circle = rbind(inner_circle, data.frame(x = 0, y = 2))
  inner_circle = rbind(inner_circle, data.frame(x = -inner_circle$x, y = inner_circle$y))
  
  # Create outer circle
  outer_circle = create_circle(center = c(0, 0), diameter = 12, start = 1/2, end = 3/2)
  outer_circle = rbind(outer_circle, data.frame(x = 0, y = -6 + (2/12)))
  outer_circle = rbind(outer_circle, create_circle(center = c(0, 0), diameter = 12 - (4/12), start = 3/2, end = 1/2))
  outer_circle = rbind(outer_circle, data.frame(x = 0, y = 6 - (2/12)))
  outer_circle = rbind(outer_circle, data.frame(x = -outer_circle$x, y = outer_circle$y))
  
  # Create free throw line
  free_throw_line = data.frame(xmin = -28 - (2/12), xmax = -28, ymin = -8, ymax = 8)
  
  # Create lane
  lane = data.frame(
    x = c(-47, -28, -28, -47, -47, -28 - (2/12), -28 - (2/12), -47, -47, -28 - (2/12), -28 - (2/12), -47, -47, -28 - (2/12), -28 - (2/12), -47, -47),
    y = c(-8, -8, 8, 8, 8 - (2/12), 8 - (2/12), 6, 6, 6 - (2/12), 6 - (2/12), -6 + (2/12), -6 + (2/12), -6, -6, -8 + (2/12), -8 + (2/12), -8)
  )
  
  lane = rbind(lane, data.frame(x = -lane$x, y = lane$y))
  
  # Create hash marks
  hash_baseline = data.frame(xmin = -47, xmax = -46.5, ymin = -11 - (2/12), ymax = -11)
  hash_baseline = rbind(hash_baseline, data.frame(xmin = hash_baseline$xmin, xmax = hash_baseline$xmax, ymin = -hash_baseline$ymax, ymax = -hash_baseline$ymin))
  hash_baseline = rbind(hash_baseline, data.frame(xmin = -hash_baseline$xmin, xmax = -hash_baseline$xmax, ymin = hash_baseline$ymax, ymax = hash_baseline$ymin))
  
  hash_lane = data.frame(xmin = -34, xmax = -34 + (2/12), ymin = -5, ymax = -4.5)
  hash_lane = rbind(hash_lane, data.frame(xmin = hash_lane$xmin, xmax = hash_lane$xmax, ymin = -hash_lane$ymax, ymax = -hash_lane$ymin))
  hash_lane = rbind(hash_lane, data.frame(xmin = -hash_lane$xmin, xmax = -hash_lane$xmax, ymin = hash_lane$ymax, ymax = hash_lane$ymin))
  
  # Blocks
  blocks = data.frame(
    xmin = c(-40, -39 - (2/12), -36, -33 + (2/12), 
             -40, -36, -33 + (2/12), -30 + (4/12)),
    xmax = c(-40 + (2/12), -39, -36 + (2/12), -33 + (4/12),
             -39, -36 + (2/12), -33 + (4/12), -30 + (6/12)),
    ymin = c(-8, -8, -8, -8, 
             -6, -6, -6, -6),
    ymax = c(-8.5, -8.5, -8.5, -8.5, 
             -6.5, -6.5, -6.5, -6.5)
  )
  
  blocks = rbind(blocks, data.frame(xmin = blocks$xmin, xmax = blocks$xmax, ymin = -blocks$ymax, ymax = -blocks$ymin))
  blocks = rbind(blocks, data.frame(xmin = -blocks$xmin, xmax = -blocks$xmax, ymin = blocks$ymax, ymax = blocks$ymin))
  
  # Create free throw circle
  free_throw_circle = create_circle(center = c(-28, 0), start = (-1/2) - ((12.29/72)/pi), end = (1/2) + ((12.29/72)/pi), diameter = 12)
  free_throw_circle = rbind(free_throw_circle, create_circle(center = c(-28, 0), start = (1/2) + ((12.29/72)/pi), end = (-1/2) - ((12.29/72)/pi), diameter = 12 - (4/12)))
  free_throw_circle = rbind(free_throw_circle, free_throw_circle[1, ])
  free_throw_circle = rbind(free_throw_circle, data.frame(x = -free_throw_circle$x, y = free_throw_circle$y))
  
  dash_1 = create_circle(center = c(-28, 0), start = (1/2) + (((12.29/72) + (15.5/72))/pi), end = (1/2) + (((12.29/72) + (31/72))/pi), diameter = 12)
  dash_1 = rbind(dash_1, create_circle(center = c(-28, 0), start = (1/2) + (((12.29/72) + (31/72))/pi), end = (1/2) + (((12.29/72) + (15.5/72))/pi), diameter = 12 - (4/12)))
  dash_1 = rbind(dash_1, dash_1[1, ])
  dash_1 = rbind(dash_1, data.frame(x = dash_1$x, y = -dash_1$y))
  
  dash_2 = create_circle(center = c(-28, 0), start = (1/2) + (((12.29/72) + (46.5/72))/pi), end = (1/2) + (((12.20/72) + (62/72))/pi), diameter = 12)
  dash_2 = rbind(dash_2, create_circle(center = c(-28, 0), start = (1/2) + (((12.20/72) + (62/72))/pi), end = (1/2) + (((12.29/72) + (46.5/72))/pi), diameter = 12 - (4/12)))
  dash_2 = rbind(dash_2, dash_2[1, ])
  dash_2 = rbind(dash_2, data.frame(x = dash_2$x, y = -dash_2$y))
  
  dash_3 = create_circle(center = c(-28, 0), start = (1/2) + (((12.29/72) + (77.5/72))/pi), end = (1/2) + (((12.20/72) + (93/72))/pi), diameter = 12)
  dash_3 = rbind(dash_3, create_circle(center = c(-28, 0), start = (1/2) + (((12.20/72) + (93/72))/pi), end = (1/2) + (((12.29/72) + (77.5/72))/pi), diameter = 12 - (4/12)))
  dash_3 = rbind(dash_3, dash_3[1, ])
  dash_3 = rbind(dash_3, data.frame(x = dash_3$x, y = -dash_3$y))
  
  # Create restricted area
  restricted_area = data.frame(x = -41.7 - (15/12), y = -4)
  restricted_area = rbind(restricted_area, data.frame(x = -41.7, y = -4))
  restricted_area = rbind(restricted_area, create_circle(center = c(-42 + (3/12), 0), start = -1/2, end = 1/2, diameter = 8))
  restricted_area = rbind(restricted_area, data.frame(x = -41.7, y = 4))
  restricted_area = rbind(restricted_area, data.frame(x = -41.7 - (15/12), y = 4))
  restricted_area = rbind(restricted_area, data.frame(x = -41.7 - (15/12), y = 4 - (2/12)))
  restricted_area = rbind(restricted_area, data.frame(x = -41.7, y = 4 - (2/12)))
  restricted_area = rbind(restricted_area, create_circle(center = c(-42 + (3/12), 0), start = 1/2, end = -1/2, diameter = 8 - (4/12)))
  restricted_area = rbind(restricted_area, data.frame(x = -41.7, y = -4 + (2/12)))
  restricted_area = rbind(restricted_area, data.frame(x = -41.7 - (15/12), y = -4 + (2/12)))
  restricted_area = rbind(restricted_area, data.frame(x = -41.7 - (15/12), y = -4))
  restricted_area = rbind(restricted_area, data.frame(x = -restricted_area$x, y = restricted_area$y))
  
  # Create three-point line
  arc_3_out = create_circle(center = c(-41.75, 0), diameter = 47.5, start = 1/2, end = -1/2)
  arc_3_out = arc_3_out[arc_3_out$y >= -22 & arc_3_out$y <= 22, ]
  
  arc_3_in = create_circle(center = c(-41.75, 0), diameter = 47.5 - (4/12), start = -1/2, end = 1/2)
  arc_3_in = arc_3_in[arc_3_in$y >= -22 + (2/12) & arc_3_in$y <= 22 - (2/12), ]
  
  three_pt_line = data.frame(x = -47, y = 22)
  three_pt_line = rbind(three_pt_line, arc_3_out)
  three_pt_line = rbind(three_pt_line, data.frame(x = -47, y = -22))
  three_pt_line = rbind(three_pt_line, data.frame(x = -47, y = -22 + (2/12)))
  three_pt_line = rbind(three_pt_line, arc_3_in)
  three_pt_line = rbind(three_pt_line, data.frame(x = -47, y = 22 - (2/12)))
  three_pt_line = rbind(three_pt_line, data.frame(x = -47, y = 22))
  three_pt_line = rbind(three_pt_line, data.frame(x = -three_pt_line$x, y = three_pt_line$y))
  
  # Create hoop
  backboard = data.frame(xmin = -43 - (2/12), xmax = -43, ymin = -3, ymax = 3)
  backboard = rbind(backboard, data.frame(xmin = -backboard$xmax, xmax = -backboard$xmin, ymin = backboard$ymin, ymax = backboard$ymax))
  
  rim_connector = data.frame(xmin = -43, xmax = -42.3, ymin = -(4/12), ymax = (4/12))
  rim_connector = rbind(rim_connector, data.frame(xmin = -rim_connector$xmax, xmax = -rim_connector$xmin, ymin = rim_connector$ymin, ymax = rim_connector$ymax))
  
  rim = create_circle(center = c(-41.75, 0), diameter = 1.5 + (4/12))
  rim = rbind(rim, data.frame(x = -rim$x, y = rim$y))
  
  net = create_circle(center = c(-41.75, 0), diameter = 1.5)
  net = rbind(net, data.frame(x = -net$x, y = net$y))
  
  ggplot() +
    theme_void() +
    theme(
      panel.border = element_blank(),
      panel.background = element_blank(),
      axis.title = element_blank(),
      axis.text = element_blank(),
      axis.ticks = element_blank()
    ) +
    coord_fixed() +
    geom_rect(data = court_out, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
    geom_rect(data = court_in, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#d2ab6f') +
    geom_polygon(data = outer_circle, aes(x, y), fill = '#000000') +
    geom_polygon(data = inner_circle, aes(x, y), fill = '#000000') +
    geom_rect(data = timeline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
    geom_rect(data = coach_box, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = substitution_area, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_polygon(data = three_pt_line, aes(x, y), fill = '#000000') +
    geom_polygon(data = free_throw_circle, aes(x, y), fill = '#000000') +
    geom_polygon(data = dash_1, aes(x, y), fill = '#000000') +
    geom_polygon(data = dash_2, aes(x, y), fill = '#000000') +
    geom_polygon(data = dash_3, aes(x, y), fill = '#000000') +
    geom_polygon(data = dash_1, aes(-x, y), fill = '#000000') +
    geom_polygon(data = dash_2, aes(-x, y), fill = '#000000') +
    geom_polygon(data = dash_3, aes(-x, y), fill = '#000000') +
    geom_polygon(data = restricted_area, aes(x, y), fill = '#000000') +
    geom_polygon(data = lane, aes(x, y), fill = '#000000') +
    geom_rect(data = hash_baseline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = hash_lane, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
    geom_rect(data = blocks, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
    geom_rect(data = baseline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = sideline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = backboard, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
    geom_rect(data = rim_connector, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#e04e39') +
    geom_polygon(data = rim, aes(x, y), fill = '#e04e39') +
    geom_polygon(data = net, aes(x, y), fill = '#ffffff') +
    annotation_custom(nba_logo, xmin = logo_borders$xmin, xmax = logo_borders$xmax, ymin = logo_borders$ymin, ymax = logo_borders$ymax)
}
