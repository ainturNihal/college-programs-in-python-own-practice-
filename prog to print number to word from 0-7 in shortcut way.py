num_to_word = {0: "Zero", 1: "One", 2: "Two", 3: "Three",
       4: "Four", 5: "Five", 6: "Six", 7: "Seven"}

num = int(input("Enter a number from 0-7 and the programwill show it in word form: "))
print(num_to_word.get(num, "Invalid number"))