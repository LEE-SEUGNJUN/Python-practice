##1부터 100까지 사이에있는 7의 배수 합계를 구하는 코드
sum=0
for i in range(7,100,7): ##조건문을 걸어서 7의 배수를 구해도되지만
    sum = sum +i         ##다른방법으로 간단하게 코드를 작성해보았다
print(sum)

"""
sum=0
for i in range(1,100):
    if i % 7 == 0:
        sum=sum+i
print(sum)
이라 하여도된다
"""