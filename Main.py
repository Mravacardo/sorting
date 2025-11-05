# mylist = [10, 3, 6, 2, 8, 1, 7, 5, 9, 4]
# mylist.sort(reverse = True)
# print(mylist)
# mylist.sort(reverse = False)
# print(mylist)
#bubble sort
# for i in range(0, len(mylist)):
#     for j in range(i, len(mylist)):
#       if mylist[i] < mylist[j]:
#           mylist[i],mylist[j] = mylist[j], mylist[i]

# print(mylist)
#insertion sort
# for i in range(0, len(mylist)):
#   minElement = 10000000
#   minLocation = -1
#   for j in range(i, len(mylist)):
#     if minElement > mylist[j]:
#       minElement = mylist[j]
#       minLocation = j
#       mylist[i],mylist[j] = mylist[j], mylist[i]

# print(mylist)
# merge sort
# def merge(arr, low, mid, high):
#     c = []
#     start1 = low
#     start2 = mid+1

#     while start1 <= mid and start2 <=high:
#       if arr[start1] < arr[start2]:
#         c.append(arr[start1])
#         start1 += 1
#       else:
#         c.append(start2)
#         start2 += 1

#     while start1 <= mid:
#       c.append(arr[start1])
#       start1 += 1

#     while start2 <= high:
#       c.append(arr[start2])
#       start2 += 1

#     k = 0
#     for i in range(low, high+1):
#       arr[i] = c[k]
#       k += 1

# def mergeSort(arr, low, high):
#   if low < high:
#     mid = (low + high) // 2
#     mergeSort(arr, low, mid)
#     mergeSort(arr, mid+1, high)
#     merge(arr, low, mid, high)

# arr = [12, 11, 13, 5, 8, 3]
# n = len(arr)
# mergeSort(arr, 0, n-1)
# print(arr)
# merge sort2
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])

#     return merge(left_half, right_half)

# def merge(left, right):
#     sorted_array = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             sorted_array.append(left[i])
#             i += 1
#         else:
#             sorted_array.append(right[j])
#             j += 1

#     sorted_array.extend(left[i:])
#     sorted_array.extend(right[j:])
#     return sorted_array

# if __name__ == "__main__":
#     arr = [34, 17, 64, 53, 9, 47, 30]
#     print("Original array:", arr)
#     sorted_arr = merge_sort(arr)
#     print("Sorted array:", sorted_arr)
