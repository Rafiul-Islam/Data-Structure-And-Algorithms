def binary_search(li, target):
    list_length = len(li)
    left = 0
    right = list_length - 1

    while left <= right:
        mid = (left + right) // 2
        if li[mid] == target:
            return mid
        if li[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1


if __name__ == '__main__':
    length_of_list = int(input("List length: "))
    print("Enter list elements in one line with space: ")
    li = list(map(str, str(input()).strip().split(" ")))
    target = input("Which element do you want to find: ")
    li.sort()
    print("Element found at index", binary_search(li, target))
