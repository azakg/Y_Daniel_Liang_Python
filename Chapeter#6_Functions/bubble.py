def bubble_sort(arr):
    n = len(arr)
    newArr = []
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                newArr[j], newArr[j+1] = arr[j+1], arr[j]
    return newArr

arr1 = [4,7,3,8,67,2,6,1]
print(bubble_sort(arr1))