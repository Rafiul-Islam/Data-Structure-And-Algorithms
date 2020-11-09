def selection_sort(li):
    for i in range(len(li)):
        index_of_min_value = i
        for j in range(i + 1, len(li)):
            if li[j] < li[index_of_min_value]:
                index_of_min_value = j
        if li[i] > li[index_of_min_value]:
            li[i], li[index_of_min_value] = li[index_of_min_value], li[i]
    return li


length_of_list = int(input("List length: "))
print("Enter list elements in one line with space: ")
li = list(map(int, str(input()).strip().split(" ")))
print(selection_sort(li))
