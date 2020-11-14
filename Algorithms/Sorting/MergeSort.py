def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = int(len(li) / 2)
    left, right = merge_sort(li[:mid]), merge_sort(li[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result


if __name__ == '__main__':
    li = [2, 5, 7, 1, 9]
    print(*li)
    print(*merge_sort(li))
