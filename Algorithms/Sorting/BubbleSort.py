# 64, 34, 25, 12, 22, 11, 90
def bubble_sort(li):
    for i in range(len(li)):
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


length_of_list = int(input("List length: "))
print("Enter list elements in one line with space: ")
li = list(map(int, str(input()).strip().split(" ")))
print(bubble_sort(li))
