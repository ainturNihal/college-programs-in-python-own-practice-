import time
print("This is a simple calculator to add, subtract, multiply, and divide.")
x = int(input("Enter a number for x: "))
y = (input("Add +,-,*,/: "))
z = int(input("Enter a number for y: "))
if y == "+":
  time.sleep(1)
  print(x+z)
if y == "-":
  time.sleep(1)
  print(x-z)
if y == "*":
  time.sleep(1)
  print(x*z)
if y == "/":
  time.sleep(1)
  print(x/z)
