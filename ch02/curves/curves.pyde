size(500,500)
grid = loadImage('grid.png')
image(grid, 0, 0)
noFill()
strokeWeight(3)

# Draw a straight line
stroke('#0099FF') # pale blue
line(100, 100, 
     400, 400)

# Draw a Catmull-Rom spline
curveTightness(0)
stroke('#FFFF00') # yellow
curve(0, 250,
      100, 100,
      400, 400,
      500, 250)

# Draw control point splines
stroke('#FF9900') # orange
curve(0, 250,
      0, 250,
      100, 100,
      400, 400)

curve(100, 100,
      400, 400,
      500, 250,
      500, 250)

# Draw Bézier curve
stroke('#FF99FF')

cp1x = 200
cp1y = 250
cp2x = 320
cp2y = 420

bezier(400, 100,
       cp1x, cp1y,
       cp2x, cp2y,
       100, 400)

# Draw line to control points
stroke('#FF0000')
line(400, 100,
     cp1x, cp1y)
line(100, 400,
     cp2x, cp2y)
