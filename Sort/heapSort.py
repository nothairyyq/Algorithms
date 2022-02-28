def heapSort(arr):
    for i in range(len(arr)-1,0,-1):
        maxHeapify(arr,i+1)
        arr[0],arr[i]=arr[i],arr[0]

    return arr

def maxHeapify(arr,end):
    # end = len(arr)
    last_parent =  end // 2 - 1
    last_node = end - 1

    #iterate from last parent to first
    for parent in range(last_parent,-1,-1):
        current_parent = parent

        #iterate from current_parent to last_parent
        while current_parent<=last_parent:
            child = 2*current_parent + 1

            # Find greatest child of current parent
            if child + 1 <= last_node and arr[child] < arr[child+1]:
                child+=1

            # Find greatest node of current sub-tree
            if arr[child]>arr[current_parent]:
                arr[child],arr[current_parent] = arr[current_parent],arr[child]
                current_parent = child
            else:
                break  #current_parent is greatest, no swap
    return arr


def heapify(arr, n, root):
    largest = root # Initialize largest as root
    left = 2*root + 1    # left = 2*i + 1
    right = 2*root + 2    # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

 
    # See if right child of root exists and is
    # greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

 
    # Change root, if needed
    if largest != root :
        arr[largest],arr[root] = arr[root],arr[largest]    # swap
        # Heapify the root.
        heapify(arr,n,largest)

def heap_sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
        print(arr)

    return arr


if __name__ == "__main__":

    arr=[1,2,3,4,5,6,7]
    print(heap_sort(arr))
    