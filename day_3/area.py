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
