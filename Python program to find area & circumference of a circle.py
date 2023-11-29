## a python proram to determine the areaand circumference of a circle
print("This a python program to find the area and circumference of  circle\n")
PI = 3.1416
radius = int(input("Enter the circumference of the circle: "))
circumference =  2*PI*radius
area = PI*radius**2
print(f"Area of the circle = {area:.2f}")
print(f"Circumference of thr circle = {circumference:.2f}")