#####################################################################################
#####################################################################################
## This script produces a ggplot version of a regulation NFL field. Each unit      ##
## in x and y is equivalent to one foot (12 in) and all parts of the model are     ##
## drawn to scale.                                                                 ##
#####################################################################################
#####################################################################################

library(ggplot2)
library(png)
library(grid)
library(raster)
library(magick)

draw_nfl = function(){
  nfl_logo = readPNG('League Logos/nfl.png')
  nfl_logo = rasterGrob(nfl_logo, interpolate = TRUE)
  
  logo_borders = data.frame(xmin = -18, xmax = 18, ymin = -30, ymax = 30)
  
  field = data.frame(xmin = -190, xmax = 190, ymin = -90, ymax = 90)
  sideline = data.frame(xmin = c(-180, -180), xmax = c(180, 180), ymin = c(-86, 80), ymax = c(-80, 86))
  endline = data.frame(xmin = c(-186, 180), xmax = c(-180, 186), ymin = c(-86, -86), ymax = c(86, 86))
  goalline = data.frame(xmin = c(-150 - (2/12), 150 - (2/12)), xmax = c(-150 + (2/12), 150 + (2/12)), ymin = c(-86, -86), ymax = c(86, 86))
  midline = data.frame(xmin = -2/12, xmax = 2/12, ymin = -80 + 4/12, ymax = 80 - 4/12)
  yd_line = data.frame(xmin = -147 - (2/12), xmax = -147 + (2/12), ymin = -80 + (4/12), ymax = -78 + (4/12))
  
  minor_yd_lines = data.frame(xmin = rep(NA, 49), xmax = rep(NA, 49), ymin = rep(NA, 49), ymax = rep(NA, 49))
  
  for(i in 1:49){
    minor_yd_lines$xmin[i] = (0 - (3 * i)) - (2/12)
    minor_yd_lines$xmax[i] = (0 - (3 * i)) + (2/12)
    minor_yd_lines$ymin[i] = -80 + (4/12)
    minor_yd_lines$ymax[i] = -78 + (4/12)
  }
  
  minor_yd_lines = rbind(minor_yd_lines, data.frame(xmin = rep(NA, 49), xmax = rep(NA, 49), ymin = rep(NA, 49), ymax = rep(NA, 49)))
  
  for(i in 50:98){
    minor_yd_lines$xmin[i] = (0 - (3 * (i - 49))) - (2/12)
    minor_yd_lines$xmax[i] = (0 - (3 * (i - 49))) + (2/12)
    minor_yd_lines$ymin[i] = 78 - (4/12)
    minor_yd_lines$ymax[i] = 80 - (4/12)
  }
  
  minor_yd_lines = rbind(minor_yd_lines, data.frame(xmin = rep(NA, 49), xmax = rep(NA, 49), ymin = rep(NA, 49), ymax = rep(NA, 49)))
  
  for(i in 99:147){
    minor_yd_lines$xmin[i] = (0 - (3 * (i - 98))) - (2/12)
    minor_yd_lines$xmax[i] = (0 - (3 * (i - 98))) + (2/12)
    minor_yd_lines$ymin[i] = -22 + (4/12)
    minor_yd_lines$ymax[i] = -20 + (4/12)
  }
  
  minor_yd_lines = rbind(minor_yd_lines, data.frame(xmin = rep(NA, 49), xmax = rep(NA, 49), ymin = rep(NA, 49), ymax = rep(NA, 49)))
  
  for(i in 148:196){
    minor_yd_lines$xmin[i] = (0 - (3 * (i - 147))) - (2/12)
    minor_yd_lines$xmax[i] = (0 - (3 * (i - 147))) + (2/12)
    minor_yd_lines$ymin[i] = 20 - (4/12)
    minor_yd_lines$ymax[i] = 22 - (4/12)
  }
  
  minor_yd_lines = rbind(minor_yd_lines, data.frame(xmin = -minor_yd_lines$xmax, xmax = -minor_yd_lines$xmin, ymin = minor_yd_lines$ymin, ymax = minor_yd_lines$ymax))
  
  major_yd_lines = data.frame(
    xmin = seq(0, 150, by = 15) - (2/12),
    xmax = seq(0, 150, by = 15) + (2/12),
    ymin = -80 + (4/12),
    ymax = 80 - (4/12)
  )
  
  major_yd_lines = rbind(major_yd_lines, data.frame(xmin = -major_yd_lines$xmax, xmax = -major_yd_lines$xmin, ymin = major_yd_lines$ymin, ymax = major_yd_lines$ymax))
  
  hashes = data.frame(xmin = rep(NA, 9), xmax = rep(NA, 9), ymin = rep(NA, 9), ymax = rep(NA, 9))
  for(i in 1:9){
    hashes$xmin[i] = (0 - (15 * i)) - (10/12)
    hashes$xmax[i] = (0 - (15 * i)) + (10/12)
    hashes$ymin[i] = -20 + (4/12)
    hashes$ymax[i] = -20 + (2/12)
  }
  
  hashes = rbind(
    hashes,
    data.frame(xmin = hashes$xmin, xmax = hashes$xmax, ymin = -hashes$ymax, ymax = -hashes$ymin)
  )
  
  hashes = rbind(
    hashes,
    data.frame(xmin = -hashes$xmax, xmax = -hashes$xmin, ymin = hashes$ymin, ymax = hashes$ymax)
  )
  
  extra_pt_mark = data.frame(xmin = c(-141 - (2/12), 141 - (2/12)), xmax = c(-141 + (2/12), 141 + (2/12)), ymin = c(-1, -1), ymax = c(1, 1))
  
  arrows_40 = data.frame(
    x = c(
      -36 - (6/12), -36 - (6/12), -36 - ((sqrt((36^2) - 36))/12), -36 - (6/12), -36 - (6/12),
      -36 - (6/12), -36 - (6/12), -36 - ((sqrt((36^2) - 36))/12), -36 - (6/12), -36 - (6/12)
    ),
    y = c(
      -44, -44 + (9/12), -44, -44 - (9/12), -44,
      44, 44 - (9/12), 44, 44 + (9/12), 44
    )
  )
  
  arrows_30 = data.frame(
    x = c(-66 - (6/12), -66 - (6/12), -66 - ((sqrt((36^2) - 36))/12), -66 - (6/12), -66 - (6/12),
          -66 - (6/12), -66 - (6/12), -66 - ((sqrt((36^2) - 36))/12), -66 - (6/12), -66 - (6/12)
    ),
    
    y = c( -44, -44 + (9/12), -44, -44 - (9/12), -44,
           44, 44 - (9/12), 44, 44 + (9/12), 44
    )
  )
  
  arrows_20 = data.frame(
    x = c(
      -96 - (6/12), -96 - (6/12), -96 - ((sqrt((36^2) - 36))/12), -96 - (6/12), -96 - (6/12),
      -96 - (6/12), -96 - (6/12), -96 - ((sqrt((36^2) - 36))/12), -96 - (6/12), -96 - (6/12)
    ),
    y = c(
      -44, -44 + (9/12), -44, -44 - (9/12), -44,
      44, 44 - (9/12), 44, 44 + (9/12), 44
    )
  )
  
  arrows_10 = data.frame(
    x = c(
      -126 - (6/12), -126 - (6/12), -126 - ((sqrt((36^2) - 36))/12), -126 - (6/12), -126 - (6/12),
      -126 - (6/12), -126 - (6/12), -126 - ((sqrt((36^2) - 36))/12), -126 - (6/12), -126 - (6/12)
    ),
    y = c(
      -44, -44 + (9/12), -44, -44 - (9/12), -44,
      44, 44 - (9/12), 44, 44 + (9/12), 44
    )
  )
  
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
    geom_rect(data = field, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#196f0c') +
    geom_rect(data = sideline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = endline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = goalline, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = minor_yd_lines, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = major_yd_lines, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    geom_rect(data = extra_pt_mark, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff') +
    annotation_custom(nfl_logo, xmin = logo_borders$xmin, xmax = logo_borders$xmax, ymin = logo_borders$ymin, ymax = logo_borders$ymax) +
    annotate('text', label = '5', x = -3, y = -44, col = '#ffffff') +
    annotate('text', label = '0', x = c(3, -27, 33, -57, 63, -87, 93, -117, 123), y = -44, col = '#ffffff') +
    annotate('text', label = '4', x = c(-33, 27), y = -44, col = '#ffffff') +
    annotate('text', label = '3', x = c(-63, 57), y = -44, col = '#ffffff') +
    annotate('text', label = '2', x = c(-93, 87), y = -44, col = '#ffffff') +
    annotate('text', label = '1', x = c(-123, 117), y = -44, col = '#ffffff') +
    annotate('text', label = '5', x = 3, y = 44, col = '#ffffff', angle = 180) +
    annotate('text', label = '0', x = c(-3, 27, -33, 57, -63, 87, -93, 117, -123), y = 44, col = '#ffffff', angle = 180) +
    annotate('text', label = '4', x = c(33, -27), y = 44, col = '#ffffff', angle = 180) +
    annotate('text', label = '3', x = c(63, -57), y = 44, col = '#ffffff', angle = 180) +
    annotate('text', label = '2', x = c(93, -87), y = 44, col = '#ffffff', angle = 180) +
    annotate('text', label = '1', x = c(123, -117), y = 44, col = '#ffffff', angle = 180) +
    geom_polygon(data = arrows_40, aes(x, y), fill = '#ffffff') +
    geom_polygon(data = arrows_30, aes(x, y), fill = '#ffffff') +
    geom_polygon(data = arrows_20, aes(x, y), fill = '#ffffff') +
    geom_polygon(data = arrows_10, aes(x, y), fill = '#ffffff') +
    geom_polygon(data = arrows_40, aes(-x, y), fill = '#ffffff') +
    geom_polygon(data = arrows_30, aes(-x, y), fill = '#ffffff') +
    geom_polygon(data = arrows_20, aes(-x, y), fill = '#ffffff') +
    geom_polygon(data = arrows_10, aes(-x, y), fill = '#ffffff') +
    geom_rect(data = hashes, aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), fill = '#ffffff')
}
