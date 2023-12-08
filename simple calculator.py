import time
print("This is a simple calculator to add, subtract, multiply, and divide.")
x = float(input("Enter a number for x: "))
y = (input("Add +,-,*,/: "))
z = float(input("Enter a number for y: "))
if y == "+":
  time.sleep(1)
  print(round(x+z))
if y == "-":
  time.sleep(1)
  print(round(x-z))
if y == "*":
  time.sleep(1)
  print(round(x*z))
if y == "/":
  time.sleep(1)
  print(round(x/z))
