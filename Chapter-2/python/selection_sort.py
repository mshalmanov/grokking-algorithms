def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index, smallest


def selectionSort(arr):
    newArr = []
    sortArr = arr[:]
    for i in range(len(sortArr)):
        smallest_index, _ = findSmallest(sortArr)
        newArr.append(sortArr.pop(smallest_index))
    return newArr


def printSmallestSort(data):
    index, smallest_value = findSmallest(data)
    sort_value = selectionSort(data)
    print(
        f"Smaller element index is {index}. "
        f"Smaller element is {smallest_value}. "
        f"Sorting is {sort_value}"
    )


data = [4, 2, 7, 1, 5]
printSmallestSort(data)
