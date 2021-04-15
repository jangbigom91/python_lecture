# 재귀함수 : 함수 내부에서 자기 자신을 호출하는 함수
def factorial(n) :
    if n <= 1 :
        return 1
    else :
        return n * factorial(n-1)

n = 10
print('{}! = {}'.format(n, factorial(n)))