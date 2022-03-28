'''
Method1: Brute-Force Recursion / Exhaustive Search
Time Complexity: O(2^n)
Auxiliary Space: O(1)
'''

# Case1: item is in the optimal subset
# Case2: item is not in the optimal subset

def knapSack(W,wt,val,n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    if wt[n-1] > W :
        return knapSack(W,wt,val,n-1)
    else:
        return max(knapSack(W,wt,val,n-1),
                   val[n-1]+knapSack(W-wt[n-1],wt,val,n-1))

'''
Time: O(N*W)
Space: O(N*W)
'''
def knapSackDP(W,wt,val,n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif wt[i-1] <= j:
                K[i][j] = max(K[i-1][j], val[i-1]+K[i-1][j-wt[i-1]])
            else:
                K[i][j] = K[i-1][j]
    return K[n][W]

'''
Improvement space complexity
Time: O(NW)
Space:O(2W)
'''
def knapSackDP2(W,wt,val,n):
    K=[[0 for x in range(W+1)] for y in range(2)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                K[i%2][j] = 0
            elif wt[i-1] <= j:
                K[i % 2][j] = max(K[(i-1) % 2][j], val[i-1]+K[(i-1) % 2][j-wt[i-1]])
            else:
                K[i % 2][j] = K[(i-1) % 2][j]
    return K[n%2][W]

if __name__ == "__main__":
    val = [60,100,120]
    wt = [10,20,30]
    W = 50
    n = len(val)

    print(knapSack(W,wt,val,n))
    print(knapSackDP(W,wt,val,n))
    print(knapSackDP2(W,wt,val,n))