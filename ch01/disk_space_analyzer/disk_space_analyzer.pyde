size(600, 600)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)

# Segments of 100MB
segment = PI * 2 / 14 

# Vacation
fill('#00AA33')
arc(width/2, height/2,
    600, 600,
    segment * 11, segment * 12, PIE)

# Metal
fill('#EEAACC')
arc(width/2, height/2,
    450, 450,
    segment * 7, segment * 9, PIE)

# Rap
fill('#EEAACC')
arc(width/2, height/2,
    450, 450,
    segment * 9, segment * 11, PIE)

# Photos
fill('#00AAEE')
arc(width/2, height/2,
    450, 450,
    segment * 11, segment * 13, PIE)

# Work
fill('#00AAEE')
arc(width/2, height/2,
    450, 450,
    segment * 13, segment * 14, PIE)

# Videos
fill("#EE2222")
arc(width/2, height/2,
    300, 300,
    0, segment * 7, PIE)

# Music
fill('#EE5599')
arc(width/2, height/2,
    300, 300,
    segment * 7, segment * 11, PIE)

# Docs
fill('#7755AA')
arc(width/2, height/2,
    300, 300,
    segment * 11, segment * 14, PIE)

# HDD
fill('#004477')
circle(width/2, height/2, 150)



"""
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
"""
