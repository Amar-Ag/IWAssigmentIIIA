def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return False


demoArray = ['t', 'e', 's', 't', 'a', 'r', 'r', 'a', 'y']
userInput = input("Enter a element to search in the list:")
if linearsearch(demoArray, userInput):
    print("Element found at index " + str(linearsearch(demoArray, userInput)))
else:
    print("Element not found")
