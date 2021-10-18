num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))
sum = 0
for i in range(num1,num2+1):
    for q in range(2,i) :
        if i % q== 0 :
            break
    else :
        sum = sum + i

print(sum)