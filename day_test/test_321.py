def fibonacci_1(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_1(n-1)+fibonacci_1(n-2)

def fibonacci_memo(n):
    dic = {0:1,1:1}
    if n in dic:
        return dic[n]
    else:
        result = fibonacci_memo(n-1)+fibonacci_memo(n-2)
        dic[n] = result
        return result

def fibonacci_2(n):
    memo={0:1,1:1}
    for i in range(2,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n]

def fib_3(n):
    assert n >= 0
    list_result = [1,1]
    for i in range(2,n+1):
        list_result.append(list_result[i-1]+list_result[i-2])
    return list_result[n]

if __name__ == "__main__":
    for i in range(10):
        print(fibonacci_1(i))
    
    for i in range(10):
        print(fibonacci_2(i))

    for i in range(10):
        print(fib_3(i))

    print(fibonacci_memo(4))