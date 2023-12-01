num = [4,54,65,3,4,6,7,9,1,1,2,1,458,9,46,69]
num.sort()
print(f"\nEntered numbers sorted in assending manner:\n{num}")
num.sort(reverse=True)
print(f"\nAll numbers sorted in dessending order:\n{num}")
min = min(num)
max = max(num)
print(f"\nThe minimum number from the list: {min}")
print(f"\nThe maximum number from the list: {max}")