##oct(), hex() 등등 내장라이브러리를 사용하지않고 진수변환 함수 구현하기
def deci_to_any(n,b):
    result=""
    while (n!=0): ##n이 0아니면 무한반복
        if n%b==10:  ##16진수는 b로 나누고나서 나머지가 15까지 있기때문에 숫자로 표현되는게아닌 16진수 표현법으로 고치게끔 if~else문을 구현했다.
            result="A"+result
        elif n%b==11:
            result="B"+result
        elif n%b==12:
            result="C"+result
        elif n%b==13:
            result="D"+result
        elif n%b==14:
            result="E"+result
        elif n%b==15:
            result="F"+result
        else :
            result=(str(n%b)+result) ##임의의 숫자를 b진수로 바꿀라면 n을 b로 나눈후 나머지를 역순으로 하면된다.
        n=n//b ## 나눈후엔 n을 b로 나눈 몫을 정수형태로 반환한다.
    return result
asd=deci_to_any(61,2)
print(asd)