'''
Time: O(n)
'''
def assemb(l,t):
    x1 = [l[0][0]]
    x2 = [l[1][0]]
    n = len(l[0])
    for j in range(1,n):
        x1.append(min((x1[j-1]+l[0][j]),(x2[j-1]+t[1][j]+l[0][j])))
        x2.append(min((x2[j-1]+l[1][j]),(x1[j-1]+t[0][j]+l[1][j])))
    return min(x1[n-1],x2[n-1])

def assemb_1(l,t):
    x1 = l[0][0]
    x2 = l[1][0]
    n = len(l[0])
    for j in range(1,n):
        l1=min((x1+l[0][j]),(x2+t[1][j]+l[0][j]))
        l2=min((x2+l[1][j]),(x1+t[0][j]+l[1][j]))
        x1,x2=l1,l2
    return min(x1,x2)
if __name__ == "__main__":
    l = [[5,5,9,4],[15,4,3,7]]
    t = [[0,2,4,1],[0,1,11,2]]
    print(assemb(l,t))
    print(assemb_1(l,t))
