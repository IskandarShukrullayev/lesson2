import random
from datetime import datetime

data = list()
for i in range(20):
    data.append(random.randint(1, 50))

data = sorted(set(data))
print("Tartiblangan Ma'lumotlar:", data)

target = int(input("qidiryotgan soningizni kiriting: "))

def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

start_time = datetime.now()
linear_result = linear_search(data, target)
end_time = datetime.now()
print(f"natija: {linear_result}, vaqt: {end_time - start_time}")