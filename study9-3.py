##code09-11.py에서 2에서 10개까지 
##몇개를 매개변수로 사용하든지 합계를 구하도록 para_func()함수를 수정해보자

##함수 선언 부분##
def para_func(*asd):
    result=0
    for i in asd : ##var가 튜플형식으로 들어오니까 하나씩 받아들여 i에 넣고 반복문으로 result에 수를 하나씩 다 더한다
        result+=i
    return result ## 함수를 종료하고 result를 호출한 장소로 보낸다
hap=0
hap=para_func(10,20) ##매개변수 2개
print("매개변수가 2개인 함수를 호출한 결과==> ",hap)
hap=para_func(1,2,3,4,5,6,7,8,9,10) ##매개변수 10개
print("매개변수가 10개인 함수를 호출한 결과==>",hap)
