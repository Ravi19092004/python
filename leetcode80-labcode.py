def removeDuplicates(arr):
    if not arr:
        return 0
    temp = [arr[0]]
    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            temp.append(arr[i])
            j += 1
    for i in range(j):
        arr[i] = temp[i]
    return j

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
n = removeDuplicates(arr)
print(arr[:n])