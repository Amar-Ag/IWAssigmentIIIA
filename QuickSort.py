def partition(Array, low, up):
    i = low + 1
    j = up
    pivot = Array[low]
    while (i <= j):
        while (Array[i] < pivot and i < up):
            i = i + 1
        while (Array[j] > pivot):
            j = j - 1
        if (i < j):
            Array[i], Array[j] = Array[j], Array[i]
            i = i + 1
            j = j - 1
        else:
            i = i + 1
    Array[low] = Array[j]
    Array[j] = pivot
    return j


def quickSort(Array, low, up):
    if (low >= up):
        return
    piv_loc = partition(Array, low, up)
    quickSort(Array, low, piv_loc - 1)
    quickSort(Array, piv_loc + 1, up)
    return Array


demoArray = [98, 43, 51, 19, 2, 31, 40]
print("Original Array:", demoArray)
print("Sorted array:", quickSort(demoArray, 0, len(demoArray) - 1))
