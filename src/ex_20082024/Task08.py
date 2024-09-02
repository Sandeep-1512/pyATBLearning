## Write a program that classifies a triangle based on its side lengths.

##Given three input values representing the lengths of the sides,

##determine if the triangle is equilateral (all sides are equal),

##isosceles (exactly two sides are equal), or scalene (no sides are equal).

##Use an if-else statement to classify the triangle.


angle = int(input("Enter length of side 1 : "))
angle2 = int(input("Enter length of side 2 : "))
angle3 = int(input("Enter length of side 3 : "))

if angle == angle2 and angle2 == angle3:
    print("This is Equilateral Angle:")
elif angle == angle2 and angle2 != angle3:
    print("This is isosceles")
else:
    print("Scalene")

