# 근의공식 input(입력)로 호출
a=float(input("2차항의 계수 입력: "))
b=float(input("2차항의 계수 입력: "))
c=float(input("상수 입력: "))

# (a*x^2)+(b*x)+c
r1 = (-b+(b ** 2 - 4 * a * c) ** 0.5)/ (2 * a)
r2 = (-b-(b ** 2 - 4 * a * c) ** 0.5)/ (2 * a)
print(r1, r2)

# 근의공식 함수로 호출
def print_root(a, b, c) :
    r1 = (-b+(b ** 2 - 4 * a * c) ** (1/2))/ (2 * a)
    r2 = (-b-(b ** 2 - 4 * a * c) ** 0.5)/ (2 * a)

    print('해는', r1, '또는', r2)

print_root(2, -1, -6)
