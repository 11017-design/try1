def lsearch(arr, item):
    for i in range(len(arr)):
        if arr[i]==item:
            print(f"Element found at index: {i}")
            return
      
        
def bsearch(arr, item):
    f=0
    l=len(arr)-1
    while f<=l:
        mid=(f+l)//2
        if arr[mid]==item:
            print("Element found at index:",mid)
            return
        elif arr[mid]<item:
            f=mid-1
        else:
            l=mid+1
    
            
def SS(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

    
def MS(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = MS(left_half)
    right_half = MS(right_half)
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def QS(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QS(left) + middle + QS(right)


list1=[10,2,8,9,6]
list2=[4,6,8,12,19]
lsearch(list1,9)
bsearch(list2,6)
Selection=SS(list1)
Merge=MS(list1)
Quick=QS(list1)
print("Section Sort:\n", Selection)
print("Merge Sort:\n", Merge)
print("Quick Sort:\n", Quick)


