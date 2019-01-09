#####################################################################################
#####################################################################################
## This script produces a ggplot version of a regulation NCAA court. Each unit     ##
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

draw_ncaa = function(mens = TRUE){
  ncaa_logo = readPNG('League Logos/ncaa.png')
  ncaa_logo = rasterGrob(ncaa_logo, interpolate = TRUE)
  
  logo_borders = data.frame(xmin = -6, xmax = 6, ymin = -6, ymax = 6)
  
  # Create court
  court_in = data.frame(xmin = -47, xmax = 47, ymin = -25, ymax = 25)
  
  # Create baseline
  baseline = data.frame(
    xmin = c(-47 - (8/12), 47), 
    xmax = c(-47, 47 + (8/12)), 
    ymin = c(-25 - (8/12), -25 - (8/12)), 
    ymax = c(25 + (8/12), 25 + (8/12))
  )
  
  # Create sideline
  sideline = data.frame(
    xmin = c(-47 - (8/12), -47 - (8/12)), 
    xmax = c(47 + (8/12), 47 + (8/12)), 
    ymin = c(-25 - (8/12), 25), 
    ymax = c(-25, 25 + (8/12)) 
  )
  
  # Create division line
  division_line = data.frame(xmin = -(1/12), xmax = (1/12), ymin = -25, ymax = 25)
  
  # Create center circle
  center_circle = create_circle(center = c(0, 0), diameter = 12, start = -1/2, end = 1/2)
  center_circle = rbind(center_circle, data.frame(x = 0, y = 6 - (2/12)))
  center_circle = rbind(center_circle, create_circle(center = c(0, 0), diameter = 12 - (4/12), start = 1/2, end = -1/2))
  center_circle = rbind(center_circle, data.frame(x = 0, y = -6))
  center_circle = rbind(center_circle, data.frame(x = -center_circle$x, y = center_circle$y))
  
  # Create three-point line
  three_pt_line = rbind(
    data.frame(x = -47, y = -20.75),
    create_circle(center = c(-41.75, 0), diameter = 41.5, start = -1/2, end = 1/2),
    data.frame(x = -47, y = 20.75),
    data.frame(x = -47, y = 20.75 - (2/12)),
    create_circle(center = c(-41.75, 0), diameter = 41.5 - (4/12), start = 1/2, end = -1/2),
    data.frame(x = -47, y = -20.75 + (2/12)),
    data.frame(x = -47, y = -20.75)
  )
  
  three_pt_line = rbind(
    three_pt_line,
    data.frame(x = -three_pt_line$x, y = three_pt_line$y)
  )
  
  # Create free-throw lane
  lane = data.frame(
    x = c(-47, -28, -28, -47, -47, -28 - (2/12), -28 - (2/12), -47, -47, -47),
    y = c( -6, -6, 6, 6, 6 - (2/12), 6 - (2/12), -6 + (2/12), -6 + (2/12), 6, -6) 
  )
  
  lane = rbind(
    lane,
    data.frame(x = -lane$x, y = lane$y)
  )
  
  # Create free-throw circle
  free_throw_circle = rbind(
    create_circle(center = c(-28, 0), start = -1/2, end = 1/2, diameter = 12),
    data.frame(x = -28, y = 6),
    create_circle(center = c(-28, 0), start = 1/2, end = -1/2, diameter = 12 - (4/12)),
    data.frame(x = -28, y = -6)
  )
  
  free_throw_circle = rbind(
    free_throw_circle,
    data.frame(x = -free_throw_circle$x, y = free_throw_circle$y)
  )
  
  # Create restricted area
  restricted_area = rbind(
    data.frame(x = -43, y = -4 - (2/12)),
    create_circle(center = c(-41.75, 0), start = -1/2, end = 1/2, diameter = 8 + (4/12)),
    data.frame(x = -43, y = 4 + (2/12)),
    data.frame(x = -43, y = 4),
    create_circle(center = c(-41.75, 0), start = 1/2, end = -1/2, diameter = 8),
    data.frame(x = -43, y = -4),
    data.frame(x = -43, y = -4 - (2/12))
  )
  
  restricted_area = rbind(
    restricted_area,
    data.frame(x = -restricted_area$x, y = restricted_area$y)
  )
  
  # Create blocks
  blocks = data.frame(
    xmin = c(-40, -40, 39, 39, 
             -36, -36, 36 - (2/12), 36 - (2/12),
             -33 + (2/12), -33 + (2/12), 33 - (4/12), 33 - (4/12),
             -30 + (4/12), -30 + (4/12), 30 - (6/12), 30 - (6/12)
    ),
    xmax = c(-39, -39, 40, 40, 
             -36 + (2/12), -36 + (2/12), 36, 36,
             -33 + (4/12), -33 + (4/12), 33 - (2/12), 33 - (2/12),
             -30 + (6/12), -30 + (6/12), 30 - (4/12), 30 - (4/12)
    ),
    ymin = c(-6 - (8/12), 6, -6 - (8/12), 6,
             -6 - (8/12), 6, -6 - (8/12), 6,
             -6 - (8/12), 6, -6 - (8/12), 6,
             -6 - (8/12), 6, -6 - (8/12), 6
    ),
    ymax = c(-6, 6 + (8/12), -6, 6 + (8/12),
             -6, 6 + (8/12), -6, 6 + (8/12),
             -6, 6 + (8/12), -6, 6 + (8/12),
             -6, 6 + (8/12), -6, 6 + (8/12)
    )
  )
  
  # Create baseline hashmarks (women only)
  w_baseline_hashes = data.frame(
    xmin = c(-47, -47, 46, 46),
    xmax = c(-46, -46, 47, 47),
    ymin = c(-9 - (2/12), 9, -9 - (2/12), 9),
    ymax = c(-9, 9 + (2/12), -9, 9 + (2/12))
  )
  
  # Create coaches box
  coaches_box = rbind(
    data.frame(x = -19 - (2/12), y = 22),
    data.frame(x = -19 - (2/12), y = 28),
    data.frame(x = -19, y = 28),
    data.frame(x = -19, y = 22),
    data.frame(x = -19 - (2/12), y = 22)
  )
  
  coaches_box = rbind(
    coaches_box,
    data.frame(x = -coaches_box$x, y = coaches_box$y)
  )
  
  # Create substitution area
  substitution_area = rbind(
    data.frame(x = -9 - (2/12), y = 25 + (8/12)),
    data.frame(x = -9 - (2/12), y = 27 + (8/12)),
    data.frame(x = -9, y = 27 + (8/12)),
    data.frame(x = -9, y = 25 + (8/12)),
    data.frame(x = -9 - (2/12), y= 25 + (8/12))
  )
  
  substitution_area = rbind(
    substitution_area,
    data.frame(x = -substitution_area$x, y = substitution_area$y)
  )
  
  # Create hoop
  backboard = data.frame(xmin = -43 - (4/12), xmax = -43, ymin = -3, ymax = 3)
  backboard = rbind(backboard, data.frame(xmin = -backboard$xmax, xmax = -backboard$xmin, ymin = backboard$ymin, ymax = backboard$ymax))
  
  rim_connector = data.frame(xmin = -43, xmax = -42.3, ymin = -(4/12), ymax = (4/12))
  rim_connector = rbind(rim_connector, data.frame(xmin = -rim_connector$xmax, xmax = -rim_connector$xmin, ymin = rim_connector$ymin, ymax = rim_connector$ymax))
  
  rim = create_circle(center = c(-41.75, 0), diameter = 1.5 + (4/12))
  rim = rbind(rim, data.frame(x = -rim$x, y = rim$y))
  
  net = create_circle(center = c(-41.75, 0), diameter = 1.5)
  net = rbind(net, data.frame(x = -net$x, y = net$y))
  
  if(mens == TRUE){
    court = ggplot() +
      theme_void() +
      theme(
        panel.border = element_blank(),
        panel.background = element_blank(),
        axis.title = element_blank(),
        axis.text = element_blank(),
        axis.ticks = element_blank()
      ) +
      coord_fixed() +
      geom_rect(data = court_in, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#d2ab6f') +
      geom_rect(data = baseline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_rect(data = sideline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_rect(data = division_line, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_polygon(data = center_circle, aes(x, y), fill = '#000000') +
      geom_polygon(data = three_pt_line, aes(x, y), fill = '#000000') +
      geom_polygon(data = lane, aes(x, y), fill = '#000000') +
      geom_rect(data = blocks, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_polygon(data = free_throw_circle, aes(x, y), fill = '#000000') +
      geom_polygon(data = restricted_area, aes(x, y), fill = '#000000') +
      geom_polygon(data = coaches_box, aes(x, y), fill = '#000000') +
      geom_polygon(data = substitution_area, aes(x, y), fill = '#000000') +
      geom_rect(data = backboard, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_rect(data = rim_connector, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#e04e39') +
      geom_polygon(data = rim, aes(x, y), fill = '#e04e39') +
      geom_polygon(data = net, aes(x, y), fill = '#ffffff') +
      annotation_custom(ncaa_logo, xmin = logo_borders$xmin, xmax = logo_borders$xmax, ymin = logo_borders$ymin, ymax = logo_borders$ymax)
  }
  
  else{
    court = ggplot() +
      theme_void() +
      theme(
        panel.border = element_blank(),
        panel.background = element_blank(),
        axis.title = element_blank(),
        axis.text = element_blank(),
        axis.ticks = element_blank()
      ) +
      coord_fixed() +
      geom_rect(data = court_in, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#d2ab6f') +
      geom_rect(data = baseline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_rect(data = w_baseline_hashes, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_rect(data = sideline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_rect(data = division_line, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_polygon(data = center_circle, aes(x, y), fill = '#000000') +
      geom_polygon(data = three_pt_line, aes(x, y), fill = '#000000') +
      geom_polygon(data = lane, aes(x, y), fill = '#000000') +
      geom_rect(data = blocks, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_polygon(data = free_throw_circle, aes(x, y), fill = '#000000') +
      geom_polygon(data = restricted_area, aes(x, y), fill = '#000000') +
      geom_polygon(data = coaches_box, aes(x, y), fill = '#000000') +
      geom_polygon(data = substitution_area, aes(x, y), fill = '#000000') +
      geom_rect(data = backboard, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#000000') +
      geom_rect(data = rim_connector, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#e04e39') +
      geom_polygon(data = rim, aes(x, y), fill = '#e04e39') +
      geom_polygon(data = net, aes(x, y), fill = '#ffffff') +
      annotation_custom(ncaa_logo, xmin = logo_borders$xmin, xmax = logo_borders$xmax, ymin = logo_borders$ymin, ymax = logo_borders$ymax)
  }
  
  return(court)
}
