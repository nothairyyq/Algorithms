from statistics import median
from tkinter import N
from typing import List

class Solution:
    def maxPathSum(self, grid: List[List[int]]):
        #Time: O(ij)
        #Space: O(1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

    def allPaths(self,graph):
        #Time:O(n*2^n)
        #Space:O(n)
        paths = []
        path = []
    
        def dfs(graph, node) :
            path.append(node)
            if node not in graph.keys():
                paths.append(path.copy())
                return
            for i in graph[node]:
                dfs(graph, i)
                path.pop()
    
        dfs(graph, list(graph.keys())[0])
        return paths


    def findMedian(self, nums1: List[int], nums2: List[int]) -> float: 
        #Time: O(log(n))
        #Space: O(1)
        size1 = len(nums1)

        left = 0
        right = size1      

        while left < right:
            line1 = (left + right) // 2
            line2 = (size1 + size1 + 1) // 2 - line1

            if nums1[line1] < nums2[line2-1]:
                left = line1 + 1
            else :
                right = line1 
        
        line1 = left
        line2 = (size1 + size1 + 1) // 2 - line1

        nums1LeftMax = (-float('inf') if line1 == 0 else nums1[line1-1])
        nums1RightMin = (float('inf') if line1 == size1  else nums1[line1])
        nums2LeftMax = (-float('inf') if line2 == 0 else nums2[line2-1])
        nums2RightMin = (float('inf') if line2 == size1 else nums2[line2])

        if (size1 + size1) % 2 != 0:
            return max(nums1LeftMax,nums2LeftMax)
        else :
            return (max(nums1LeftMax,nums2LeftMax) + min(nums1RightMin,nums2RightMin)) / 2
    
    def LongestPalindromicPrefix(self,string):
        #Time: O(n^2)
        #Space: O(n)
        n = len(string)
        max_len = 0
     
        for l in range(0, n + 1):
            temp = string[0:l]
            temp2 = temp
            temp3 = temp2[::-1]
            
            if temp == temp3:
                max_len = l
        return string[0:max_len]

    
    def getMedian(x,y):
        n = len(x)
        if n == 0:
            return -1
        elif n == 1:
            return(x[0]+x[0])/2.0
        elif n == 2:
            return (max(x[0],y[1])+min(x[1],y[0])) / 2.0
        else:
            x_media = median(x)
            y_media = median(y)
            if x_media < y_media:
                if n % 2 == 0:
                    return getMedian(x[:int(n/2)+1],y[int(n/2)-1])
                else:
                    return getMedian
    def median(arr):
        middle = (len(arr)-1)//2
        if middle % 2 == 0:
            return(arr[middle])
        else:
            return(arr[middle] + arr[middle+1])/2.0


    


if __name__ == "__main__":
    print(median([1,2,3,4,5]))
    