def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


demoArray = [98, 43, 51, 19, 2, 31, 40]
print("Original Array:", demoArray)
userChoice = int(input("Enter the term you want to search:"))
if binary_search(sorted(demoArray), userChoice):
    print(f"{userChoice} found")
else:
    print(f"{userChoice} not found")
