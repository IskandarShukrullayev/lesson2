import random
import time
from datetime import datetime

data = list(range(1,60))
for i in range(20):
    data.append(random.randint(1, 50))

data = sorted(set(data))
print("Tartiblangan Ma'lumotlar:", data)

target = int(input("qidiryotgan soningizni kiriting: "))

low = 0
high = len(data) - 1
count = 0

start_time = datetime.now()

while low <= high:
    count += 1
    middle = (low + high) // 2
    if data[middle] < target:
        low = middle + 1
    elif data[middle] == target:
        binary_result = middle
        break
    else:
        high = middle - 1
else:
    binary_result = -1

end_time = datetime.now()

print(f"Binary Search natija: {binary_result}, vaqt: {end_time - start_time}, qidiruv soni: {count}")
