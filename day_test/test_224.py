
from operator import le


def insertionSort(arr):
    for i in range(len(arr)):
        cursor=arr[i]
        j=i
        while j >0 and arr[j-1] > cursor:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=cursor
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid=len(arr)//2
    left,right=mergeSort(arr[:mid]),mergeSort(arr[mid:])

    return merge(left,right,arr.copy())

def merge(left,right,merged):
    left_cursor,right_cursor=0,0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor+=1
        else:
            merged[left_cursor+right_cursor]=right[right_cursor]
            right_cursor+=1
    
    for left_cursor in range(left_cursor,len(left)):
        merged[left_cursor+right_cursor]=left[left_cursor]
    for right_cursor in range(right_cursor,len(right)):
        merged[left_cursor+right_cursor]=right[right_cursor]

    return merged


def binarySearch(arr,query):
    lo,hi=0,len(arr)-1
    
    while lo<=hi:
        mid = (lo+hi)//2
        if arr[mid] == query:
            return mid
        elif query<arr[mid]:
            hi=mid-1
        else:
            lo=mid+1
    return None

def binary_Search(arr,query,lo,hi):
    if lo > hi:
        return None
    mid=(lo+hi)//2
    if query==arr[mid]:
        return mid
    elif query< arr[mid]:
        return binary_Search(arr,query,lo,mid-1)
    else:
        return binary_Search(arr,query,mid+1,hi)




if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    print(binarySearch(arr,4))
    print(binary_Search(arr,4,0,len(arr)-1))
    print(insertionSort([8271,91876,19,29,00,12,3]))
    print(mergeSort([8271,91876,19,29,00,12,3]))