def insertion_sort(arr, simulation=False):
    """ Insertion Sort
        Complexity: O(n^2)
    """
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > cursor:
            arr[pos]=arr[pos-1]
            pos-=1
        
        #break and the final swap
        arr[pos] = cursor

        if simulation:
            iteration+=1
            print("iteration",iteration,":",*arr)

    return arr

if __name__ == "__main__":
    arr=[6,8,4,6,2,3]
    print(insertion_sort(arr,simulation=True))
