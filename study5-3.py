num1 = int(input("소수인지 판별 할 수를 입력하세요. : "))

for i in range(2,num1) :
    if num1 % i == 0 :
        print("이 수는 소수가 아닙니다.")
        break
    else :
        print("이 수는 소수 입니다 ㅎㅎ.")
        break
