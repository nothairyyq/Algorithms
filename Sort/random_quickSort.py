import random

def quickSort(arr,p,r):
    if p < r:
        q=random_partition(arr,p,r)
        quickSort(arr,p,q)
        quickSort(arr,q+1,r)

    return arr

def random_partition(arr,p,q):
    i=random.randint(p,q-1)
    arr[p],arr[i]=arr[i],arr[p]
    return partition(arr,p,q)

def partition(arr,p,q):
    x=arr[p] # x is pivot
    i = p
    for j in range(p+1,q):
        if arr[j] <= x: 
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[p],arr[i]=arr[i],arr[p]

    return i

if __name__ == "__main__":
    arr=[6,10,13,5,8,3,2,11]
    print(quickSort(arr,0,len(arr)))