a = 10
b = 14  # b값을 13으로 수정하면 첫번째 조건문을 만족하지 않음
if (a % 2 == 0) and (b % 2 == 0) :  # 첫번째 조건문
    print('두 수 모두 짝수입니다.')
if (a % 2 == 0) or (b % 2 == 0) :   # 두번째 조건문
    print('두 수 중 하나 이상이 짝수입니다.')