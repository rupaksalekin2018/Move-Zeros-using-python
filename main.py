def move_zeros(arr):
    j = 0
    for i in arr:
        if i != 0:
            arr[j] = i
            j = j + 1

    for x in range(j, len(arr)):
        arr[x] = 0

    return arr


arr = [0, 1, 0, 2, 3, 0, 0, 0, 12, 1]

result = move_zeros(arr)

if(result != -1):
    print('All the zero values are pushed to the end ', result)
else:
    print('Error')
