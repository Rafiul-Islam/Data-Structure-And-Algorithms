def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            print(f"{target} exist in the list and the index is: {index}")
            return
    else:
        print(f"{target} does not exist in the following list")


li = [1, 2, 3, 4, 5, 6, 7]
target = 5
linear_search(li, target)
