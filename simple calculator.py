import time
print("This is a simple calculator to add, subtract, multiply, and divide.")
x = float(input("Enter a number for x: "))
y = (input("Add +,-,*,/: "))
z = float(input("Enter a number for y: "))
if y == "+":
  time.sleep(1)
  a = x + z
  print(f"{a:.2f}")
if y == "-":
  time.sleep(1)
  b = x - z
  print(f"{b:.2f}")
if y == "*":
  time.sleep(1)
  c = x*z
  print(f"{c:.2f}")
if y == "/":
  time.sleep(1)
  d = x/z
  print(f"{d:.2f}")
