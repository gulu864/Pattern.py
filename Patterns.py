print("How much pyramids you want to be as numbers?")
row=int(input("Enter a number of rows:"))

for i in range(row):
    for j in range(i + 1):
        print("*", end="")
    print()
for i in range(row,0,-1):
    for j in range(i):
       print("*", end="")
    print()
for i in range(row,0,-1):
    for j in range(i):
        print(i, end="")
    print()