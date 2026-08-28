import math


    # Area of a triangle
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(area)

    # Perimeter of a triangle
side_a = int(input("Enter side a of the triangle: "))
side_b = int(input("Enter side b of the triangle: "))
side_c = int(input("Enter side c of the triangle: "))
perimeter = side_a + side_b + side_c
print(perimeter)

    # Area and Perimeter of a Rectangle
length = int(input("Enter the length of the Rectangle: "))
height = int(input("Enter the height of the Rectangle: "))
area = length * height
perimeter = 2 * (length + height)
print(area, perimeter)

    # Area and Circumference of a Circle
pi = 3.14
radius = int(input("Enter the radius of the circle: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print(area, circumference)

    # Find the slope, x-intercept and y-intercept of y = 2x -2
slope_1 = 2

# Y Intercept
x = 0
y_intercept = (slope_1 * x) - 2

# X Intercept
x_intercept = (0 - y_intercept) / slope_1
print(slope_1, x_intercept, y_intercept)

    # Find slope m = y2-y1/x2-x1 and Euclidean distance between point (2, 2) and point (6,10)
slope_2 = (10 - 2) / (6 - 2)
euclidean = math.dist((2, 2), (6, 10))
print(slope_2, euclidean)

    # Comparing slopes
print(slope_1 == slope_2)

    # Calculate the value of y (y = x^2 + 6x + 9) using different x values that make y = 0
