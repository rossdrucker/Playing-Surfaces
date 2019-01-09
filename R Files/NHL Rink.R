#####################################################################################
#####################################################################################
## This script produces a ggplot version of a regulation NHL ice rink. Each        ##
## unit in x and y is equivalent to one foot (12 in) and all parts of the model    ##
## are drawn to scale.                                                             ##
#####################################################################################
#####################################################################################

create_circle = function(center = c(0, 0), npoints = 500, diameter = 1, start = 0, end = 2, color = '#c8012e', fill = NA){
  pts = seq(start * pi, end * pi, length.out = npoints)
  data.frame(x = center[1] + ((diameter/2) * cos(pts)),
             y = center[2] + ((diameter/2) * sin(pts)))
}

make_faceoff_detail = function(center){
  data.frame(
    xmin = c(center[1] - 2, center[1] - 2, center[1] + 2, center[1] + 2, center[1] - 2, center[1] - 2, center[1] + 2, center[1] + 2, center[1] - ((5 + (9/12)) / 2), center[1] + ((5 + (9/12)) / 2), center[1] - ((5 + (9/12)) / 2), center[1] + ((5 + (9/12)) / 2)),
    xmax = c(center[1] - 6, center[1] - 6, center[1] + 6, center[1] + 6, center[1] - (2 + (2/12) ), center[1] - (2 + (2/12) ), center[1] + (2 + (2/12) ), center[1] + (2 + (2/12)), center[1] - ((5 + (7/12)) / 2), center[1] + ((5 + (7/12)) / 2), center[1] - ((5 + (7/12)) / 2), center[1] + ((5 + (7/12)) / 2)),
    ymin = c(center[2] - (.75 + (2/12)), center[2] + .75, center[2] - (.75 + (2/12)), center[2] + .75, center[2] - .75, center[2] + .75, center[2] - .75, center[2] + .75, center[2] - (15 - (2/12)), center[2] - (15 - (2/12)), center[2] + (15 - (2/12)), center[2] + (15 - (2/12))),
    ymax = c(center[2] - .75, center[2] + (.75 + (2/12)), center[2] - .75, center[2] + (.75 + (2/12)), center[2] - 3.75, center[2] + 3.75, center[2] - 3.75, center[2] + 3.75, center[2] - 17, center[2] - 17, center[2] + 17, center[2] + 17)
  )
}

make_faceoff_dot = function(spot){
  center = c(0, 0)
  
  dot = create_circle(center = center, diameter = 2, start = -1/2, end = 1/2)
  dot = rbind(dot, data.frame(x = 0, y = 1 - (4/12)))
  dot = rbind(dot, create_circle(center = center, diameter = 2 - (4/12), start = 1/2, end = -1/2))
  dot = rbind(dot, data.frame(x = 0, y = -1))
  dot = rbind(dot, data.frame(x = -dot$x, y = dot$y))
  
  dot_fill = create_circle(center = center, diameter = 2 - (3.99/12), start = acos(7/10)/pi, end = .5 + (acos(7/10)/pi))
  dot_fill = rbind(dot_fill, data.frame(x = rev(dot_fill$x), y = -rev(dot_fill$y)))
  
  dot$x = dot$x + spot[1]
  dot$y = dot$y + spot[2]
  
  dot_fill$x = dot_fill$x + spot[1]
  dot_fill$y = dot_fill$y + spot[2]
  
  return(list(dot = dot, dot_fill = dot_fill))
}

blocked_center_line = function(center){
  data.frame(
    xmin = -3/12,
    xmax = 3/12,
    ymin = center - 5/12,
    ymax = center + 5/12
  )
}

library(ggplot2)
library(png)
library(grid)
library(raster)
library(magick)

draw_nhl = function(){
  nhl_logo = readPNG('League Logos/nhl.png')
  nhl_logo = rasterGrob(nhl_logo, interpolate = TRUE)
  
  logo_borders = data.frame(
    xmin = sqrt(225 - (15/sqrt(2)) ^ 2) + 2,
    xmax = sqrt(225 - (15/sqrt(2)) ^ 2) + 2,
    ymin = sqrt(225 - (15/sqrt(2)) ^ 2) + 2,
    ymax = sqrt(225 - (15/sqrt(2)) ^ 2) + 2
  )
  
  boards = rbind(
    data.frame(x = 0, y = 42.5),
    data.frame(x = 72, y = 42.5),
    create_circle(center = c(72, 14.5), diameter = 56, start = 1/2, end = 0),
    create_circle(center = c(72, -14.5), diameter = 56, start = 0, end = -1/2),
    data.frame(x = 72, y = -42.5),
    data.frame(x = 0, y = -42.5),
    data.frame(x = 0, y = -42.5 - (2/12)),
    data.frame(x = 72, y = -42.5 - (2/12)),
    create_circle(center = c(72, -14.5), diameter = 56 + (4/12), start = -1/2, end = 0),
    create_circle(center = c(72, 14.5), diameter = 56 + (4/12), start = 0, end = 1/2),
    data.frame(x = 72, y = 42.5 + (2/12)),
    data.frame(x = 0, y = 42.5 + (2/12)),
    data.frame(x = 0, y = 42.5)
  )
  
  boards = rbind(boards, data.frame(x = -boards$x, y = boards$y))
  
  # Create center circle
  center_circle = create_circle(center = c(0, 0), diameter = 30, start = -1/2, end = 1/2)
  center_circle = rbind(center_circle, data.frame(x = 0, y = 15 - (2/12)))
  center_circle = rbind(center_circle, create_circle(center = c(0, 0), diameter = 30 - (4/12), start = 1/2, end = -1/2))
  center_circle = rbind(center_circle, data.frame(x = -center_circle$x, y = center_circle$y))
  
  # Create faceoff circles
  faceoff_circles_l = create_circle(center = c(0, 0), diameter = 30, start = -1/2, end = 1/2)
  faceoff_circles_l = rbind(faceoff_circles_l, data.frame(x = 0, y = 7 - (2/12)))
  faceoff_circles_l = rbind(faceoff_circles_l, create_circle(center = c(0, 0), diameter = 30 - (4/12), start = 1/2, end = -1/2))
  faceoff_circles_l = rbind(faceoff_circles_l, data.frame(x = 0, y = -7))
  faceoff_circles_l = rbind(faceoff_circles_l, data.frame(x = -faceoff_circles_l$x, y = faceoff_circles_l$y))
  
  faceoff_circles_l$x = faceoff_circles_l$x - 69
  faceoff_circles_l$y = faceoff_circles_l$y - 22
  
  faceoff_circles_l = rbind(faceoff_circles_l, data.frame(x = faceoff_circles_l$x, y = -faceoff_circles_l$y))
  faceoff_circles_r = data.frame(x = -faceoff_circles_l$x, y = faceoff_circles_l$y)
  
  # Make faceoff spots
  center_dot = create_circle(center = c(0, 0), diameter = 1)
  
  l_l_dot = make_faceoff_dot(c(-69, -22))$dot
  l_l_dot_fill = make_faceoff_dot(c(-69, -22))$dot_fill
  
  h_l_dot = make_faceoff_dot(c(-69, 22))$dot
  h_l_dot_fill = make_faceoff_dot(c(-69, 22))$dot_fill
  
  l_nz_l_dot = make_faceoff_dot(c(-20, -22))$dot
  l_nz_l_dot_fill = make_faceoff_dot(c(-20, -22))$dot_fill
  
  h_nz_l_dot = make_faceoff_dot(c(-20, 22))$dot
  h_nz_l_dot_fill = make_faceoff_dot(c(-20, 22))$dot_fill
  
  l_nz_r_dot = make_faceoff_dot(c(20, -22))$dot
  l_nz_r_dot_fill = make_faceoff_dot(c(20, -22))$dot_fill
  
  h_nz_r_dot = make_faceoff_dot(c(20, 22))$dot
  h_nz_r_dot_fill = make_faceoff_dot(c(20, 22))$dot_fill
  
  l_r_dot = make_faceoff_dot(c(69, -22))$dot
  l_r_dot_fill = make_faceoff_dot(c(69, -22))$dot_fill
  
  h_r_dot = make_faceoff_dot(c(69, 22))$dot
  h_r_dot_fill = make_faceoff_dot(c(69, 22))$dot_fill
  
  # Make faceoff details
  faceoff_details = rbind(
    make_faceoff_detail(center = c(-69, -22)),
    make_faceoff_detail(center = c(-69, 22)),
    make_faceoff_detail(center = c(69, -22)),
    make_faceoff_detail(center = c(69, 22))
  )
  
  # Create red line
  red_line = data.frame(xmin = -.5, xmax = .5, ymin = -42.5, ymax = 42.5)
  red_line_detail = blocked_center_line(center = c(seq(-40.5, -1, by = 5), 0))
  red_line_detail = rbind(red_line_detail, data.frame(xmin = red_line_detail$xmin, xmax = red_line_detail$xmax, ymin = -red_line_detail$ymax, ymax = -red_line_detail$ymin))
  
  # Create referee's crease
  ref_crease = create_circle(center = c(0, -42.5), diameter = 20, start = 0, end = 1)
  ref_crease = rbind(ref_crease, create_circle(center = c(0, -42.5), diameter = 20 - (4/12), start = 1, end = 0))
  
  # Create blue line
  blue_line = data.frame(xmin = -26, xmax = -25, ymin = -42.5, ymax = 42.5)
  blue_line = rbind(
    blue_line, 
    data.frame(xmin = -blue_line$xmin, xmax = -blue_line$xmax, ymin = -blue_line$ymin, ymax = -blue_line$ymax)
  )
  
  # Create goal line
  goal_line = data.frame(xmin = 89 - (1/12), xmax = 89 + (1/12), ymin = -36.77, ymax = 36.77)
  goal_line = rbind(goal_line, data.frame(xmin = -89 - (1/12), xmax = -89 + (1/12), ymin = -36.77, ymax = 36.77))
  #goal_line = rbind(goal_line, data.frame(xmin = -goal_line$xmax, xmax = -goal_line$xmin, ymin = goal_line$ymin, ymax = goal_line$ymax))
  
  # Create goal crease
  crease = data.frame(
    x = c(-89, (-83 - (2/12)) - ((1.5 * seq(-4, 4, length = 100)^2) / (4^2)), -89, -89),
    y = c(-4 + (2/12), seq(-4 + (2/12), 4 - (2/12), length = 100), 4 - (2/12), -4 + (2/12))
  )
  
  crease_outline = data.frame(
    x = c(-89, -83 - ((1.5 * seq(-4, 4, length = 100)^2) / (4^2)), -89, -89, -85, -85, -85 + (2/12), -85 + (2/12), rev((-83 - (2/12)) - ((1.5 * seq(-4, 4, length = 100)^2) / (4^2))),-85 + (2/12), -85 + (2/12), -85, -85,-89, -89),
    y = c(-4, seq(-4, 4, length = 100), 4, 4 - (2/12), 4 - (2/12), 4 - (7/12), 4 - (7/12), 4 - (2/12), seq(4 - (2/12), -4 + (2/12), length = 100), -4 + (2/12), -4 + (7/12), -4 + (7/12), -4 + (2/12), -4 + (2/12), -4)
  )
  
  # Create goal
  goal = data.frame(x = -89, y = 3)
  goal = rbind(goal, create_circle(center = c(-89 - (20/12), 2), diameter = (40/12), start = 1/3, end = 1))
  goal = rbind(goal, create_circle(center = c(-89 - (20/12), -2), diameter = (40/12), start = 1, end = 5/3))
  goal = rbind(goal, data.frame(x = -89, y = -3))
  goal = rbind(goal, data.frame(x = -89, y = -3 - (2.375/12)))
  goal = rbind(goal, create_circle(center = c(-89 - (20/12), -2), diameter = (40/12) + (4.75/12), start = 5/3, end = 1))
  goal = rbind(goal, create_circle(center = c(-89 - (20/12), 2), diameter = (40/12) + (4.75/12), start = 1, end = 1/3))
  goal = rbind(goal, data.frame(x = -89, y = 3 + (2.375/12)))
  
  goal_fill = data.frame(x = -89, y = 3)
  goal_fill = rbind(goal_fill, create_circle(center = c(-89 - (20/12), 2), diameter = (40/12), start = 1/3, end = 1))
  goal_fill = rbind(goal_fill, create_circle(center = c(-89 - (20/12), -2), diameter = (40/12), start = 1, end = 5/3))
  goal_fill = rbind(goal_fill, data.frame(x = -89, y = -3))
  
  # Create restricted areas
  left_restricted_area = data.frame(
    x = c(-89, -100, -100, -89, -89),
    y = c(11 - (1/12), 14 - (1/12), 14 + (1/12), 11 + (1/12), 11 - (1/12))
  )
  left_restricted_area = rbind(left_restricted_area, data.frame(x = left_restricted_area$x, y = -left_restricted_area$y))
  
  right_restricted_area = data.frame(
    x = c(89, 100, 100, 89, 89),
    y = c(11 - (1/12), 14 - (1/12), 14 + (1/12), 11 + (1/12), 11 - (1/12))
  )
  right_restricted_area = rbind(right_restricted_area, data.frame(x = right_restricted_area$x, y = -right_restricted_area$y))
  
  
  # Make rink
  ggplot() +
    coord_fixed() +
    theme(
      panel.border = element_blank(),
      panel.background = element_blank(),
      axis.title = element_blank(),
      axis.text = element_blank(),
      axis.ticks = element_blank()
    ) +
    geom_polygon(data = boards, aes(x, y), fill = '#ffcb05') +
    annotation_custom(nhl_logo, xmin = -logo_borders$xmin, xmax = logo_borders$xmax, ymin = -logo_borders$ymin, ymax = logo_borders$ymax) +
    geom_polygon(data = center_circle, aes(x, y), fill = '#0033a0') +
    geom_polygon(data = faceoff_circles_l, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = faceoff_circles_r, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_l_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_l_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_nz_l_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_nz_l_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_nz_r_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_nz_r_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_r_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_r_dot, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_l_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_l_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_nz_l_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_nz_l_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_nz_r_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_nz_r_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = l_r_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = h_r_dot_fill, aes(x, y), fill = '#c8102e') +
    geom_rect(data = faceoff_details, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#c8102e') +
    geom_rect(data = red_line, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#c8102e') +
    geom_rect(data = red_line_detail, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_polygon(data = center_dot, aes(x, y), fill = '#0033a0') +
    geom_polygon(data = ref_crease, aes(x, y), fill = '#c8102e') +
    geom_rect(data = blue_line, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#0033a0') +
    geom_polygon(data = crease, aes(x, y), fill = '#0088ce') +
    geom_polygon(data = crease_outline, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = crease, aes(-x, y), fill = '#0088ce') +
    geom_polygon(data = crease_outline, aes(-x, y), fill = '#c8102e') +
    geom_polygon(data = left_restricted_area, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = right_restricted_area, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = goal, aes(x, y), fill = '#c8102e') +
    geom_polygon(data = goal, aes(-x, y), fill = '#c8102e') +
    geom_polygon(data = goal_fill, aes(x, y), fill = '#939598') +
    geom_polygon(data = goal_fill, aes(-x, y), fill = '#939598') +
    geom_rect(data = goal_line, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#c8102e')
}
