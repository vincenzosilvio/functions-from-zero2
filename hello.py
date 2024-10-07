# create a list with 10 random fruits
import random

fruits = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "imbe",
    "jackfruit",
]
random.shuffle(fruits)

# print it
print(fruits)

# loop through the list and count the total number of fruits in the list
count = 0
for fruit in fruits:
    count += 1
print(count)
