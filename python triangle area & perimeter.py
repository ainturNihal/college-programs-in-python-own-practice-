## apython program to find the area and perimeter of a traingle (The user will enter the values)

print("This a python program that will calculate the area  and perimeter of a triangle from your given values\n\n\n")
a = int(input("\nEnter the value of side a: "))
b = int(input("\nEnter the value of side b: "))
c = int(input("\nEnter the value of side c: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"\n\n\nThe area of the triangle is: {area:.2f}")
print(f"\nThe perimter of the triangle is: {s:.2f}")

