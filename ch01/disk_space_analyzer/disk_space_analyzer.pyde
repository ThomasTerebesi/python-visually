size(600, 600)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()

# Partial circle of two radians length
arc(width/2, height/2,
    200, 200,
    0, 2)

# Semi-circle
arc(width/2, height/2,
    300, 300,
    0, PI)

# Full-circle
arc(width/2, height/2,
    400, 400,
    0, PI * 2)

# Forming a "Slice"
arc(width/2, height/2,
    350, 350,
    3.4, (PI * 2 )- (PI / 2),
    PIE)
