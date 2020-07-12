def bubbleSort(array):
    length = len(array)

    for i in range(length - 1):
        for j in range(0, length - i - 1):  # Inner loop that runs decrementally as the array gets sorted.

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


demoArray = [98, 43, 51, 19, 2, 31, 40]
print("Original Array:", demoArray)
print("Sorted array:", bubbleSort(demoArray))
