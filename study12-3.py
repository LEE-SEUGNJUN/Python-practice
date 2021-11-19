##code12-12를 활용해서 1~1000,1~100000,1~10000000 각각의 합을 계산하는 스레드 프로그램을 작성하시자.

import threading
import time
## 클래스 선언 부분 ##
class Calculate:
    def __init__(self,name) : ## 인스턴스 생성시 __init__ 함수의 필드대로 자동 초기화 
        self.name=name ##생성할때의 매개변수 값으로 name값 설정
        
    def Calcul(self,start,end) : ## 쓰레드생성할때 타겟에다가 start,end 매개변수 넣어줄것임
        result=0 ## result값 초기화 
        for i in range(start,end+1): ## start부터 end+1 (ex) end==1000이라하면 999까지밖에 안더하기때문에 1 더함)
            result+=i ##결과를 받는 변수 result
        print("%d+%d+%d....+%d = %d" % (start,start+1,start+2,end,result))##책과 동일하게 표현하기위함.
        ##다른 인스턴스 name을 따서도 표현해 보았다.
        print("%s = %d" % (self.name, result))
# 메인 코드 부분 #
cal1=Calculate("1~1000연산 인스턴스") ##괄호안에 들어간 문장 = 인스턴스의 name
cal2=Calculate("1~10000000연산 인스턴스")
cal3=Calculate("1~10000000연산 인스턴스")
th1=threading.Thread(target=cal1.Calcul(1,1000)) ##쓰레드 생성
th2=threading.Thread(target=cal2.Calcul(1,100000))
th3=threading.Thread(target=cal3.Calcul(1,10000000))
th1.start() ##스레드 시작
th2.start()
th3.start()