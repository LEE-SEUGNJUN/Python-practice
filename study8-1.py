##문자열을 받아서 짝수번째 문자는 #으로 나오게끔 출력하기
str1 = "파이썬은완전재미있어요"

for i in range(0,len(str1)): ##인덱스 0부터 문자열길이까지 반복
    if (i%2!=0):
        print("#",end="") ##인덱스가 홀수일땐#
    else :
        print(str1[i],end="")##인덱스가 짝수일땐 글자그대로 출력
        