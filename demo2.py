from ast import List


class Solution:

    #Given two lists X and Y, each containing n numbers already in sorted order.
    #find the median of all 2n elements in arrays X and Y
    def findMedian(self,x,y):
        n = len(x) + len(y)
        if n % 2 == 1:
            return self.findKth(x,y,n//2 + 1)
        else:
            return (self.findKth(x,y,n//2) + self.findKth(x,y,n//2 + 1)) / 2.0
    def findKth(self,x,y,n):
        if len(x) == 0:
            return y[n-1]
        if len(y) == 0:
            return x[n-1]
        if n == 1:
            return min(x[0],y[0])
        xMid = x[n//2 - 1] if len(x) >= n//2 else None
        yMid = y[n//2 - 1] if len(y) >= n//2 else None
        if xMid == None:
            return self.findKth(y,x[n//2:],n-n//2)
        if yMid == None:
            return self.findKth(x[n//2:],y,n-n//2)
        if xMid > yMid:
            return self.findKth(x[n//2:],y,n-n//2)
        else:
            return self.findKth(x,y[n//2:],n-n//2)

if __name__ == "__main__":
    s=Solution()
    print(s.findMedian([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]))