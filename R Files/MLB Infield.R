#####################################################################################
#####################################################################################
## This script produces a ggplot version of a regulation MLB infield. Each unit    ##
## in x and y is equivalent to one foot (12 in) and all parts of the model are     ##
## drawn to scale.                                                                 ##
#####################################################################################
#####################################################################################

create_circle = function(center = c(0, 0), npoints = 500, diameter = 1, start = 0, end = 2) {
  pts = seq(start * pi, end * pi, length.out = npoints)
  data.frame(x = center[1] + ((diameter/2) * cos(pts)),
             y = center[2] + ((diameter/2) * sin(pts)))
}

a = 2

b = (2 * (((45 - (3 * sin(pi/4))) - (45 + (3 * cos(pi/4)))) - 60.5))

c =  (((((45 - (3 * sin(pi/4))) - (45 + (3 * cos(pi/4)))) - 60.5)^2) - (95^2))

infield_dirt = rbind(
  data.frame(x = 0, y = (45 - (3 * sin(pi/4))) - (45 + (3 * cos(pi/4)))),
  data.frame(x = (-b + sqrt((b^2) - (4 * a * c)))/(2 * a), 
             y = ((-b + sqrt((b^2) - (4 * a * c)))/(2 * a)) + ((45 - (3 * sin(pi/4))) - (45 + (3 * cos(pi/4))))
             ),
  create_circle(
    center = c(0, 60.5),
    diameter = 190,
    start = atan2(
      y = ((-b + sqrt((b^2) - (4 * a * c)))/(2 * a)) - 60.5,
      x = ((-b + sqrt((b^2) - (4 * a * c)))/(2 * a))
    )/pi,
    end = 1 - (atan2(
      y = ((-b + sqrt((b^2) - (4 * a * c)))/(2 * a)) - 60.5,
      x = ((-b + sqrt((b^2) - (4 * a * c)))/(2 * a))
    )/pi)
  ),
  data.frame(x = -((-b + sqrt((b^2) - (4 * a * c)))/(2 * a)), 
             y = ((-b + sqrt((b^2) - (4 * a * c)))/(2 * a)) + ((45 - (3 * sin(pi/4))) - (45 + (3 * cos(pi/4))))
  ),
  data.frame(x = 0, y = (45 - (3 * sin(pi/4))) - (45 + (3 * cos(pi/4))))
)



infield_grass = data.frame(
  x = c(0, 
        (45 * sqrt(2)) - 3, 
        0, 
        (-45 * sqrt(2) + sqrt(2 * (15/12) * (15/12))) + 3),
  y = c(3, 
        45 * sqrt(2), 
        (sqrt(2 * (90^2)) - .5 * sqrt(2 * ((15/12)^2))) - 3, 
        45 * sqrt(2)),
  desc = c('Infield grass', 'Infield grass', 'Infield grass', 'Infield grass')
)

home_dirt = create_circle(center = c(0, 0), diameter = 26, start = 0, end = 2)

first_dirt = rbind(
  data.frame(x = (45 * sqrt(2)), y = 45 * sqrt(2)),
  create_circle(center = c((45 * sqrt(2)) - 3, 45 * sqrt(2)), diameter = 20, start = 3/4, end = 5/4),
  data.frame(x = (45 * sqrt(2)), y = 45 * sqrt(2))
)

second_dirt = rbind(
  data.frame(x = 0, y = (sqrt(2 * (90^2)) - .5 * sqrt(2 * ((15/12)^2))) - 3),
  create_circle(center = c(0, (sqrt(2 * (90^2)) - .5 * sqrt(2 * ((15/12)^2))) - 3), diameter = 20, start = 4.9/4, end = 7.1/4),
  data.frame(x = 0, y = (sqrt(2 * (90^2)) - .5 * sqrt(2 * ((15/12)^2))) - 3)
)

third_dirt = data.frame(x = -first_dirt$x, y = first_dirt$y)

mound = create_circle(center = c(0, 718/12), diameter = 9, start = 0, end = 2)

home_plate = data.frame(
  x = c(0, -8.5/12, -8.5/12, 8.5/12, 8.5/12),
  y = c(0, sqrt(1 - (8.5/12)^2), sqrt(1 - (8.5/12)^2) + (8.5/12), sqrt(1 - (8.5/12)^2) + (8.5/12), sqrt(1 - (8.5/12)^2)),
  desc = c('Home plate tip', 'Home plate back left', 'Home plate front left', 'Home plate front right', 'Home plate back right'),
  stringsAsFactors = FALSE
)

pitchers_plate = data.frame(
  x = c(-1, -1, 1, 1),
  y = c(60 + (6/12), 61, 61, 60 + (6/12)),
  desc = c('Pitcher\'s plate front left', 'Pitcher\'s plate back left', 'Pitcher\'s plate back right', 'Pitcher\'s plate front right'),
  stringsAsFactors = FALSE
)

first_base = data.frame(
  x = c(44.375 * sqrt(2), 45 * sqrt(2), 44.375 * sqrt(2), 45 * sqrt(2) - sqrt(2 * (15/12) * (15/12))),
  y = c(44.375 * sqrt(2), 45 * sqrt(2), (44.375 * sqrt(2)) + sqrt(2 * (15/12) * (15/12)), 45 * sqrt(2)),
  desc = c('1B front right corner', '1B back right corner', '1B back left corner', '1B front left corner'),
  stringsAsFactors = FALSE
)

second_base = data.frame(
  x = c(0, .625 * sqrt(2), 0, -.625 * sqrt(2)),
  y = c(sqrt(2 * (90^2)) - .5 * sqrt(2 * ((15/12)^2)), sqrt(2 * (90^2)), sqrt(2 * (90^2)) + .5 * sqrt(2 * ((15/12)^2)), sqrt(2 * (90^2))),
  desc = c('2B front corner', '2B right corner', '2B back corner', '2B left corner'),
  stringsAsFactors = FALSE
)

third_base = data.frame(
  x = c(-44.375 * sqrt(2), -45 * sqrt(2), -44.375 * sqrt(2), -45 * sqrt(2) + sqrt(2 * (15/12) * (15/12))),
  y = c(44.375 * sqrt(2), 45 * sqrt(2), (44.375 * sqrt(2)) + sqrt(2 * (15/12) * (15/12)), 45 * sqrt(2)),
  desc = c('3B front left corner', '3B back left corner', '3B back right corner', '3B front right corner'),
  stringsAsFactors = FALSE
)

lefty_batters_box = data.frame(
  x = c(38.5/12, 14.5/12, 14.5/12, 38.5/12, 38.5/12, 17.5/12, 17.5/12, 38.5/12, 38.5/12, 62.5/12, 62.5/12, 38.5/12, 38.5/12, 59.5/12, 59.5/12, 38.5/12, 38.5/12),
  y = c(sqrt(1 - (8.5/12)^2) - 3, sqrt(1 - (8.5/12)^2) - 3, sqrt(1 - (8.5/12)^2) + 3, sqrt(1 - (8.5/12)^2) + 3, sqrt(1 - (8.5/12)^2) + 2.75, sqrt(1 - (8.5/12)^2) + 2.75, sqrt(1 - (8.5/12)^2) - 2.75, sqrt(1 - (8.5/12)^2) - 2.75, sqrt(1 - (8.5/12)^2) - 3, sqrt(1 - (8.5/12)^2) - 3, sqrt(1 - (8.5/12)^2) + 3, sqrt(1 - (8.5/12)^2) + 3, sqrt(1 - (8.5/12)^2) + 2.75, sqrt(1 - (8.5/12)^2) + 2.75, sqrt(1 - (8.5/12)^2) - 2.75, sqrt(1 - (8.5/12)^2) - 2.75, sqrt(1 - (8.5/12)^2) - 3)
)

righty_batters_box = data.frame(x = -lefty_batters_box$x, y = lefty_batters_box$y)

catchers_box = data.frame(
  x = c(-23.5/12, -23.5/12, 23.5/12, 23.5/12, 20.5/12, 20.5/12, -20.5/12, -20.5/12, -23.5/12),
  y = c(sqrt(1 - (8.5/12)^2) - 3, -8, -8, sqrt(1 - (8.5/12)^2) - 3, sqrt(1 - (8.5/12)^2) - 3, -7.75, -7.75, sqrt(1 - (8.5/12)^2) - 3, sqrt(1 - (8.5/12)^2) - 3)
)

rf_line = data.frame(
  x = c(sqrt(1 - (8.5/12)^2) + 3, 155.5, 155.25, sqrt(1 - (8.5/12)^2) + 2.75, sqrt(1 - (8.5/12)^2) + 3), 
  y = c(sqrt(1 - (8.5/12)^2) + 3, 155.5, 155.5, sqrt(1 - (8.5/12)^2) + 3, sqrt(1 - (8.5/12)^2) + 3)
)

lf_line = data.frame(x = -rf_line$x, y = rf_line$y)

running_lane = data.frame(
  x = c(
    22.5 * sqrt(2),
    (22.5 * sqrt(2)) + (3 * cos(pi/4)),
    ((22.5 * sqrt(2)) + (3 * cos(pi/4))) + (45 * cos(pi/4)),
    (((22.5 * sqrt(2)) + (3 * cos(pi/4))) + (45 * cos(pi/4))) - ((3/12) * cos(pi/4)),
    ((((22.5 * sqrt(2)) + (3 * cos(pi/4))) + (45 * cos(pi/4))) - ((3/12) * cos(pi/4))) - (44.75 * cos(pi/4)),
    (((((22.5 * sqrt(2)) + (3 * cos(pi/4))) + (45 * cos(pi/4))) - ((3/12) * cos(pi/4))) - (44.75 * cos(pi/4))) - (3 * cos(pi/4))
  ),
  y = c(
    22.5 * sqrt(2),
    (22.5 * sqrt(2)) - (3 * sin(pi/4)),
    ((22.5 * sqrt(2)) - (3 * sin(pi/4))) + (45 * sin(pi/4)),
    (((22.5 * sqrt(2)) - (3 * sin(pi/4))) + (45 * sin(pi/4))) + ((3/12) * sin(pi/4)),
    ((((22.5 * sqrt(2)) - (3 * sin(pi/4))) + (45 * sin(pi/4))) + ((3/12) * sin(pi/4))) - (44.75 * cos(pi/4)),
    (((((22.5 * sqrt(2)) - (3 * sin(pi/4))) + (45 * sin(pi/4))) + ((3/12) * sin(pi/4))) - (44.75 * cos(pi/4))) + (3 * sin(pi/4))
  )
)

ggplot() +
  theme_void() +
  theme(
    plot.background = element_rect(fill = '#395d33')
  ) +
  geom_polygon(data = infield_dirt, aes(x, y), fill = '#9b7653') +
  geom_polygon(data = infield_grass, aes(x, y), fill = '#395d33') +
  geom_polygon(data = home_dirt, aes(x, y), fill = '#9b7653') +
  geom_polygon(data = first_dirt, aes(x, y), fill = '#9b7653') +
  geom_polygon(data = second_dirt, aes(x, y), fill = '#9b7653') +
  geom_polygon(data = third_dirt, aes(x, y), fill = '#9b7653') +
  geom_polygon(data = mound, aes(x, y), fill = '#9b7653') +
  geom_polygon(data = home_plate, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = lefty_batters_box, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = righty_batters_box, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = catchers_box, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = pitchers_plate, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = first_base, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = second_base, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = third_base, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = rf_line, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = lf_line, aes(x, y), fill = '#ffffff') +
  geom_polygon(data = running_lane, aes(x, y), fill = '#ffffff') +
  coord_fixed()

# ggplot() +
#   geom_polygon(data = home_plate, aes (x, y), fill = '#000000') +
#   coord_fixed()
