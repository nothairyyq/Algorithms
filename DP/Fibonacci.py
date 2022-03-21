'''
Recursion Method: O(2^n)
'''
from unittest import result


def fibonacci_1(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_1(n-1)+fibonacci_1(n-2)

'''
Memory Search
Time: O(n)
'''
def fibonacci_2(n):
    dic = {0:1,1:1}
    assert n >= 0
    if n in dic:
        return dic[n]
    else:
        result = fibonacci_2(n-1)+fibonacci_2(n-2)
        dic[n] = result
        return dic[n]

'''
Dynamic Programming
Time: O(n)
'''
def fibonacci_3(n):
    assert n >= 0
    list_result = [1,1]
    for i in range(2,n+1):
        list_result.append(fibonacci_3(n-1)+fibonacci_3(n-2))
    return list_result[n]

if __name__ == "__main__":
    for i in range(10):
        print(fibonacci_1(i))

    for i in range(10):
        print(fibonacci_2(i))

    for i in range(10):
        print(fibonacci_3(i))