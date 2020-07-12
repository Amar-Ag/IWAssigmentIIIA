def interpolationSearch(arr, n, x):
    lo = 0
    hi = (n - 1)

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo;
            return -1;

        pos = lo + int(((float(hi - lo) /
                         (arr[hi] - arr[lo])) * (x - arr[lo])))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            lo = pos + 1;
        else:
            hi = pos - 1;

    return -1


demoArray = [9, 11, 5, 0, 2, 1, 90, 107]
term = int(input("Enter the element you want: "))
result = interpolationSearch(sorted(demoArray), len(demoArray), term)
print("Original array:", demoArray)
print("Sorted array:", sorted(demoArray))
if result != -1:
    print(f"{term} found at {result}")
else:
    print(f"{term} not found.")
