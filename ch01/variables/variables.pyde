# Assigns values to width and height system variables
size(600,400)
background('#004477')
noStroke()

# Prints display window's width and height to the console
print(width)
print(height)

# Custom variables
x = 10
print(x)

y = 30
w = 100
h = w

rect(x, y, 
     w, h)

print(x + 2) # displays 12
print(x - 2) # displays 8

print(1 + 2 * 3) # displays 7
print((1 + 2) * 3) # displays 9

print(3 / 2) # displays 1
print(3 / 2.0) # displays 1.5

print(5.0 / 2) # displays 2.5
print(5.0 % 2) # displays 1.0

print(7 % 2) # displays 1, therefore 7 is odd
print(6 % 2) # displays 0, therefore 6 is even
