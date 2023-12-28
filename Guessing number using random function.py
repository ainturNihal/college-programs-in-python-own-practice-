import random
v = random.randint(1,123)
b = int(input("Guess a number from 1-123: "))
if b == v:
  print(f"You guess correctly! I choosed {v}")
else:
  print(f"You guessed it wrong! I choosed {v}")