def pivot_place(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last

    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right


def quick_sort(li, first, last):
    if first < last:
        p = pivot_place(li, first, last)
        quick_sort(li, first, p - 1)
        quick_sort(li, p + 1, last)


if __name__ == '__main__':
    li = list(map(int, input().strip().split(" ")))
    first = 0
    last = len(li) - 1
    quick_sort(li, first, last)
    print(*li)
