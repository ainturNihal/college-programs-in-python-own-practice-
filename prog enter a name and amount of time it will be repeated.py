import time
name = input("Enter a name you want to repeat: ")
n = int(input("How many times you want it to repeat: "))
num = (range(n))
for i in num:
  time.sleep(0.1)
  print(name)