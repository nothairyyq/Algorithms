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
    


if __name__ == "__main__":
    s = Solution()
    grid = [[1,3,4],[7,5,8],[2,6,3]]
    print(s.maxPathSum(grid=grid))
    m={"S":["A","B"],"A":["B","T"],"B":["T"]}
    print(s.allPaths(m))
    x = [1,2,3]
    y = [4,5,6]
    print(s.findMedian(x,y))
    print(s.LongestPalindromicPrefix("analysis"))
    