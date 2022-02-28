def insertionSort(arr):
    '''
    O(n^2)
    O(1) in-place
    '''
    n=len(arr)
    for j in range(1,n):
        key = arr[j]
        i=j
        while i>0 and arr[i-1]>key:
            arr[i]=arr[i-1]
            i-=1
        arr[i]=key
    return arr

def mergeSort(arr):
    '''
    O(n logn)
    O(n)
    '''
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right,arr.copy())

def merge(left,right,merged):
    #o(N)
    l,r=0,0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged[l+r] = left[l]
            l+=1
        else:
            merged[l+r] = right[r]
            r+=1
    for l in range(l,len(left)):
        merged[l+r]=left[l]
    for r in range(r,len(right)):
        merged[l+r]=right[r]

    return merged

def selectionSort(arr):
    '''
    O(n^2)
    O(1)
    '''
    n=len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

def quickSort(arr,p,r):
    '''
    O(n logn)
    O(log n)
    '''
    if p<r:
        i=partition(arr,p,r)
        quickSort(arr,p,i-1)
        quickSort(arr,i+1,r)
    return arr

def partition(arr,p,q):
    flag=arr[p]
    i=p
    for j in range(i+1,q):
        if arr[j]<flag:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i],arr[p]=arr[p],arr[i]
    return  i

def heapify(arr,n,root):
    #O(log n)
    l=2*root+1
    r=2*root+2
    largest = root
    if l < n and arr[l] > arr[largest]:
        largest=l
    if r < n and arr[r] > arr[largest]:
        largest=r
    if largest != root:
        arr[largest],arr[root] = arr[root],arr[largest]
        heapify(arr,n,largest)

def heapSort(arr):
    '''
    O(nlogn)
    '''
    # build a heap
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    
    # heap sort
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
    return arr

if __name__ == "__main__":
    arr = [4,1,9,0,1,2,38,9,1]
    print(insertionSort(arr))
    arr = [4,1,9,0,1,2,38,9,1]
    print(selectionSort(arr))
    arr = [4,1,9,0,1,2,38,9,1]
    print(mergeSort(arr))
    arr = [4,1,9,0,1,2,38,9,1]
    print(quickSort(arr,0,len(arr)))
    arr=[1,2,3,4,1,9,0,1,2,38,9,1]
    print(heapSort(arr))