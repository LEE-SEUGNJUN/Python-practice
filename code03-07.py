num1 = int(input("시프트할 숫자는 ?? : "))
num2 = int(input("출력할 횟수는 ?? : "))
i = 0
for i in range(1,num2+1) :
    print("{:d}<<{:d}= {:d}".format(num1,i,num1<<i))
for i in range(1,num2+1) :
    print("{:d}>>{:d}= {:d}".format(num1,i,num1>>i))