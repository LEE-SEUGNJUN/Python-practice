##code09-05에 다음 기능을 추가해보자.
##1. 숫자1,연산자,숫자2 순서로 입력받는다 2.제곱(**)연산자 추가 3. 0으로 나누려고 하면 메세지를 출력하고 계산되지 않도록함
def calc(v1,op,v2):
    result=0
    if op=="+":
        result=v1+v2
    elif op=="-":
        result=v1-v2
    elif op=="*":
        result=v1*v2
    elif op=="/":
        result=v1/v2
    elif op=="**": ## **연산자를 함수에 추가
        result=v1**v2
    else :
        return "잘못 입력하셨습니다"
    return result
res=0
var1,var2,oper=0,0,""
oper=input("계산을 입력하세요 (+,-,*,/,**)")
var1=int(input("첫번째 수를 입력하세요 : "))
var2=int(input("두번째 수를 입력하세요 : "))
if oper=="/" and var2==0 : ##oper를 "/"로 지정했고, var2가 0이라면 if문 실행 아니라면 else문 실행
    print("0으로 나눌수 없습니다")
else :
    res=calc(var1,oper,var2)## 숫자1,연산자,숫자2 순서로 함수에 넣음
print("##계산기 : %d %s %d = %d "% (var1,oper,var2,res))
