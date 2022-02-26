def insertionSort(arr):
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    for i in range(1,len(arr)):
        j=i
        val=arr[i]
        while j > 0 and arr[j-1] > val:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=val
    return arr

def mergeSort(arr):
    '''
    Time: O(nlog(n))
    Space: O(n)
    '''
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])
    return merge(left,right,arr.copy())

def merge(left,right,merged):
    l,r=0,0
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            merged[l+r]= left[l]
            l+=1
        else:
            merged[l+r]=right[r]
            r+=1

    for l in range(l,len(left)):
        merged[l+r]=left[l]
    for r in range(r,len(right)):
        merged[l+r]=right[r]
    return merged

def selectionSort(arr):
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

def partition(arr,p,q):
    #选择一个flag，将arr中小于flag和大于flag的分成两派
    j=p
    x=arr[j]
    for i in range(p+1,len(arr)):
        if arr[i]<x:
           j+=1
           arr[i],arr[j]=arr[j],arr[i]
    arr[p],arr[j]=arr[j],arr[p]
    return j

def quickSort(arr,p,r):
    '''
    best and average Time: O(nlog(n))
    worst Time: O(n^2)
    Space: O(log n )
    '''
    if p<r:
        i=partition(arr,p,r)
        quickSort(arr,p,i)
        quickSort(arr,i+1,r)
    return arr

def random_partition(arr,p,q):
    import random
    i=random.randint(p,q-1)
    arr[i],arr[p]=arr[p],arr[i]
    return partition(arr,p,q)

def random_quickSort(arr,p,r):
    '''
    Time: O(n log(n))
    Worst Space: O(n)
    Best Space: O(log n)
    '''
    if p<r:
        i=random_partition(arr,p,r)
        quickSort(arr,p,i)
        quickSort(arr,i+1,r)
    return arr

if __name__ == "__main__":

    arr=[6,10,13,5,8,3,2,11]
    arr2=[61,83,42,61,20,3]
    arr3=[3,7,5,4,2,1]
    arr4=[5,1,1,2,0,0]

    if insertionSort(arr) == mergeSort(arr) and insertionSort(arr2) == mergeSort(arr2):
        print("true")
    print(selectionSort(arr),selectionSort(arr2))
    print(quickSort(arr2,0,len(arr2)))
    print(random_quickSort(arr4,0,len(arr4)))
   