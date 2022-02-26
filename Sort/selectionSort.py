'''
O(n^2)
'''
def selectionSort(arr):
    for i in range(len(arr)):
        minimal = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minimal]:
                minimal=j
        arr[minimal], arr[i] = arr[i], arr[minimal]
    return arr

if __name__ == "__main__":
    print(selectionSort([2,3,8,1,0,2]))