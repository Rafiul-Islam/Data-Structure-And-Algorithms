def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    else:
        return -1


li = [1, 2, 3, 4, 5, 6, 7]
target = 10
print("Element found at index", linear_search(li, target))
