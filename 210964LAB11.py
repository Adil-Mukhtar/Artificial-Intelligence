import math
import pandas as pd

entries = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'height': [5, 5.11, 5.6, 5.9, 4.8, 5.8, 5.3, 5.8, 5.5, 5.6, 5.5],
    'age': [45, 26, 30, 34, 40, 36, 19, 28, 23, 32, 38],
    'weight': [77 ,47, 55, 59, 72, 60, 40, 60, 45, 58, 0]
}


x2 = 38
y2 = 5.5
distances = []

for i in range(len(entries['id']) - 1):
    x1 = entries['height'][i]
    y1 = entries['age'][i]
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distances.append(distance)




temp = 0
for ID, distance in enumerate(distances, start=1):
    if temp < distance:
        temp = distance

print("\nlargest distance is: ", temp)

updated = entries
updated['weight'][10] = temp

before = pd.DataFrame(entries)
result = pd.DataFrame(updated)

print("\nBefore Updation: \n\n",before)
print("\n\nAfter Updation: \n\n",result)