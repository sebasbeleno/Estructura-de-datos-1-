arr = [50, 30, 40, 20]
n = len(arr)

for i in range(1, len(arr)):
    arr = arr[1:].append(arr[0])

    print(arr)