def power(a,n):
    if n == 0:
        ans = 1
    elif n == 1:
        ans = a
    else:
        ans=power(a,n//2)
        ans=ans*ans
        if n%2:
            ans=ans*a
        
    return ans

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mat(x:float,n:int):
            if n == 0:
                ans = 1.0
            elif n == 1:
                ans = x
            else:
                ans=mat(x,n//2)
                ans=ans*ans
                if n%2:
                    ans=ans*x
            return ans
        if n >= 0:
            return mat(x, n)
        else:
            return 1.0 / mat(x, -n)

        
if __name__ =="__main__":
    print(power(2,4))