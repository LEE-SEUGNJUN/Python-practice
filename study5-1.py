num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))
num3 = int(input("몇씩 증가 하게끔 할까요 ? "))
sum=0
for i in range(num1,num2+1,num3):
    sum = sum+i

print("{:d}+{:d}+...+{:d}은 {:d}입니다".format(num1,num3+1,num2,sum))
    