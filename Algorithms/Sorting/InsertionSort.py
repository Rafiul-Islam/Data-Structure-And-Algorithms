# 64, 34, 25, 12, 22, 11, 90
def insertion_sort(li):
    for i in range(1, len(li)):
        item = li[i]
        j = i - 1
        while j >= 0 and li[j] > item:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = item
    return li

length_of_list = int(input("List length: "))
print("Enter list elements in one line with space: ")
li = list(map(int, str(input()).strip().split(" ")))
print(insertion_sort(li))
