def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


demoArray = [98, 43, 51, 19, 2, 31, 40]
print("Original Array:", demoArray)
print("Sorted array:", insertionSort(demoArray))
