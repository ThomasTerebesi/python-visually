# Dimensions of the display window measured in pixels
size(500,500)

# Change background color
background('#004477')

# Set stroke
stroke('#FFFFFF')
strokeWeight(3)

# Red fill
fill('#FF0000')
rect(100, 150, 200, 300)

# Printing things
print("Hello, world!") # Writes "Hello, world!" to the console area

'''
This is a multiline comment.
Any code between the opening and closing triple-quotes is ignored. 
'''

print('How are you?')

# Small rectangle
rect(10, 15, 20, 30)

# Orange square
fill('#FF9900')
rect(50, 100, 150, 150)

# Square without fill
noFill()
square(250, 100, 150)

# Testing HSB color mode with circles
colorMode(HSB, 360, 100, 100)
fill(225,100,100)
circle(400, 200, 100)

fill(45,100,100)
circle(400, 300, 100)
