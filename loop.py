#while loop
#syntax:
# while True:(infinite time run hunxa)
# while condition: (finite time run hunxa)

l1 = [2,3,5,6]
total = 0
index = 0
while index < len(l1):
    item = l1[index]
    total = total + item

    index = index + 1
print("total = ",total)

