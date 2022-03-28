'''
Simple Method
Time Complexity: O(2^n)
'''

def lcs(X,Y,m,n):
    if m == 0 or n == 0 :
        return 0
    elif X[m-1] == Y[n-1]:
        return lcs(X,Y,m-1,n-1)+1
    else:
        return max(lcs(X,Y,m,n-1),lcs(X,Y,m-1,n))


'''
dp method
Time: O(MN)
'''
def lcs_DP(X,Y):
    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[m][n]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("LCS:",lcs(X,Y,len(X),len(Y)))
    print("LCS:",lcs_DP(X,Y))