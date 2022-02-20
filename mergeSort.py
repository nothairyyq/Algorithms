
def mergeSort(arr):
    """Merge Sort
       Complexity: O(n log(n))
    """
    # Recursive base case:
    if len(arr)<=1:
        return arr

    mid = len(arr) // 2  # floor divided
    left,right = mergeSort(arr[:mid]),mergeSort(arr[mid:]) #performe mergesort on both halves

    # Merge each side together
    return merge(left,right,arr.copy())

def merge(left,right,merged):
    """merge
       Complexity: O(n)
    """

    left_cursor, right_cursor = 0,0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor]<=right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor+=1
        else:
            merged[left_cursor+right_cursor]=right[right_cursor]
            right_cursor+=1
    
    #Add the left, if there's any left to the result
    for left_cursor in range(left_cursor,len(left)):
        merged[left_cursor+right_cursor]=left[left_cursor]
    for right_cursor in range(right_cursor,len(right)):
        merged[left_cursor+right_cursor]=right[right_cursor]

    return merged

if __name__ == "__main__":
    arr=[6,8,4,6,2,3]
    print(mergeSort(arr))